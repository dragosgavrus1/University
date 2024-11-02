package ubb.model.expressions;

import ubb.exceptions.ExpressionEvaluationException;
import ubb.exceptions.InterpreterException;
import ubb.model.types.IType;
import ubb.model.types.IValue;
import ubb.model.utils.MyIDictionary;
import ubb.model.utils.MyIHeap;

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
