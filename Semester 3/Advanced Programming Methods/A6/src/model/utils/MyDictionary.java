package model.utils;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MyDictionary<TKey, TValue> implements MyIDictionary<TKey, TValue> {
    private final Map<TKey, TValue> dictionary;
    public MyDictionary()
    {
        dictionary = new HashMap<TKey, TValue>();
    }
    @Override
    public TValue get(TKey keyToSearch) {
        return dictionary.get(keyToSearch);
    }
    @Override
    public void put(TKey keyToAdd, TValue valueToAdd) {
        dictionary.put(keyToAdd, valueToAdd);
    }
    @Override
    public void update(TKey keyToUpdate, TValue newValue) {
        dictionary.put(keyToUpdate, newValue);
    }
    @Override
    public Set<TKey> getKeySet() {
        return this.dictionary.keySet();
    }
    @Override
    public boolean isDefined(TKey keyToSearch) {
        return dictionary.containsKey(keyToSearch);
    }
    @Override
    public void remove(TKey keyToRemove) {
        this.dictionary.remove(keyToRemove);
    }

    @Override
    public Map<TKey, TValue> getContent() {
        return this.dictionary;
    }

    @Override
    public String toString() {
        return "MyDictionary{" +
                "dictionary=" + dictionary +
                '}';
    }

    @Override
    public MyIDictionary<TKey, TValue> copy() {
        MyIDictionary<TKey, TValue> dictionaryCopy = new MyDictionary<>();

        for (TKey key : this.getKeySet())
            dictionaryCopy.put(key, this.get(key));

        return dictionaryCopy;
    }


}
