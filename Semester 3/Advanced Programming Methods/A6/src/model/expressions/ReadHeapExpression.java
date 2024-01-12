package model.expressions;

import exceptions.ExpressionEvaluationException;
import exceptions.InterpreterException;
import model.types.IType;
import model.types.IValue;
import model.types.RefType;
import model.types.RefValue;
import model.utils.MyHeap;
import model.utils.MyIDictionary;
import model.utils.MyIHeap;

public class ReadHeapExpression implements IExpression{
    IExpression expression;
    public ReadHeapExpression(IExpression expression) {
        this.expression = expression;
    }

    @Override
    public IValue evaluate(MyIDictionary<String, IValue> symbolTable, MyIHeap heap) throws ExpressionEvaluationException {
        IValue expressionValue = expression.evaluate(symbolTable, heap);
        if (!(expressionValue instanceof RefValue expressionValueRef))
            throw new ExpressionEvaluationException("Expression is not a reference type!");

        int address = expressionValueRef.getAddress();
        IValue valueFound = heap.read(address);

        if(valueFound == null)
            throw new ExpressionEvaluationException("The address is not allocated in heap!");

        return valueFound;
    }

    @Override
    public IType typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        IType expressionType = expression.typeCheck(typeEnvironment);
        if (!(expressionType instanceof RefType))
            throw new InterpreterException("Expression is not a reference type!");

        return ((RefType) expressionType).getInner();
    }

    @Override
    public String toString() {
        return "readHeap(" + expression.toString() + ")";
    }
}
