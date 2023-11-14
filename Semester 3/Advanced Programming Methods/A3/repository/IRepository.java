package repository;

import model.PrgState;

public interface IRepository {
    void addProgram(PrgState programToAdd);
    PrgState getCurrentProgram();
}
