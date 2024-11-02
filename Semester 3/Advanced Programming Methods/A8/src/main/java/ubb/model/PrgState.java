package ubb.model;

import ubb.exceptions.ExpressionEvaluationException;
import ubb.exceptions.InterpreterException;
import ubb.exceptions.StackException;
import ubb.exceptions.StatementException;
import ubb.model.statements.CompoundStatement;
import ubb.model.statements.IStatement;
import ubb.model.types.IValue;
import ubb.model.utils.*;

import java.io.BufferedReader;
import java.util.*;

public class PrgState {
    private MyIStack<IStatement> exeStack;
    private MyIDictionary<String, IValue> symbolTable;
    private MyIList<IValue> outputList;
    private final MyIDictionary<String, BufferedReader> fileTable;
    private final MyIHeap heap;
    private final int id;
    private static int currentId = 0;
    private static final Set<Integer> idSet = new TreeSet<>();

    public PrgState(IStatement program) {
        this.exeStack = new MyStack<>();
        this.symbolTable = new MyDictionary<>();
        this.outputList = new MyList<>();
        this.fileTable = new MyDictionary<>();
        this.heap = new MyHeap();

        this.exeStack.push(program);
        this.id = PrgState.getAvailableId();
    }

    public PrgState(MyIStack<IStatement> exeStack, MyIDictionary<String, IValue> symbolTable,
                    MyIList<IValue> outputList, MyIDictionary<String, BufferedReader> fileTable, MyIHeap heapTable)
    {
        this.exeStack = exeStack;
        this.symbolTable = symbolTable;
        this.outputList = outputList;
        this.fileTable = fileTable;
        this.heap = heapTable;

        this.id = PrgState.getAvailableId();
    }

    public int getId() {
        return id;
    }

    private static int getAvailableId() {
        synchronized (idSet) {
            PrgState.currentId +=1;
            idSet.add(currentId);
            return currentId;
        }
    }

    public MyIStack<IStatement> getStack()
    {
        return this.exeStack;
    }

    public void setExeStack(MyIStack<IStatement> newStack)
    {
        this.exeStack = newStack;
    }

    public MyIDictionary<String, IValue> getSymbolTable()
    {
        return this.symbolTable;
    }

    public void setSymbolTable(MyIDictionary<String, IValue> newSymbolTable)
    {
        this.symbolTable = newSymbolTable;
    }

    public MyIList<IValue> getOutputList()
    {
        return this.outputList;
    }

    public MyIDictionary<String, BufferedReader> getFileTable()
    {
        return this.fileTable;
    }

    public void setOutputList(MyList<IValue> newOutputList)
    {
        this.outputList = newOutputList;
    }

    public MyIHeap getHeap() {
        return heap;
    }

    public MyIDictionary<String, IValue> getSymTable() {
        return symbolTable;
    }

    public List<IStatement> getStackStatements() {
        ArrayList<IStatement> stackStatements = new ArrayList<>();

        if (exeStack.isEmpty())
            return stackStatements;

        Stack<IStatement> statements = new Stack<>();
        for (IStatement currentStatement : this.exeStack.getStackAsList())
            statements.push(currentStatement);

        while (!statements.isEmpty())
        {
            IStatement topStatement = statements.pop();
            if (topStatement instanceof CompoundStatement currentStatement)
            {
                statements.push(currentStatement.getSecondStatement());
                statements.push(currentStatement.getFirstStatement());
            }

            else
                stackStatements.add(topStatement);
        }

        return stackStatements;
    }

    @Override
    public String toString() {
        return "PrgState{" +
                "exeStack=" + exeStack +
                ", symbolTable=" + symbolTable +
                ", outputList=" + outputList +
                ", fileTable=" + fileTable +
                ", heap=" + heap +
                '}';
    }



    public Boolean isNotCompleted() {
        return !this.exeStack.isEmpty();
    }

    public PrgState executeOneStatement() throws StatementException, ExpressionEvaluationException, InterpreterException {
        try {
            IStatement currentStatement = exeStack.pop();
            return currentStatement.execute(this);
        }
        catch (StackException e)
        {
            throw new StatementException("Statements stack is empty!");
        }
    }
}
