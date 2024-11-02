package ubb.model.statements;

import ubb.exceptions.ExpressionEvaluationException;
import ubb.exceptions.InterpreterException;
import ubb.model.PrgState;
import ubb.model.expressions.IExpression;
import ubb.model.types.IType;
import ubb.model.types.IValue;
import ubb.model.utils.MyIDictionary;

public class AssignStatement implements IStatement {
    private final String variableId;
    private final IExpression expressionToAssign;

    public AssignStatement(String variableId, IExpression expressionToAssign)
    {
        this.variableId = variableId;
        this.expressionToAssign = expressionToAssign;
    }

    @Override
    public PrgState execute(PrgState currentState) throws ExpressionEvaluationException {
        MyIDictionary<String, IValue> symbolTable = currentState.getSymbolTable();

        if (!symbolTable.isDefined(variableId))
            throw new ExpressionEvaluationException("Variable " + variableId + " is not defined!");

        IValue valueToAssign = expressionToAssign.evaluate(symbolTable, currentState.getHeap());

        IValue variableValue = symbolTable.get(variableId);

        if (!valueToAssign.getType().equals(variableValue.getType()))
            throw new ExpressionEvaluationException("Type of variable do not match type of expression!");

        symbolTable.update(variableId, valueToAssign);

        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        IType expressionType = expressionToAssign.typeCheck(typeEnvironment);

        if(!typeEnvironment.isDefined(variableId))
            throw new InterpreterException("Variable " + variableId + " is not defined!");

        IType variableType = typeEnvironment.get(variableId);

        if(!variableType.equals(expressionType))
            throw new InterpreterException("Type of variable " + variableId + " and type of expression " + expressionToAssign.toString() + " do not match!");

        return typeEnvironment;
    }

    @Override
    public String toString() {
        return variableId + "=" + expressionToAssign ;
    }
}
