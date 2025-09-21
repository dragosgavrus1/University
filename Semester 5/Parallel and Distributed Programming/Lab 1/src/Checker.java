import java.util.ArrayList;
import java.util.concurrent.atomic.AtomicBoolean;

public class Checker {
    private final ArrayList<Variable> variables;

    public Checker(ArrayList<Variable> variables) {
        this.variables = variables;
    }

    public boolean run() {
        lockVariables();
        boolean isValid = checkVariables();
        unlockVariables();
        return isValid;
    }

    public void lockVariables() {
        this.variables.forEach(variable -> {
            variable.mutex.lock();
            lockDependent(variable);
        });
    }

    public void unlockVariables() {
        this.variables.forEach(variable -> {
            variable.mutex.unlock();
            unlockDependent(variable);
        });
    }

    public void lockDependent(Variable variable) {
        variable.getDependents().forEach(secondary -> {
            secondary.mutex.lock();
            lockDependent(secondary);
        });
    }

    public void unlockDependent(Variable variable) {
        variable.getDependents().forEach(secondary -> {
            secondary.mutex.unlock();
            unlockDependent(secondary);
        });
    }

    public boolean checkVariables() {
        AtomicBoolean isValid = new AtomicBoolean(true);

        variables.forEach(variable -> {
            System.out.println("Variable with value: " + variable.getValue());
            if(check(variable))
                isValid.set(false);
        });

        return isValid.get();
    }

    public boolean check(Variable variable) {
        boolean isValid = true;

        if (!variable.getInputs().isEmpty()) {
            int sumValue = variable.getInputs().stream().mapToInt(Variable::getValue).sum();
            if (sumValue != variable.getValue()) {
                isValid = false;
            }
        }

        for (Variable dependent : variable.getDependents()) {
            if (check(dependent)) {
                isValid = false;
            }
        }

        return !isValid;
    }
}