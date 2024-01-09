package model.expressions;

import exceptions.ExpressionEvaluationException;
import model.types.BoolValue;
import model.types.IValue;
import model.types.IntType;
import model.types.IntValue;
import model.utils.MyHeap;
import model.utils.MyIDictionary;
import model.utils.MyIHeap;

public class RelationalExpression implements IExpression {
    private final IExpression firstExpression, secondExpression;
    private final String operation;

    public RelationalExpression(IExpression firstExpression, IExpression secondExpression, String operation)
    {
        this.firstExpression = firstExpression;
        this.secondExpression = secondExpression;
        this.operation = operation;
    }

    @Override
    public IValue evaluate(MyIDictionary<String, IValue> symbolTable, MyIHeap heap) throws ExpressionEvaluationException {
        IValue firstValue = this.firstExpression.evaluate(symbolTable, heap);
        IValue secondValue = this.secondExpression.evaluate(symbolTable, heap);

        if (!firstValue.getType().equals(new IntType()))
            throw new ExpressionEvaluationException("First operand does not evaluate to an IntType!");

        if (!secondValue.getType().equals(new IntType()))
            throw new ExpressionEvaluationException("Second operand does not evaluate to an IntType!");

        int firstInteger = ((IntValue) firstValue).getValue();
        int secondInteger = ((IntValue) secondValue).getValue();

        return switch (operation) {
            case "<" -> new BoolValue(firstInteger < secondInteger);
            case "<=" -> new BoolValue(firstInteger <= secondInteger);
            case "==" -> new BoolValue(firstInteger == secondInteger);
            case "!=" -> new BoolValue(firstInteger != secondInteger);
            case ">" -> new BoolValue(firstInteger > secondInteger);
            case ">=" -> new BoolValue(firstInteger >= secondInteger);
            default -> throw new ExpressionEvaluationException("Invalid comparison between operands!");
        };

    }

    @Override
    public String toString() {
        return super.toString();
    }
}
