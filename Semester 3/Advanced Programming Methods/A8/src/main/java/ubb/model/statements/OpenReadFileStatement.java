package ubb.model.statements;

import ubb.exceptions.ExpressionEvaluationException;
import ubb.exceptions.InterpreterException;
import ubb.model.PrgState;
import ubb.model.expressions.IExpression;
import ubb.model.types.IType;
import ubb.model.types.IValue;
import ubb.model.types.StringType;
import ubb.model.types.StringValue;
import ubb.model.utils.MyIDictionary;

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

        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        if(!fileNameExpression.typeCheck(typeEnvironment).equals(new StringType()))
            throw new InterpreterException("File name is not of type String!");

        return typeEnvironment;
    }

    @Override
    public String toString() {
        return "OpenReadFile(" + fileNameExpression + ")";
    }
}
