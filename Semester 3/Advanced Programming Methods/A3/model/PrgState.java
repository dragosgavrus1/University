package model;

import model.statements.IStatement;
import model.types.IValue;
import model.utils.MyIDictionary;
import model.utils.MyIList;
import model.utils.MyIStack;
import model.utils.MyList;

public class PrgState {
    private MyIStack<IStatement> exeStack;
    private MyIDictionary<String, IValue> symbolTable;
    private MyIList<IValue> outputList;

    public PrgState(MyIStack<IStatement> exeStack, MyIDictionary<String, IValue> symbolTable,
                    MyList<IValue> outputList, IStatement program) {
        this.exeStack = exeStack;
        this.symbolTable = symbolTable;
        this.outputList = outputList;

        this.exeStack.push(program);
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

    public void setOutputList(MyList<IValue> newOutputList)
    {
        this.outputList = newOutputList;
    }

    @Override
    public String toString() {
        return "PrgState{" +
                "exeStack=" + exeStack +
                ", symbolTable=" + symbolTable +
                ", outputList=" + outputList +
                '}';
    }
}
