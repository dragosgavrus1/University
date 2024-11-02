package ubb.model.types;

public class IntValue implements IValue {
    private final int value;

    public IntValue(int value)
    {
        this.value = value;
    }

    public int getValue()
    {
        return value;
    }

    @Override
    public String toString()
    {
        return Integer.toString(value);
    }

    @Override
    public boolean equals(Object obj) {
        if (! (obj instanceof IntValue objValue))
            return false;

        return this.getValue() == objValue.getValue();
    }

    @Override
    public IType getType() {
        return new IntType();
    }
}
