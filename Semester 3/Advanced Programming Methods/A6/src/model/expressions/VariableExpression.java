package model.expressions;

import exceptions.ExpressionEvaluationException;
import exceptions.InterpreterException;
import model.types.IType;
import model.types.IValue;
import model.utils.MyHeap;
import model.utils.MyIDictionary;
import model.utils.MyIHeap;

public class VariableExpression implements IExpression {
    private final String id;

    public VariableExpression(String id)
    {
        this.id = id;
    }

    @Override
    public IValue evaluate(MyIDictionary<String, IValue> symbolTable, MyIHeap heap) throws ExpressionEvaluationException {
        return symbolTable.get(id);
    }

    @Override
    public IType typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        if(!typeEnvironment.isDefined(id))
            throw new InterpreterException("Variable " + id + " is not defined!");

        return typeEnvironment.get(id);
    }

    @Override
    public String toString() {
        return "(" + id + ')';
    }
}
