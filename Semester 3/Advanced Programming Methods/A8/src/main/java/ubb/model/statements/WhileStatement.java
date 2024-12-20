package ubb.model.statements;

import ubb.exceptions.ExpressionEvaluationException;
import ubb.exceptions.InterpreterException;
import ubb.exceptions.StatementException;
import ubb.model.PrgState;
import ubb.model.expressions.IExpression;
import ubb.model.types.BoolType;
import ubb.model.types.BoolValue;
import ubb.model.types.IType;
import ubb.model.types.IValue;
import ubb.model.utils.MyIDictionary;
import ubb.model.utils.MyIHeap;
import ubb.model.utils.MyIStack;

public class WhileStatement implements IStatement{
    private final IExpression expressionToEvaluate;
    private final IStatement innerStatement;

    public WhileStatement(IExpression expressionToEvaluate, IStatement innerStatement)
    {
        this.expressionToEvaluate = expressionToEvaluate;
        this.innerStatement = innerStatement;
    }

    @Override
    public PrgState execute(PrgState currentState) throws StatementException, ExpressionEvaluationException, InterpreterException {
        MyIDictionary<String, IValue> symbolTable = currentState.getSymbolTable();
        MyIHeap heapTable = currentState.getHeap();
        MyIStack<IStatement> programStack = currentState.getStack();

        IValue evaluatedExpression = expressionToEvaluate.evaluate(symbolTable, heapTable);

        // Check if the expressionToEvaluate evaluates to a boolean
        if (!evaluatedExpression.getType().equals(new BoolType()))
            throw new StatementException("Expression " + expressionToEvaluate.toString() + " is not of type BoolType!");

        BoolValue expressionValue = (BoolValue) evaluatedExpression;

        // If the expression is false, do not execute the innerStatement and return the current program state
        if (!expressionValue.getValue())
            return null;

        // Push the WhileStatement and the innerStatement onto the program stack to repeat the loop
        programStack.push(this);
        programStack.push(innerStatement);

        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        innerStatement.typeCheck(typeEnvironment.copy());
        IType typeExpression = expressionToEvaluate.typeCheck(typeEnvironment);

        if(!typeExpression.equals(new BoolType()))
            throw new InterpreterException("Conditional expression is not boolean!");

        return typeEnvironment;
    }

    @Override
    public String toString() {
        return "while(" + this.expressionToEvaluate + ") {" + this.innerStatement + "}";
    }
}
