package model.statements;

import model.PrgState;

public class NOPStatement implements IStatement {
    @Override
    public PrgState execute(PrgState currentState) {
        return currentState;
    }

    @Override
    public String toString() {
        return "NOP";
    }
}
