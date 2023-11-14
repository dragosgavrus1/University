package controller;

import exceptions.ExpressionEvaluationException;
import exceptions.StackException;
import exceptions.StatementException;
import repository.IRepository;
import model.statements.IStatement;
import model.utils.MyIStack;
import model.PrgState;

public class Controller {
    private final IRepository programs;

    public Controller(IRepository programs)
    {
        this.programs = programs;
    }

    public void addProgram(PrgState programToAdd)
    {
        programs.addProgram(programToAdd);
    }

    public PrgState getCurrentProgram()
    {
        return programs.getCurrentProgram();
    }

    public boolean isEmpty()
    {
        return this.programs.getCurrentProgram().getStack().isEmpty();
    }

    public PrgState executeOneStatement(PrgState currentState) throws StatementException, ExpressionEvaluationException {
        MyIStack<IStatement> exeStack = currentState.getStack();

        try {
            IStatement currentStatement = exeStack.pop();
            return currentStatement.execute(currentState);
        }
        catch (StackException e)
        {
            throw new StatementException("Statements stack is empty!");
        }
    }

    public void executeAllStatements() throws StatementException, ExpressionEvaluationException
    {
        PrgState currentState = programs.getCurrentProgram();

        while (!currentState.getStack().isEmpty())
        {
            this.executeOneStatement(currentState);
        }
    }
}
