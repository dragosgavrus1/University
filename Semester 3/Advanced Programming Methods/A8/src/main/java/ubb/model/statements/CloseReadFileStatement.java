package ubb.model.statements;

import ubb.exceptions.ExpressionEvaluationException;
import ubb.exceptions.InterpreterException;
import ubb.exceptions.StatementException;
import ubb.model.PrgState;
import ubb.model.expressions.IExpression;
import ubb.model.types.IType;
import ubb.model.types.IValue;
import ubb.model.types.StringType;
import ubb.model.types.StringValue;
import ubb.model.utils.MyIDictionary;

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
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        if(!fileNameExpression.typeCheck(typeEnvironment).equals(new StringType()))
            throw new InterpreterException("File name is not of type string!");

        return typeEnvironment;
    }

    @Override
    public String toString() {
        return String.format("CloseFile(%s)", this.fileNameExpression);
    }
}
