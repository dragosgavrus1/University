package ubb.model.statements;

import ubb.exceptions.ExpressionEvaluationException;
import ubb.exceptions.InterpreterException;
import ubb.model.PrgState;
import ubb.model.types.IType;
import ubb.model.utils.MyIDictionary;
import ubb.model.utils.MyIStack;

public class CompoundStatement implements IStatement {
    private final IStatement firstStatement, secondStatement;

    public CompoundStatement(IStatement firstStatement, IStatement secondStatement)
    {
        this.firstStatement = firstStatement;
        this.secondStatement = secondStatement;
    }

    public IStatement getFirstStatement()
    {
        return this.firstStatement;
    }

    public IStatement getSecondStatement()
    {
        return this.secondStatement;
    }

    @Override
    public String toString() {
        return  firstStatement.toString() + "; " + secondStatement.toString() ;
    }

    @Override
    public PrgState execute(PrgState currentState) throws ExpressionEvaluationException {
        MyIStack<IStatement> exeStack = currentState.getStack();
        exeStack.push(secondStatement);
        exeStack.push(firstStatement);
        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        return secondStatement.typeCheck(firstStatement.typeCheck(typeEnvironment));
    }
}
