package repository;

import model.PrgState;

import java.io.IOException;
import java.io.PrintWriter;

public interface IRepository {
    void addProgram(PrgState programToAdd);
    PrgState getCurrentProgram();
    void logProgramState() throws IOException;

}
