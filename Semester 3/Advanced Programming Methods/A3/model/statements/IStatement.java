package model.statements;

import exceptions.ExpressionEvaluationException;
import exceptions.StatementException;
import model.PrgState;

public interface IStatement {
    PrgState execute(PrgState currentState) throws StatementException, ExpressionEvaluationException;
}
