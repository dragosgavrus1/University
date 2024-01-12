package model.expressions;

import exceptions.ExpressionEvaluationException;
import exceptions.InterpreterException;
import model.types.IType;
import model.types.IValue;
import model.utils.MyHeap;
import model.utils.MyIDictionary;
import model.utils.MyIHeap;

public interface IExpression {
    IValue evaluate(MyIDictionary<String, IValue> symbolTable, MyIHeap heap) throws ExpressionEvaluationException;
    IType typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException;
}