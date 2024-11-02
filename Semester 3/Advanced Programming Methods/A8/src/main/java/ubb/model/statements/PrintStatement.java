package ubb.model.statements;

import ubb.exceptions.ExpressionEvaluationException;
import ubb.exceptions.InterpreterException;
import ubb.model.PrgState;
import ubb.model.expressions.IExpression;
import ubb.model.types.IType;
import ubb.model.types.IValue;
import ubb.model.utils.MyIDictionary;
import ubb.model.utils.MyIList;

public class PrintStatement implements IStatement {
    private final IExpression expression;

    public PrintStatement(IExpression expression)
    {
        this.expression = expression;
    }

    @Override
    public PrgState execute(PrgState currentState) throws ExpressionEvaluationException {
        MyIList<IValue> outputList = currentState.getOutputList();

        outputList.add(expression.evaluate(currentState.getSymbolTable(), currentState.getHeap()));

        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        expression.typeCheck(typeEnvironment);
        return typeEnvironment;
    }

    @Override
    public String toString() {
        return "print " + expression ;
    }
}
