package view;

import controller.Controller;
import repository.IRepository;
import repository.Repository;
import model.PrgState;
import model.statements.IStatement;
import model.statements.*;
import model.types.*;
import model.expressions.*;

import java.util.Scanner;

public class View {
    private final Scanner consoleScanner;
    private boolean displayFlag;

    public static IStatement createExample1() {
        IStatement example1 = new CompoundStatement(
                new VariableDeclarationStatement("v", new BoolType()),
                new CompoundStatement(
                        new AssignStatement("v", new ValueExpression(new BoolValue(true))),
                        new CompoundStatement(
                                new VariableDeclarationStatement("a", new IntType()),
                                new NOPStatement()))
        );
        return example1;
    }

    public static IStatement createExample2()
    {
        IStatement example2 = new CompoundStatement(
                new VariableDeclarationStatement("a", new IntType()),
                new CompoundStatement(
                        new VariableDeclarationStatement("b", new IntType()),
                        new CompoundStatement(
                                new AssignStatement("a",
                                        new ArithmeticExpression('+',
                                                new ValueExpression(new IntValue(2)),
                                                new ArithmeticExpression('*',
                                                        new ValueExpression(new IntValue(3)),
                                                        new ValueExpression(new IntValue(5))))),
                                new CompoundStatement(
                                        new AssignStatement("b",
                                                new ArithmeticExpression('+',
                                                        new VariableExpression("a"),
                                                        new ValueExpression(new IntValue(1)))),
                                        new PrintStatement(new VariableExpression("b"))
                                )
                        )
                )
        );

        return example2;
    }

    public static IStatement createExample3()
    {
        IStatement example3 = new CompoundStatement(
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

        return example3;
    }

    public static IStatement createExample4() {
        IStatement example4 = new CompoundStatement(
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
        return example4;
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

    public View()
    {
        consoleScanner = new Scanner(System.in);
    }

    public void mainMenu()
    {
        String option;
        TextMenu menu = new TextMenu();
        menu.addCommand(new ExitCommand("0", "exit"));

        IStatement currentStatement1 = createExample1();
        PrgState currentProgram = new PrgState(currentStatement1);
        IRepository repository1 = new Repository("log1.txt");
        Controller controller1 = new Controller(repository1);
        controller1.addProgram(currentProgram);
        menu.addCommand(new RunCommand("1", currentStatement1.toString(), controller1));

        IStatement currentStatement2 = createExample2();
        PrgState currentProgram2 = new PrgState(currentStatement2);
        IRepository repository2 = new Repository("log2.txt");
        Controller controller2 = new Controller(repository2);
        controller2.addProgram(currentProgram2);
        menu.addCommand(new RunCommand("2", currentStatement2.toString(), controller2));

        IStatement currentStatement3 = createExample3();
        PrgState currentProgram3 = new PrgState(currentStatement3);
        IRepository repository3 = new Repository("log3.txt");
        Controller controller3 = new Controller(repository3);
        controller3.addProgram(currentProgram3);
        menu.addCommand(new RunCommand("3", currentStatement3.toString(), controller3));

        IStatement currentStatement4 = createExample4();
        PrgState currentProgram4 = new PrgState(currentStatement4);
        IRepository repository4 = new Repository("log4.txt");
        Controller controller4 = new Controller(repository4);
        controller4.addProgram(currentProgram4);
        menu.addCommand(new RunCommand("4", currentStatement4.toString(), controller4));

        IStatement currentStatement5 = createExample5();
        PrgState currentProgram5 = new PrgState(currentStatement5);
        IRepository repository5 = new Repository("log5.txt");
        Controller controller5 = new Controller(repository5);
        controller5.addProgram(currentProgram5);
        menu.addCommand(new RunCommand("5", currentStatement5.toString(), controller5));

        IStatement currentStatement6 = createExample6();
        PrgState currentProgram6 = new PrgState(currentStatement6);
        IRepository repository6 = new Repository("log6.txt");
        Controller controller6 = new Controller(repository6);
        controller6.addProgram(currentProgram6);
        menu.addCommand(new RunCommand("6", currentStatement6.toString(), controller6));

        IStatement currentStatement7 = createExample7();
        PrgState currentProgram7 = new PrgState(currentStatement7);
        IRepository repository7 = new Repository("log7.txt");
        Controller controller7 = new Controller(repository7);
        controller7.addProgram(currentProgram7);
        menu.addCommand(new RunCommand("7", currentStatement7.toString(), controller7));

        IStatement currentStatement8 = createExample8();
        PrgState currentProgram8 = new PrgState(currentStatement8);
        IRepository repository8 = new Repository("log8.txt");
        Controller controller8 = new Controller(repository8);
        controller8.addProgram(currentProgram8);
        menu.addCommand(new RunCommand("8", currentStatement8.toString(), controller8));

        IStatement currentStatement9 = createExample9();
        PrgState currentProgram9 = new PrgState(currentStatement9);
        IRepository repository9 = new Repository("log9.txt");
        Controller controller9 = new Controller(repository9);
        controller9.addProgram(currentProgram9);
        menu.addCommand(new RunCommand("9", currentStatement9.toString(), controller9));

        menu.show();
    }
}
