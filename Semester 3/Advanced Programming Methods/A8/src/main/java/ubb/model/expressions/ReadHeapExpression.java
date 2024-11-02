package ubb.model.expressions;

import ubb.exceptions.ExpressionEvaluationException;
import ubb.exceptions.InterpreterException;
import ubb.model.types.IType;
import ubb.model.types.IValue;
import ubb.model.types.RefType;
import ubb.model.types.RefValue;
import ubb.model.utils.MyIDictionary;
import ubb.model.utils.MyIHeap;

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
