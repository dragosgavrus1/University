package model.statements;

import exceptions.ExpressionEvaluationException;
import exceptions.InterpreterException;
import model.types.IType;
import model.utils.MyIDictionary;
import model.utils.MyIStack;
import model.PrgState;

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
