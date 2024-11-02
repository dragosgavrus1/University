package ubb.model.types;

public class RefValue implements IValue{
    private  int address;
    private final IType locationType;

    public RefValue(int address, IType locationType) {
        this.address = address;
        this.locationType = locationType;
    }

    public int getAddress() {
        return address;
    }

    public void setAddress(int address) {
        this.address = address;
    }

    public IType getLocationType() {
        return locationType;
    }

    @Override
    public IType getType() {
        return new RefType(locationType);
    }

    @Override
    public boolean equals(Object other) {
        if (other instanceof RefValue)
            return address == ((RefValue) other).getAddress() && locationType.equals(((RefValue) other).getLocationType());
        return false;
    }

    @Override
    public String toString() {
        return "(" + address + ", " + locationType.toString() + ")";
    }

}
