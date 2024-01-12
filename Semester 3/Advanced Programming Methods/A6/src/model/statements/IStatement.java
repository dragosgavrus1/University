package model.statements;

import exceptions.ExpressionEvaluationException;
import exceptions.InterpreterException;
import exceptions.StatementException;
import model.PrgState;
import model.types.IType;
import model.utils.MyIDictionary;

public interface IStatement {
    PrgState execute(PrgState currentState) throws StatementException, ExpressionEvaluationException, InterpreterException;
    MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException;
}
