package repository;

import model.PrgState;

import java.util.ArrayList;

public class Repository implements IRepository {
    private final ArrayList<PrgState> programs;

    public Repository()
    {
        programs = new ArrayList<PrgState>();
    }

    @Override
    public void addProgram(PrgState programToAdd) {
        if (!programs.isEmpty())
            programs.set(0, programToAdd);
        else
            programs.add(programToAdd);
    }

    @Override
    public PrgState getCurrentProgram() {
        return programs.get(0);
    }
}
