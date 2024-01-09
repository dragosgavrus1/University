package model.statements;

import exceptions.ExpressionEvaluationException;
import model.types.IValue;
import model.utils.MyIList;
import model.PrgState;
import model.expressions.IExpression;

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

        return currentState;
    }

    @Override
    public String toString() {
        return "print " + expression ;
    }
}
