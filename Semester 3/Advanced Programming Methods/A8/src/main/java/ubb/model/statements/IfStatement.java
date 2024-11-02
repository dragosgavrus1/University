package ubb.model.statements;

import ubb.exceptions.ExpressionEvaluationException;
import ubb.exceptions.InterpreterException;
import ubb.model.PrgState;
import ubb.model.expressions.IExpression;
import ubb.model.types.BoolType;
import ubb.model.types.BoolValue;
import ubb.model.types.IType;
import ubb.model.types.IValue;
import ubb.model.utils.MyIDictionary;
import ubb.model.utils.MyIStack;

public class IfStatement implements IStatement {
    private final IExpression expressionToEvaluate;
    private final IStatement firstStatement, secondStatement;

    public IfStatement(IExpression expressionToEvaluate, IStatement firstStatement, IStatement secondStatement)
    {
        this.expressionToEvaluate = expressionToEvaluate;
        this.firstStatement = firstStatement;
        this.secondStatement = secondStatement;
    }

    @Override
    public PrgState execute(PrgState currentState) throws ExpressionEvaluationException {
        MyIStack<IStatement> exeStack = currentState.getStack();

        IValue conditionToEvaluate = expressionToEvaluate.evaluate(currentState.getSymbolTable(), currentState.getHeap());

        if (!conditionToEvaluate.getType().equals(new BoolType()))
            throw new ExpressionEvaluationException("Conditional expression is not boolean!");

        BoolValue conditionValue = (BoolValue) conditionToEvaluate;

        if (conditionValue.getValue())
            exeStack.push(firstStatement);
        else
            exeStack.push(secondStatement);

        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        IType typeExpression = expressionToEvaluate.typeCheck(typeEnvironment);

        if(!typeExpression.equals(new BoolType()))
            throw new InterpreterException("Conditional expression is not boolean!");

        firstStatement.typeCheck(typeEnvironment.copy());
        secondStatement.typeCheck(typeEnvironment.copy());

        return typeEnvironment;
    }

    @Override
    public String toString() {
        return "if " + expressionToEvaluate + " then " + firstStatement
                + " else " + secondStatement ;
    }
}
