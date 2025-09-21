import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

class modifyVariablesTask extends TimerTask {
    @Override
    public void run() {
        int index = ThreadLocalRandom.current().nextInt(0, Main.primaryVariables.size());
        Variable var = Main.primaryVariables.get(index);
        int value = ThreadLocalRandom.current().nextInt(-10, 11);
        var.setValue(value);
    }
}

class runCheckerTask extends TimerTask {
    @Override
    public void run() {
        Checker consistencyChecker = new Checker(Main.variables);
        System.out.println("Running checker...");
        boolean result = consistencyChecker.run();
        System.out.println("Checker result " + result);
    }
}

public class Main {
    public static ArrayList<Variable> primaryVariables = new ArrayList<>();
    public static ArrayList<Variable> variables = new ArrayList<>();


    public static void main(String[] args) {
        createVariables();
        modifyVariables();
        runChecker();

        Timer cancelTimer = new Timer();
        cancelTimer.schedule(new TimerTask() {
            @Override
            public void run() {
                System.out.println("Cancelling timers after 2 seconds...");
                Main.stopTimers();
                cancelTimer.cancel();
            }
        }, 2000);
    }

    private static List<Timer> timers = new ArrayList<>();

    private static void modifyVariables() {
        for (int i = 0; i < 10; ++i) {
            Timer timer = new Timer();
            timers.add(timer);
            timer.schedule(new modifyVariablesTask(), 0, 100);
        }
    }

    private static void runChecker() {
        Timer timer = new Timer();
        timers.add(timer);
        timer.schedule(new runCheckerTask(), 300, 100);
    }

    public static void stopTimers() {
        for (Timer timer : timers) {
            timer.cancel();
        }
    }

    private static void createVariables() {
        Variable primary1 = new Variable(2);
        Variable primary2 = new Variable(3);
        Variable primary3 = new Variable(1);

        variables.add(primary1);
        variables.add(primary2);
        variables.add(primary3);
        primaryVariables.add(primary1);
        primaryVariables.add(primary2);
        primaryVariables.add(primary3);

        Variable secondSecondary1 = new Variable();
        Variable secondSecondary2 = new Variable();

        variables.add(secondSecondary1);
        variables.add(secondSecondary2);

        primary1.addDependent(secondSecondary1);
        primary2.addDependent(secondSecondary1);
        primary2.addDependent(secondSecondary2);
        primary3.addDependent(secondSecondary2);

        for (Variable var : variables) {
            System.out.println("Variable with value: " + var.getValue());
        }
    }

}