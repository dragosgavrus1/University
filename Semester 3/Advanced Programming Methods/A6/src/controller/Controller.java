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
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.stream.Collectors;

public class Controller {
    private final IRepository repository;
    private ExecutorService threadsExecutor;

    public Controller(IRepository repository)
    {
        this.repository = repository;
    }

    public void addProgram(PrgState programToAdd)
    {
        repository.addProgram(programToAdd);
    }


    public void allSteps() throws StatementException, ExpressionEvaluationException, IOException, InterpreterException, InterruptedException {
        threadsExecutor = Executors.newFixedThreadPool(2);
        List<PrgState> programList = removeCompletedPrograms(repository.getProgramList());
        
        while (!programList.isEmpty())
        {
            this.updateHeap();
            this.oneStepForAllPrograms(programList);
            programList = removeCompletedPrograms(repository.getProgramList());
        }

        threadsExecutor.shutdownNow();
        repository.setProgramList(programList);
    }

    private void oneStepForAllPrograms(List<PrgState> programList) throws InterruptedException
    {
        List<Callable<PrgState>> callablesList = programList.stream()
                .map((PrgState program) -> (Callable<PrgState>) (program::executeOneStatement))
                .collect(Collectors.toList());

        List<PrgState> newProgramList = threadsExecutor.invokeAll(callablesList).stream()
                .map(future -> {
                    try {
                        return future.get();
                    } catch (Exception e) {
                        System.out.println(e.getMessage());
                        return null;
                    }
                })
                .filter(program -> program != null)
                .collect(Collectors.toList());

        programList.addAll(newProgramList);
        repository.setProgramList(programList);

        programList.forEach(this.repository::logProgramState);
    }

    List<PrgState> removeCompletedPrograms(List<PrgState> allPrograms)
    {
        return allPrograms.stream()
                .filter(program -> program.isNotCompleted())
                .collect(Collectors.toList());
    }

    Map<Integer, IValue> garbageCollector(List<Integer> symTableAddresses, Map<Integer, IValue> heap)
    {
        return heap.entrySet().stream()
                .filter(entry -> symTableAddresses.contains(entry.getKey()))
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue));
    }


    private void updateHeap()
    {
        PrgState firstProgram = this.repository.getProgramList().get(0);

        firstProgram.getHeap().setContent(
                this.garbageCollector(
                        this.getAddressFromSymTable(
                                this.repository.getProgramList().stream()
                                        .map(program -> program.getSymbolTable().getContent().values())
                                        .collect(Collectors.toList()),
                                firstProgram.getHeap().getContent()
                        ),
                        firstProgram.getHeap().getContent()
                ));
    }

    List<Integer> getAddressFromSymTable(List<Collection<IValue>> symbolTableValues, Map<Integer, IValue> heapTable)
    {
        List<Integer> allAddresses = new ArrayList<>();

        symbolTableValues.forEach(symbolTable -> symbolTable.stream()
                .filter(value -> value instanceof RefValue)
                .forEach( value -> {
                    while (value instanceof RefValue) {
                        allAddresses.add(((RefValue) value).getAddress());
                        value = heapTable.get(((RefValue) value).getAddress());
                    }
                })
        );

        return allAddresses;
    }

}
