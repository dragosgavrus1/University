package model.statements;

import exceptions.ExpressionEvaluationException;
import exceptions.InterpreterException;
import exceptions.StatementException;
import model.PrgState;
import model.expressions.IExpression;
import model.types.IType;
import model.types.IValue;
import model.types.RefType;
import model.types.RefValue;
import model.utils.MyIDictionary;
import model.utils.MyIHeap;

public class WriteHeapStatement implements IStatement {
    private final String variableName;
    private final IExpression expression;
    public WriteHeapStatement(String variableName, IExpression expression) {
        this.variableName = variableName;
        this.expression = expression;
    }


    @Override
    public PrgState execute(PrgState currentState) throws StatementException, ExpressionEvaluationException, InterpreterException {
        MyIDictionary<String, IValue> symbolTable = currentState.getSymbolTable();
        MyIHeap heap = currentState.getHeap();

        RefValue variableToWrite = (RefValue) symbolTable.get(variableName);

        if(!symbolTable.isDefined(variableName))
            throw new StatementException("Variable " + variableName + " is not defined!");
        else if(!(symbolTable.get(variableName).getType() instanceof RefType))
            throw new StatementException("Variable " + variableName + " is not of type RefType!");
        else if(!currentState.getHeap().isDefined(variableToWrite.getAddress()))
            throw new StatementException("Address " + variableToWrite.getAddress() + " is not defined in the heap!");
        else {
            IValue newValue = expression.evaluate(symbolTable, currentState.getHeap());
            RefType variableType = (RefType) variableToWrite.getType();
            if(!newValue.getType().equals(variableType.getInner()))
                throw new StatementException("Type of variable " + variableName + " and type of expression " + expression.toString() + " do not match!");
            heap.update(variableToWrite.getAddress(), newValue);
        }
        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        if(!typeEnvironment.get(variableName).equals(new RefType(expression.typeCheck(typeEnvironment))))
            throw new InterpreterException("Variable " + variableName + " is not of type RefType!");

        return typeEnvironment;
    }

    @Override
    public String toString() {
        return "WriteHeap(" + variableName + ", " + expression + ")";
    }
}
