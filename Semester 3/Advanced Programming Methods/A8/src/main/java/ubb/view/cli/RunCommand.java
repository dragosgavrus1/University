package ubb.view.cli;

import ubb.controller.Controller;
import ubb.exceptions.ExpressionEvaluationException;
import ubb.exceptions.InterpreterException;
import ubb.exceptions.StatementException;

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