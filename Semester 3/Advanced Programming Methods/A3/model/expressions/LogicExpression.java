package model.expressions;


import exceptions.ExpressionEvaluationException;
import model.types.BoolType;
import model.types.BoolValue;
import model.types.IValue;
import model.utils.MyIDictionary;

public class LogicExpression implements IExpression {
    private final IExpression firstExpression, secondExpression;
    private final int operation;

    public LogicExpression(IExpression firstExpression, IExpression secondExpression, int operation)
    {
        this.firstExpression = firstExpression;
        this.secondExpression = secondExpression;
        this.operation = operation;
    }

    @Override
    public IValue evaluate(MyIDictionary<String, IValue> symbolTable) throws ExpressionEvaluationException {
        IValue firstValue = firstExpression.evaluate(symbolTable);
        IValue secondValue = secondExpression.evaluate(symbolTable);

        if (!firstValue.getType().equals(new BoolType()))
            throw new ExpressionEvaluationException("First operand is not bool!");

        if (!secondValue.getType().equals(new BoolType()))
            throw new ExpressionEvaluationException("Second operand is not bool!");

        BoolValue firstOperand = (BoolValue) firstValue;
        BoolValue secondOperand = (BoolValue) secondValue;

        switch (operation)
        {
            case 1: // LOGIC AND
                return new BoolValue(firstOperand.getValue() && secondOperand.getValue());

            case 2: // LOGIC OR
                return new BoolValue(firstOperand.getValue() || secondOperand.getValue());
        }

        return null;
    }

    @Override
    public String toString() {
        return switch (operation) {
            case 1 -> "(" + firstExpression + " && " + secondExpression + ")";
            case 2 -> "(" + firstExpression + " || " + secondExpression + ")";

            default -> "";
        };
    }
}
