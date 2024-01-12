package model.utils;

import java.util.Map;
import java.util.Set;

public interface MyIDictionary<TKey, TValue> {
    TValue get(TKey keyToSearch);
    void put(TKey keyToAdd, TValue valueToAdd);
    void update(TKey keyToUpdate, TValue newValue);
    boolean isDefined(TKey keyToSearch);
    Set<TKey> getKeySet();
    void remove(TKey keyToRemove);
    public Map<TKey, TValue> getContent();
    MyIDictionary<TKey, TValue> copy();
}
