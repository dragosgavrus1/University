package model.statements;


import exceptions.StatementException;
import model.*;
import model.types.*;
import model.utils.MyIDictionary;

public class VariableDeclarationStatement implements IStatement {
    private final String variableId;
    private final IType variableIType;

    public VariableDeclarationStatement(String variableId, IType variableIType)
    {
        this.variableId = variableId;
        this.variableIType = variableIType;
    }

    @Override
    public PrgState execute(PrgState currentState) throws StatementException {
        MyIDictionary<String, IValue> symbolTable = currentState.getSymbolTable();

        if (symbolTable.isDefined(variableId))
            throw new StatementException("Variable already defined!");

        if (variableIType.equals(new IntType()))
            symbolTable.put(variableId, new IntValue(0));

        else
            symbolTable.put(variableId, new BoolValue(false));

        return currentState;
    }

    @Override
    public String toString() {
        return "(" + variableIType + " " + variableId +  ')';
    }
}
