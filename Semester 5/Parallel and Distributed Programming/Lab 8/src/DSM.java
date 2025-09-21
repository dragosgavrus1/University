import mpi.MPI;

import java.io.Serializable;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;

public class DSM {

    private final Map<String, Set<Integer>> subscribers;

    private final Map<String, Object> variables;

    public DSM() {
        variables = new ConcurrentHashMap<>();
        variables.put("a", 0);
        variables.put("b", 0);
        variables.put("c", 0);

        subscribers = new ConcurrentHashMap<>();
        subscribers.put("a", new HashSet<>());
        subscribers.put("b", new HashSet<>());
        subscribers.put("c", new HashSet<>());
    }

    public synchronized void updateVariable(final String variable, final Object value) {
        setVariable(variable, value);

        final Message message = new Message(Message.Type.UPDATE);
        message.setField(Message.Fields.VARIABLE, variable);
        message.setField(Message.Fields.VALUE, value);

        sendToSubscribers(variable, message);
    }

    public synchronized void setVariable(final String variable, final Object value) {
        if (variables.containsKey(variable)) {
            variables.put(variable, value);
        }
    }

    public synchronized void compareAndExchange(final String variable, final Object oldValue, final Object newValue) {
        if (oldValue.equals(variables.get(variable))) {
            updateVariable(variable, newValue);
        }
    }

    public void subscribe(final String variable) {
        subscribers.get(variable).add(MPI.COMM_WORLD.Rank());

        final Message message = new Message(Message.Type.SUBSCRIBE);
        message.setField(Message.Fields.VARIABLE, variable);
        message.setField(Message.Fields.RANK, MPI.COMM_WORLD.Rank());

        sendAll(message);
    }

    public void syncSubscription(final String variable, final int rank) {
        subscribers.get(variable).add(rank);
    }

    public void sendToSubscribers(final String variable, final Message message) {
        for (int i = 0; i < MPI.COMM_WORLD.Size(); i++) {
            if (MPI.COMM_WORLD.Rank() == i || !subscribers.get(variable).contains(i)) {
                continue;
            }

            MPI.COMM_WORLD.Send(new Object[]{message}, 0, 1, MPI.OBJECT, i, 0);
        }
    }

    private void sendAll(final Message message) {
        for (int i = 0; i < MPI.COMM_WORLD.Size(); i++) {
            if (MPI.COMM_WORLD.Rank() == i && !message.getField(Message.Fields.TYPE).equals(Message.Type.QUIT)) {
                continue;
            }

            MPI.COMM_WORLD.Send(new Object[]{message}, 0, 1, MPI.OBJECT, i, 0);
        }
    }

    public void close() {
        sendAll(new Message(Message.Type.QUIT));
    }

    @Override
    public String toString() {
        return "DSM{" +
                "subscribers=" + subscribers +
                ", variables=" + variables +
                '}';
    }

    public static class Message implements Serializable {

        private final Map<String, Object> fields = new HashMap<>();

        public Message(final Type type) {
            setField(Fields.TYPE, type);
        }

        public void setField(final String key, final Object value) {
            fields.put(key, value);
        }

        public Object getField(final String key) {
            return fields.get(key);
        }

        public enum Type {
            SUBSCRIBE, UPDATE, QUIT
        }

        public static class Fields {
            public static final String VARIABLE = "variable";
            public static final String VALUE = "value";
            public static final String RANK = "rank";
            public static final String TYPE = "type";

        }
    }
}