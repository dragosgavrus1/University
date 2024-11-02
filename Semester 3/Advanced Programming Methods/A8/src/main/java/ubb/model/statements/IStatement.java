package ubb.model.statements;

import ubb.exceptions.ExpressionEvaluationException;
import ubb.exceptions.InterpreterException;
import ubb.exceptions.StatementException;
import ubb.model.PrgState;
import ubb.model.types.IType;
import ubb.model.utils.MyIDictionary;

public interface IStatement {
    PrgState execute(PrgState currentState) throws StatementException, ExpressionEvaluationException, InterpreterException;
    MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException;
}
