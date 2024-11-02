package ubb.model.expressions;

import ubb.exceptions.ExpressionEvaluationException;
import ubb.exceptions.InterpreterException;
import ubb.model.types.IType;
import ubb.model.types.IValue;
import ubb.model.utils.MyIDictionary;
import ubb.model.utils.MyIHeap;

public interface IExpression {
    IValue evaluate(MyIDictionary<String, IValue> symbolTable, MyIHeap heap) throws ExpressionEvaluationException;
    IType typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException;
}