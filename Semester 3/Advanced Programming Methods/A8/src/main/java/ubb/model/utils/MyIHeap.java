package ubb.model.utils;

import ubb.model.types.IValue;

import java.util.Map;

public interface MyIHeap{
    int allocate(IValue value);
    int getCurrentAddress();
    void deallocate(Integer address);
    IValue read(Integer address);
    void write(Integer address, IValue value);
    boolean isDefined(Integer address);
    void update(Integer address, IValue value);
    String toString();
    void setContent(Map<Integer, IValue> newContent);
    Map<Integer, IValue> getContent();
}
