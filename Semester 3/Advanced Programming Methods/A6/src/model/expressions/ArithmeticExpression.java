package model.expressions;

import exceptions.ExpressionEvaluationException;
import exceptions.InterpreterException;
import model.types.IType;
import model.types.IValue;
import model.types.IntType;
import model.types.IntValue;
import model.utils.MyHeap;
import model.utils.MyIDictionary;
import model.utils.MyIHeap;

public class ArithmeticExpression implements IExpression {
    private final IExpression firstExpression, secondExpression;
    private final char operation;

    public ArithmeticExpression(char operation, IExpression firstExpression, IExpression secondExpression)
    {
        this.firstExpression = firstExpression;
        this.secondExpression = secondExpression;
        this.operation = operation;
    }

    @Override
    public IValue evaluate(MyIDictionary<String, IValue> symbolTable, MyIHeap heap) throws ExpressionEvaluationException {
        IValue firstValue, secondValue;
        firstValue = firstExpression.evaluate(symbolTable, heap);
        secondValue = secondExpression.evaluate(symbolTable, heap);

        if (!firstValue.getType().equals(new IntType()))
            throw new ExpressionEvaluationException("First operand is not integer!");

        if (!secondValue.getType().equals(new IntType()))
            throw new ExpressionEvaluationException("Second operand is not integer!");

        IntValue firstOperand = (IntValue) firstValue;
        IntValue secondOperand = (IntValue) secondValue;

        int firstNumber = firstOperand.getValue();
        int secondNumber = secondOperand.getValue();

        switch (operation)
        {
            case '+':
                return new IntValue(firstNumber + secondNumber);

            case '-':
                return new IntValue(firstNumber - secondNumber);

            case '*':
                return new IntValue(firstNumber * secondNumber);

            case '/':
                if (secondNumber == 0)
                    throw new ExpressionEvaluationException("Division by 0!");

                return new IntValue(firstNumber / secondNumber);
        }

        return null;
    }

    @Override
    public IType typeCheck(MyIDictionary<String, IType> typeEnvironment) throws InterpreterException {
        IType firstExpressionType = firstExpression.typeCheck(typeEnvironment);
        IType secondExpressionType = secondExpression.typeCheck(typeEnvironment);

        if(!firstExpressionType.equals(new IntType()))
            throw new InterpreterException("First operand is not an integer!");

        if(!secondExpressionType.equals(new IntType()))
            throw new InterpreterException("Second operand is not an integer!");

        return new IntType();
    }

    @Override
    public String toString() {

        return switch (operation) {
            case '+' -> "(" + firstExpression.toString() + "+" + secondExpression.toString() + ")";
            case '-' -> "(" + firstExpression.toString() + "-" + secondExpression.toString() + ")";
            case '*' -> "(" + firstExpression.toString() + "*" + secondExpression.toString() + ")";
            case '/' -> "(" + firstExpression.toString() + "/" + secondExpression.toString() + ")";
            default -> "";
        };
    }
}
