package model.expressions;

import exceptions.InterpreterException;
import model.types.IType;
import model.types.IValue;
import model.utils.MyHeap;
import model.utils.MyIDictionary;
import model.utils.MyIHeap;

public class ValueExpression implements IExpression {
    private final IValue value;

    public ValueExpression(IValue value)
    {
        this.value = value;
    }

    @Override
    public IValue evaluate(MyIDictionary<String, IValue> symbolTable, MyIHeap heap) {
        return value;
    }

    @Override
    public IType typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        return value.getType();
    }

    @Override
    public String toString() {
        return value.toString();
    }
}
