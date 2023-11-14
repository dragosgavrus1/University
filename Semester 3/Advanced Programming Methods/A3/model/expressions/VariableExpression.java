package model.expressions;

import exceptions.ExpressionEvaluationException;
import model.types.IValue;
import model.utils.MyIDictionary;

public class VariableExpression implements IExpression {
    private final String id;

    public VariableExpression(String id)
    {
        this.id = id;
    }

    @Override
    public IValue evaluate(MyIDictionary<String, IValue> symbolTable) throws ExpressionEvaluationException {
        return symbolTable.get(id);
    }

    @Override
    public String toString() {
        return "(" + id + ')';
    }
}
