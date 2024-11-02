package ubb.model.statements;

import ubb.exceptions.ExpressionEvaluationException;
import ubb.exceptions.InterpreterException;
import ubb.exceptions.StatementException;
import ubb.model.PrgState;
import ubb.model.expressions.IExpression;
import ubb.model.types.*;
import ubb.model.utils.MyIDictionary;

import java.io.BufferedReader;
import java.io.IOException;

public class ReadFileStatement implements IStatement {
    private final IExpression fileNameExpression;
    private final String variableId;

    public ReadFileStatement(IExpression fileNameExpression, String variableId)
    {
        this.fileNameExpression = fileNameExpression;
        this.variableId = variableId;
    }

    @Override
    public PrgState execute(PrgState currentState) throws StatementException, ExpressionEvaluationException, InterpreterException {
        MyIDictionary<String, IValue> symbolTable = currentState.getSymbolTable();
        MyIDictionary<String, BufferedReader> fileTable = currentState.getFileTable();

        if (!symbolTable.isDefined(variableId))
            throw new ExpressionEvaluationException(String.format("Variable %s is not defined!", variableId));

        IValue variableValue = symbolTable.get(variableId);

        if (!variableValue.getType().equals(new IntType()))
            throw new InterpreterException(String.format("Variable %s does not evaluate to IntType", variableId));

        IValue fileNameValue = fileNameExpression.evaluate(symbolTable, currentState.getHeap());

        if (!fileNameValue.getType().equals(new StringType()))
            throw new InterpreterException(String.format("File %s is not opened!", fileNameValue));

        StringValue fileName = (StringValue) fileNameValue;
        BufferedReader openedFile = fileTable.get(fileName.getValue());

        try {
            String newValue = openedFile.readLine().strip();
            int valueToAssign;

            if (newValue.isEmpty())
            {
                valueToAssign = 0;
            }
            else {
                valueToAssign = Integer.parseInt(newValue);
            }

            symbolTable.update(variableId, new IntValue(valueToAssign));
        }

        catch (IOException e)
        {
            throw new InterpreterException("Failed to read from file " + fileName.getValue());
        }

        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        if(!fileNameExpression.typeCheck(typeEnvironment).equals(new StringType()))
            throw new InterpreterException("File name  is not of type String!");

        if(!typeEnvironment.get(variableId).equals(new IntType()))
            throw new InterpreterException("Variable " + variableId + " is not of type Int!");

        return typeEnvironment;
    }

    @Override
    public String toString() {
        return String.format("ReadFile(%s, %s)", this.fileNameExpression, this.variableId);
    }
}
