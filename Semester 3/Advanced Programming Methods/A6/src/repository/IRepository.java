package repository;

import model.PrgState;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;

public interface IRepository {
    void addProgram(PrgState programToAdd);
    void logProgramState(PrgState program);
    List<PrgState> getProgramList();
    void setProgramList(List<PrgState> programList);

}
