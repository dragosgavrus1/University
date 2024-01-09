package model.utils;

import model.types.IValue;

import java.util.HashMap;
import java.util.Map;

public class MyHeap implements MyIHeap{
    private Map<Integer, IValue> heap;
    private int freeAddress;

    public MyHeap() {
        heap = new HashMap<>();
        freeAddress = 0;
    }

    @Override
    public int allocate(IValue value) {
        freeAddress++;
        heap.put(freeAddress, value);
        return freeAddress;
    }

    @Override
    public int getCurrentAddress() {
        return freeAddress;
    }

    @Override
    public void deallocate(Integer address) {
        heap.remove(address);
    }

    @Override
    public IValue read(Integer address) {
        return heap.get(address);
    }

    @Override
    public void write(Integer address, IValue value) {
        heap.put(address, value);
    }

    @Override
    public boolean isDefined(Integer address) {
        return heap.containsKey(address);
    }

    @Override
    public void update(Integer address, IValue value) {
        heap.put(address, value);
    }

    @Override
    public String toString() {
        return "MyHeap{" +
                "heap=" + heap + '}';
    }

    @Override
    public void setContent(Map<Integer, IValue> newContent) {
        heap.clear();
        for (Integer address : newContent.keySet()) {
            heap.put(address, newContent.get(address));
        }
    }

    @Override
    public Map<Integer, IValue> getContent() {
        return heap;
    }
}
