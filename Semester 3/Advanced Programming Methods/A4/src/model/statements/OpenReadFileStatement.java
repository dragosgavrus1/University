package model.statements;

import exceptions.ExpressionEvaluationException;
import exceptions.InterpreterException;
import model.PrgState;
import model.expressions.IExpression;
import model.types.IValue;
import model.types.StringType;
import model.types.StringValue;
import model.utils.MyIDictionary;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class OpenReadFileStatement implements IStatement {
    private final IExpression fileNameExpression;

    public OpenReadFileStatement(IExpression fileNameExpression)
    {
        this.fileNameExpression = fileNameExpression;
    }

    @Override
    public PrgState execute(PrgState currentState) throws ExpressionEvaluationException, InterpreterException {
        MyIDictionary<String, IValue> symbolTable = currentState.getSymbolTable();
        MyIDictionary<String, BufferedReader> fileTable = currentState.getFileTable();

        IValue fileNameValue = fileNameExpression.evaluate(symbolTable, currentState.getHeap());

        if (!fileNameValue.getType().equals(new StringType()))
            throw new ExpressionEvaluationException(fileNameExpression + " does not evaluate to a StringValue");

        StringValue fileName = (StringValue) fileNameValue;

        if (fileTable.isDefined(fileName.getValue()))
            throw new InterpreterException(fileName.getValue() + " is already opened!");

        try {
            BufferedReader openedFile = new BufferedReader(new FileReader(fileName.getValue()));
            fileTable.put(fileName.getValue(), openedFile);
        }

        catch (IOException e)
        {
            throw new InterpreterException("Failed to open file " + fileName.getValue());
        }

        return currentState;
    }

    @Override
    public String toString() {
        return "OpenReadFile(" + fileNameExpression + ")";
    }
}
