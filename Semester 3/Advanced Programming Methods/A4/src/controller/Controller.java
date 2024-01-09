package controller;

import exceptions.ExpressionEvaluationException;
import exceptions.InterpreterException;
import exceptions.StackException;
import exceptions.StatementException;
import model.types.IValue;
import model.types.RefValue;
import repository.IRepository;
import model.statements.IStatement;
import model.utils.MyIStack;
import model.PrgState;

import java.io.IOException;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Controller {
    private final IRepository repository;

    public Controller(IRepository repository)
    {
        this.repository = repository;
    }

    public void addProgram(PrgState programToAdd)
    {
        repository.addProgram(programToAdd);
    }

    public PrgState getCurrentProgram()
    {
        return repository.getCurrentProgram();
    }

    public boolean isEmpty()
    {
        return this.repository.getCurrentProgram().getStack().isEmpty();
    }

    public PrgState executeOneStatement(PrgState currentState) throws StatementException, ExpressionEvaluationException, InterpreterException {
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

    public void executeAllStatements() throws StatementException, ExpressionEvaluationException, IOException, InterpreterException
    {
        PrgState currentState = repository.getCurrentProgram();
        while (!currentState.getStack().isEmpty())
        {
            this.executeOneStatement(currentState);
            this.repository.logProgramState();
            currentState.getHeap().setContent(unsafeGarbageCollector(
                    getAddressFromSymTable(currentState.getSymTable().getContent().values()), currentState.getHeap().getContent()));
            this.repository.logProgramState();
        }
    }

    Map<Integer, IValue> unsafeGarbageCollector(List<Integer> symTableAddresses, Map<Integer, IValue> heap)
    {
        return heap.entrySet().stream()
                .filter(entry -> symTableAddresses.contains(entry.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }


    List<Integer> getAddressFromSymTable(Collection<IValue> symTableValues)
    {
        return symTableValues.stream()
                .filter(value -> value instanceof RefValue)
                .map(value -> {RefValue value1 = (RefValue)value; return  value1.getAddress();})
                .collect(Collectors.toList());
    }

}
