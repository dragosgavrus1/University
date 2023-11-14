package model.expressions;

import exceptions.ExpressionEvaluationException;
import model.types.IValue;
import model.utils.MyIDictionary;
public interface IExpression {
    IValue evaluate(MyIDictionary<String, IValue> symbolTable) throws ExpressionEvaluationException;
}