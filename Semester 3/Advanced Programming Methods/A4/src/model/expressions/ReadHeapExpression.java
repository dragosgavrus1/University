package model.expressions;

import exceptions.ExpressionEvaluationException;
import model.types.IValue;
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
    public String toString() {
        return "readHeap(" + expression.toString() + ")";
    }
}
