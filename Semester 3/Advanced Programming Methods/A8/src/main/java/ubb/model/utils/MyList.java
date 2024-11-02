package ubb.model.utils;

import ubb.exceptions.ListException;

import java.util.ArrayList;
import java.util.List;

public class MyList<T> implements MyIList<T> {
    private final List<T> itemsList;

    public MyList()
    {
        itemsList = new ArrayList<T>();
    }

    @Override
    public void add(T itemToAdd) {
        itemsList.add(itemToAdd);
    }

    @Override
    public void remove(int position) throws ListException {
        if (position >= itemsList.size())
            throw new ListException("Index out of bound!");

        itemsList.remove(position);
    }

    @Override
    public boolean remove(T itemToRemove) {
        return itemsList.remove(itemToRemove);
    }

    @Override
    public T get(int position) throws ListException {
        if (position >= itemsList.size())
            throw new ListException("Index out of bound!");

        return itemsList.get(position);
    }

    @Override
    public void set(int position, T newValue) throws ListException {
        if (position >= itemsList.size())
            throw new ListException("Index out of bound!");

        itemsList.set(position, newValue);
    }

    @Override
    public List<T> getOutput() {
        return this.itemsList;
    }

    @Override
    public String toString() {
        return "MyList{" +
                "itemsList=" + itemsList +
                '}';
    }
}
