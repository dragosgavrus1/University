package ubb.repository;

import ubb.model.PrgState;
import ubb.model.statements.IStatement;
import ubb.model.types.IValue;
import ubb.model.utils.MyIDictionary;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Repository implements IRepository {
    private List<PrgState> programList;
    private final String logFilePath;

    public Repository(String logFilePath)
    {
        this.programList = new ArrayList<>();
        this.logFilePath = logFilePath;
    }
    public Repository(PrgState program, String logFilePath)
    {
        this.programList = new ArrayList<>(); // Initialize programList
        this.programList.add(program);
        this.logFilePath = logFilePath;
    }

    @Override
    public void addProgram(PrgState programToAdd) {
        this.programList.add(programToAdd);
    }


    private void logExeStack(PrintWriter logFile, PrgState currentProgram) {
        logFile.println("ExeStack:");

        ArrayList<IStatement> stackStatements = (ArrayList<IStatement>) currentProgram.getStackStatements();

        for (IStatement currentStatement : stackStatements)
            logFile.println(currentStatement.toString());

        logFile.println();
    }

    private void logSymbolTable(PrintWriter logFile, PrgState currentProgram)
    {
        logFile.println("SymTable:");

        MyIDictionary<String, IValue> symbolTable = currentProgram.getSymbolTable();
        for (String key : symbolTable.getKeySet())
            logFile.println(key + " = " + symbolTable.get(key));

        logFile.println();
    }

    private void logOutput(PrintWriter logFile, PrgState currentProgram)
    {
        logFile.println("Output:");

        List<IValue> outputList = currentProgram.getOutputList().getOutput();
        for (IValue currentValue : outputList)
            logFile.println(currentValue);

        logFile.println();
    }

    private void logFileTable(PrintWriter logFile, PrgState currentProgram)
    {
        logFile.println("File Table:");

        MyIDictionary<String, BufferedReader> fileTable = currentProgram.getFileTable();
        for (String fileName : fileTable.getKeySet())
            logFile.println(fileName);

        logFile.println();
    }

    private void logHeap(PrintWriter logFile, PrgState currentProgram) {
        logFile.println("Heap:");

        Map<Integer, IValue> heap = currentProgram.getHeap().getContent();
        for (IValue currentValue : heap.values())
            logFile.println(currentValue);

        logFile.println();
    }

    @Override
    public void logProgramState(PrgState program) {
        try{
            PrintWriter logFile = new PrintWriter(new BufferedWriter(new FileWriter(logFilePath, true)));
            logFile.println("Program ID: " + program.getId());
            this.logExeStack(logFile, program);
            this.logSymbolTable(logFile, program);
            this.logOutput(logFile, program);
            this.logFileTable(logFile, program);
            this.logHeap(logFile, program);
            logFile.println();
            logFile.close();
        }
        catch (IOException e) {}
    }

    @Override
    public List<PrgState> getProgramList() {
        return this.programList;
    }

    @Override
    public void setProgramList(List<PrgState> programList) {
        this.programList = programList;
    }


}
