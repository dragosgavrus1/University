package ubb.model.expressions;

import ubb.exceptions.InterpreterException;
import ubb.model.types.IType;
import ubb.model.types.IValue;
import ubb.model.utils.MyIDictionary;
import ubb.model.utils.MyIHeap;

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
