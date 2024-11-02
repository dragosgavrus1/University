package ubb.model.statements;


import ubb.exceptions.InterpreterException;
import ubb.exceptions.StatementException;
import ubb.model.PrgState;
import ubb.model.types.IType;
import ubb.model.types.IValue;
import ubb.model.utils.MyIDictionary;

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

        symbolTable.put(variableId, variableIType.defaultValue());

        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        typeEnvironment.put(variableId, variableIType);
        return typeEnvironment;
    }

    @Override
    public String toString() {
        return variableIType + " " + variableId ;
    }
}
