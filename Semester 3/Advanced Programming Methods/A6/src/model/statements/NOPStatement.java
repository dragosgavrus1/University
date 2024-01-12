package model.statements;

import exceptions.InterpreterException;
import model.PrgState;
import model.types.IType;
import model.utils.MyIDictionary;

public class NOPStatement implements IStatement {
    @Override
    public PrgState execute(PrgState currentState) {
        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        return typeEnvironment;
    }

    @Override
    public String toString() {
        return "NOP";
    }
}
