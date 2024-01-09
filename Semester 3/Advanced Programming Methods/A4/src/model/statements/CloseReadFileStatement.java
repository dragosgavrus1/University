package model.statements;

import exceptions.ExpressionEvaluationException;
import exceptions.InterpreterException;
import exceptions.StatementException;
import model.PrgState;
import model.expressions.IExpression;
import model.types.IValue;
import model.types.StringType;
import model.types.StringValue;
import model.utils.MyIDictionary;

import java.io.BufferedReader;
import java.io.IOException;


public class CloseReadFileStatement implements IStatement {
    private final IExpression fileNameExpression;

    public CloseReadFileStatement(IExpression fileNameExpression)
    {
        this.fileNameExpression = fileNameExpression;
    }

    @Override
    public PrgState execute(PrgState currentState) throws StatementException, ExpressionEvaluationException, InterpreterException {
        MyIDictionary<String, IValue> symbolTable = currentState.getSymbolTable();
        MyIDictionary<String, BufferedReader> fileTable = currentState.getFileTable();

        IValue fileNameValue = fileNameExpression.evaluate(symbolTable, currentState.getHeap());

        if (!fileNameValue.getType().equals(new StringType()))
            throw new ExpressionEvaluationException(fileNameExpression + " does not evaluate to a StringType!");

        StringValue fileName = (StringValue) fileNameValue;

        if (!fileTable.isDefined(fileName.getValue()))
            throw new InterpreterException(String.format("File %s is not opened!", fileName));

        BufferedReader fileToClose = fileTable.get(fileName.getValue());

        try {
            fileToClose.close();
            fileTable.remove(fileName.getValue());
        }

        catch (IOException e)
        {
            throw new InterpreterException(String.format("Failed to close file %s!", fileName.getValue()));
        }
        return null;
    }

    @Override
    public String toString() {
        return String.format("CloseFile(%s)", this.fileNameExpression);
    }
}
