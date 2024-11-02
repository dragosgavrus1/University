package ubb.model.statements;

import ubb.exceptions.ExpressionEvaluationException;
import ubb.exceptions.InterpreterException;
import ubb.exceptions.StatementException;
import ubb.model.PrgState;
import ubb.model.types.IType;
import ubb.model.utils.MyIDictionary;
import ubb.model.utils.MyIStack;
import ubb.model.utils.MyStack;

public class ForkStatement implements IStatement{
    private final IStatement innerStatement;

    public ForkStatement(IStatement innerStatement)
    {
        this.innerStatement = innerStatement;
    }

    @Override
    public PrgState execute(PrgState currentState) throws StatementException, ExpressionEvaluationException, InterpreterException {
        MyIStack<IStatement> newThreadStack = new MyStack<>();
        newThreadStack.push(innerStatement);

        return new PrgState(newThreadStack, currentState.getSymbolTable().copy(), currentState.getOutputList(),
                currentState.getFileTable(), currentState.getHeap());
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        innerStatement.typeCheck(typeEnvironment.copy());
        return typeEnvironment;
    }

    @Override
    public String toString() {
        return "Fork(" + innerStatement + ")";
    }
}
