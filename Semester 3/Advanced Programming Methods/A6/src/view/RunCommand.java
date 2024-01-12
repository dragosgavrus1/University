package view;

import controller.Controller;
import exceptions.ExpressionEvaluationException;
import exceptions.InterpreterException;
import exceptions.StatementException;

import java.io.IOException;

public class RunCommand extends Command {
    private final Controller controller;

    public RunCommand(String key, String description, Controller interpreterController)
    {
        super(key, description);
        this.controller = interpreterController;
    }

    @Override
    public void execute()
    {
        try
        {
            controller.allSteps();
        }
        catch (IOException | StatementException | ExpressionEvaluationException | InterpreterException | InterruptedException e)
        {
            System.out.println(e.getMessage());
        }
    }
}