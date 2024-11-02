package ubb.repository;

import ubb.model.PrgState;

import java.util.List;

public interface IRepository {
    void addProgram(PrgState programToAdd);
    void logProgramState(PrgState program);
    List<PrgState> getProgramList();
    void setProgramList(List<PrgState> programList);

}
