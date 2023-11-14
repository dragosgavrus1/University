import controller.Controller;
import repository.Repository;
import view.View;

public class Main {
    public static void main(String[] args)
    {
        Repository repo = new Repository();
        Controller ctrl = new Controller(repo);
        View view = new View(ctrl);

        view.mainMenu();
    }
}
