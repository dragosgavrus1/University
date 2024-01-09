package repository;

import model.PrgState;
import model.statements.IStatement;
import model.types.IValue;
import model.utils.MyIDictionary;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Repository implements IRepository {
    private PrgState program;
    private final String logFilePath;

    public Repository(String logFilePath)
    {
        this.logFilePath = logFilePath;
    }
    public Repository(PrgState program, String logFilePath)
    {
        this.program = program;
        this.logFilePath = logFilePath;
    }

    @Override
    public void addProgram(PrgState programToAdd) {
        this.program = programToAdd;
    }

    @Override
    public PrgState getCurrentProgram() {
        return program;
    }

    private void logExeStack(PrintWriter logFile) {
        logFile.println("ExeStack:");

        ArrayList<IStatement> stackStatements = (ArrayList<IStatement>) this.getCurrentProgram().getStackStatements();

        for (IStatement currentStatement : stackStatements)
            logFile.println(currentStatement.toString());

        logFile.println();
    }

    private void logSymbolTable(PrintWriter logFile)
    {
        logFile.println("SymTable:");

        MyIDictionary<String, IValue> symbolTable = this.getCurrentProgram().getSymbolTable();
        for (String key : symbolTable.getKeySet())
            logFile.println(key + " = " + symbolTable.get(key));

        logFile.println();
    }

    private void logOutput(PrintWriter logFile)
    {
        logFile.println("Output:");

        List<IValue> outputList = this.getCurrentProgram().getOutputList().getOutput();
        for (IValue currentValue : outputList)
            logFile.println(currentValue);

        logFile.println();
    }

    private void logFileTable(PrintWriter logFile)
    {
        logFile.println("File Table:");

        MyIDictionary<String, BufferedReader> fileTable = this.getCurrentProgram().getFileTable();
        for (String fileName : fileTable.getKeySet())
            logFile.println(fileName);

        logFile.println();
    }

    @Override
    public void logProgramState() throws IOException {
        PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
        this.logExeStack(logFile);
        this.logSymbolTable(logFile);
        this.logOutput(logFile);
        this.logFileTable(logFile);
        this.logHeap(logFile);
        logFile.println();
        logFile.close();
    }

    private void logHeap(PrintWriter logFile) {
        logFile.println("Heap:");

        Map<Integer, IValue> heap = this.getCurrentProgram().getHeap().getContent();
        for (IValue currentValue : heap.values())
            logFile.println(currentValue);

        logFile.println();
    }
}
