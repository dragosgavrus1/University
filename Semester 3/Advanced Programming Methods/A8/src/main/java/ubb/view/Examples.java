package ubb.view;

import ubb.model.expressions.*;
import ubb.model.statements.*;
import ubb.model.types.*;

import java.util.ArrayList;
import java.util.List;

public class Examples {
    public static IStatement createExample1() {
        return new CompoundStatement(
                new VariableDeclarationStatement("v", new BoolType()),
                new CompoundStatement(
                        new AssignStatement("v", new ValueExpression(new IntValue(2))),
                        new CompoundStatement(
                                new VariableDeclarationStatement("a", new IntType()),
                                new NOPStatement()))
        );
    }

    public static IStatement createExample2()
    {
        return new CompoundStatement
                (
                        new VariableDeclarationStatement("a", new IntType()),
                        new CompoundStatement
                                (
                                        new VariableDeclarationStatement("b", new IntType()),
                                        new CompoundStatement
                                                (
                                                        new AssignStatement("a",
                                                                new ArithmeticExpression('+',
                                                                        new ValueExpression(new IntValue(2)),
                                                                        new ArithmeticExpression('*',
                                                                                new ValueExpression(new IntValue(3)),
                                                                                new ValueExpression(new IntValue(5)))
                                                                )
                                                        ),
                                                        new CompoundStatement(
                                                                new AssignStatement("b",
                                                                        new ArithmeticExpression('+',
                                                                                new VariableExpression("a"),
                                                                                new ValueExpression(new IntValue(1))
                                                                        )
                                                                ),
                                                                new PrintStatement(new VariableExpression("b"))
                                                        )
                                                )
                                )
                );
    }

    public static IStatement createExample3()
    {
        return new CompoundStatement(
                new VariableDeclarationStatement("a", new BoolType()),
                new CompoundStatement(
                        new VariableDeclarationStatement("v", new IntType()),
                        new CompoundStatement(
                                new AssignStatement("a", new ValueExpression(new BoolValue(true))),
                                new CompoundStatement(
                                        new IfStatement(
                                                new VariableExpression("a"),
                                                new AssignStatement("v", new ValueExpression(new IntValue(2))),
                                                new AssignStatement("v", new ValueExpression(new IntValue(3)))
                                        ),
                                        new PrintStatement(
                                                new VariableExpression("v")
                                        )
                                )
                        )
                )
        );
    }

    public static IStatement createExample4() {
        return new CompoundStatement(
                new VariableDeclarationStatement("varf", new StringType()),
                new CompoundStatement(
                        new AssignStatement("varf", new ValueExpression(new StringValue("test.in"))),
                        new CompoundStatement(
                                new OpenReadFileStatement(new VariableExpression("varf")),
                                new CompoundStatement(
                                        new VariableDeclarationStatement("varc", new IntType()),
                                        new CompoundStatement(
                                                new ReadFileStatement(new VariableExpression("varf"), "varc"),
                                                new CompoundStatement(
                                                        new PrintStatement(new VariableExpression("varc")),
                                                        new CompoundStatement(
                                                                new ReadFileStatement(new VariableExpression("varf"), "varc"),
                                                                new CompoundStatement(
                                                                        new PrintStatement(new VariableExpression("varc")),
                                                                        new CloseReadFileStatement(new VariableExpression("varf"))
                                                                )
                                                        )
                                                )
                                        )
                                )
                        )
                )
        );
    }

    public static IStatement createExample5() {
        return new CompoundStatement(
                new VariableDeclarationStatement("v", new RefType(new IntType())),
                new CompoundStatement(
                        new AllocateHeapStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(
                                new VariableDeclarationStatement("a", new RefType(new RefType(new IntType()))),
                                new CompoundStatement(
                                        new AllocateHeapStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(
                                                new PrintStatement(new VariableExpression("v")),
                                                new PrintStatement(new VariableExpression("a"))
                                        )
                                )
                        )
                )
        );
    }

    public static IStatement createExample6()
    {
        return new CompoundStatement(
                new VariableDeclarationStatement("v", new RefType(new IntType())),
                new CompoundStatement(
                        new AllocateHeapStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(
                                new VariableDeclarationStatement("a", new RefType(new RefType(new IntType()))),
                                new CompoundStatement(
                                        new AllocateHeapStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(
                                                new PrintStatement(new ReadHeapExpression(new VariableExpression("v"))),
                                                new PrintStatement(new ArithmeticExpression('+',
                                                        new ReadHeapExpression(new ReadHeapExpression(new VariableExpression("a"))),
                                                        new ValueExpression(new IntValue(5))
                                                )
                                                )
                                        )
                                )
                        )
                )
        );
    }

    public static IStatement createExample7()
    {
        return new CompoundStatement(
                new VariableDeclarationStatement("v", new RefType(new IntType())),
                new CompoundStatement(
                        new AllocateHeapStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(
                                new PrintStatement(new ReadHeapExpression(new VariableExpression("v"))),
                                new CompoundStatement(
                                        new WriteHeapStatement("v", new ValueExpression(new IntValue(30))),
                                        new PrintStatement(new ArithmeticExpression(
                                                '+',
                                                new ReadHeapExpression(new VariableExpression("v")),
                                                new ValueExpression(new IntValue(5))
                                        ))
                                )
                        )
                )
        );
    }

    public static IStatement createExample8()
    {
        return new CompoundStatement(
                new VariableDeclarationStatement("v", new RefType(new IntType())),
                new CompoundStatement(
                        new AllocateHeapStatement("v", new ValueExpression(new IntValue(20))),
                        new CompoundStatement(
                                new VariableDeclarationStatement("a", new RefType(new RefType(new IntType()))),
                                new CompoundStatement(
                                        new AllocateHeapStatement("a", new VariableExpression("v")),
                                        new CompoundStatement(
                                                new AllocateHeapStatement("v", new ValueExpression(new IntValue(30))),
                                                new PrintStatement(new ReadHeapExpression(
                                                        new ReadHeapExpression(new VariableExpression("a"))
                                                ))
                                        )
                                )
                        )
                )
        );
    }

    public static IStatement createExample9()
    {
        return new CompoundStatement(
                new VariableDeclarationStatement("v", new IntType() ),
                new CompoundStatement(
                        new AssignStatement("v", new ValueExpression(new IntValue(5))),
                        new CompoundStatement(
                                new WhileStatement(
                                        new RelationalExpression(
                                                new VariableExpression("v"),
                                                new ValueExpression(new IntValue(0)),
                                                ">"
                                        ),
                                        new CompoundStatement(
                                                new PrintStatement(new VariableExpression("v")),
                                                new AssignStatement("v", new ArithmeticExpression(
                                                        '-',
                                                        new VariableExpression("v"),
                                                        new ValueExpression(new IntValue(1))
                                                ))
                                        )
                                ),
                                new PrintStatement(new VariableExpression("v"))
                        )
                )
        );
    }

    public static IStatement createThreadExample()
    {
        IStatement forkStatement = new ForkStatement(new CompoundStatement(
                new WriteHeapStatement("a", new ValueExpression(new IntValue(30))),
                new CompoundStatement(
                        new AssignStatement("v", new ValueExpression(new IntValue(32))),
                        new CompoundStatement(
                                new PrintStatement(new VariableExpression("v")),
                                new PrintStatement(new ReadHeapExpression(new VariableExpression("a")))
                        )
                )
        )
        );

        return new CompoundStatement(
                new VariableDeclarationStatement("v", new IntType()),
                new CompoundStatement(
                        new VariableDeclarationStatement("a", new RefType(new IntType())),
                        new CompoundStatement(
                                new AssignStatement("v", new ValueExpression(new IntValue(10))),
                                new CompoundStatement(
                                        new AllocateHeapStatement("a", new ValueExpression(new IntValue(22))),
                                        new CompoundStatement(
                                                forkStatement,
                                                new CompoundStatement(
                                                        new PrintStatement(new VariableExpression("v")),
                                                        new PrintStatement(new ReadHeapExpression(new VariableExpression("a")))
                                                )
                                        )
                                )
                        )
                )
        );
    }


    public static IStatement createForkExample()
    {
        IStatement innerStatement = new CompoundStatement(
                new ForkStatement(
                        new ForkStatement(
                                new CompoundStatement(
                                        new VariableDeclarationStatement("a", new IntType()),
                                        new CompoundStatement(
                                                new AssignStatement("a", new VariableExpression("counter")),
                                                new PrintStatement(new VariableExpression("a"))
                                        )
                                )
                        )
                ),
                new AssignStatement("counter", new ArithmeticExpression(
                        '+',
                        new VariableExpression("counter"),
                        new ValueExpression(new IntValue(1))
                )
                )
        );

        return new CompoundStatement(
                new VariableDeclarationStatement("counter", new IntType()),
                new WhileStatement(new RelationalExpression(
                        new VariableExpression("counter"),
                        new ValueExpression(new IntValue(10)),
                        "<"
                ),
                        innerStatement
                )
        );
    }

    public static List<IStatement> getAllExamples()
    {
        ArrayList<IStatement> allStatements = new ArrayList<>();

        allStatements.add(createExample1());
        allStatements.add(createExample2());
        allStatements.add(createExample3());
        allStatements.add(createExample4());
        allStatements.add(createExample5());
        allStatements.add(createExample6());
        allStatements.add(createExample7());
        allStatements.add(createExample8());
        allStatements.add(createExample9());
        allStatements.add(createThreadExample());
        allStatements.add(createForkExample());

        return allStatements;
    }
}