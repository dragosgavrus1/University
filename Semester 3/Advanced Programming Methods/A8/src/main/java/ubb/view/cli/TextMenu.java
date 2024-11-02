package ubb.view.cli;

import ubb.model.utils.MyDictionary;
import ubb.model.utils.MyIDictionary;

import java.util.Scanner;

public class TextMenu {
    private final MyIDictionary<String, Command> commands;

    public TextMenu()
    {
        commands = new MyDictionary<>();
    }

    public void addCommand(Command commandToAdd)
    {
        commands.put(commandToAdd.getKey(), commandToAdd);
    }

    private void printMenu()
    {
        for (String commandKey : commands.getKeySet())
            System.out.println(commandKey + ". " + commands.get(commandKey).getDescription());
    }

    public void show()
    {
        Scanner consoleReader = new Scanner(System.in);

        while (true)
        {
            this.printMenu();

            System.out.print("Choose an option: ");
            String option = consoleReader.nextLine();
            Command command = commands.get(option);
            if (command == null)
            {
                System.out.println("Invalid option!");
                continue;
            }

            command.execute();
        }
    }
}
