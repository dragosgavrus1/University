package ubb.model.statements;

import ubb.exceptions.InterpreterException;
import ubb.model.PrgState;
import ubb.model.types.IType;
import ubb.model.utils.MyIDictionary;

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
