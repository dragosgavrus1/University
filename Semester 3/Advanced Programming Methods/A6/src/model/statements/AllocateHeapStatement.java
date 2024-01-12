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

public class AllocateHeapStatement implements IStatement{
    private final String variableName;
    private final IExpression expression;

    public AllocateHeapStatement(String variableName, IExpression expression) {
        this.variableName = variableName;
        this.expression = expression;
    }

    public String getVariableName() {
        return variableName;
    }

    public IExpression getExpression() {
        return expression;
    }

    @Override
    public String toString() {
        return "new(" + variableName + ", " + expression.toString() + ")";
    }

    @Override
    public PrgState execute(PrgState currentState) throws StatementException, ExpressionEvaluationException, InterpreterException {
        MyIDictionary<String, IValue> symbolTable = currentState.getSymbolTable();
        MyIHeap heap = currentState.getHeap();

        if(!currentState.getSymbolTable().isDefined(variableName))
            throw new StatementException("Variable " + variableName + " is not defined!");

        if (!(currentState.getSymbolTable().get(variableName).getType() instanceof RefType)) {
            throw new StatementException("Variable " + variableName + " is not of type RefType!");
        }

        RefValue variableToAllocate = (RefValue) currentState.getSymbolTable().get(variableName);
        IValue expressionValue = expression.evaluate(currentState.getSymbolTable(), currentState.getHeap());
        RefType variableType = (RefType) variableToAllocate.getType();

        if(!expressionValue.getType().equals(variableType.getInner()))
            throw new StatementException("Type of variable " + variableName + " and type of expression " + expression.toString() + " do not match!");

        int address = currentState.getHeap().allocate(expressionValue);
        currentState.getSymbolTable().update(variableName, new RefValue(address, variableType.getInner()));

        return null;
    }

    @Override
    public MyIDictionary<String, IType> typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        IType variableType = typeEnvironment.get(variableName);
        IType expressionType = expression.typeCheck(typeEnvironment);

        if (!variableType.equals(new RefType(expressionType)))
            throw new InterpreterException("Variable " + variableName + " and expression " + expression.toString() + " do not have the same type!");

        return typeEnvironment;
    }
}
