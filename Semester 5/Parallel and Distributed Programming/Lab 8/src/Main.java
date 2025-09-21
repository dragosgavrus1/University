import mpi.*;

public class Main {

    public static void main(final String[] args) throws InterruptedException {
        /* Set up */
        MPI.Init(args);
        final DSM dsm = new DSM();
        /* Local process index */
        if (MPI.COMM_WORLD.Rank() == 0) {
            master(dsm);
        } else {
            worker(dsm);
        }
        /* Tear down */
        MPI.Finalize();
    }

    private static void master(final DSM dsm) throws InterruptedException {
        final Thread thread = new Thread(new Listener(dsm));
        thread.start();

        dsm.subscribe("a");
        dsm.subscribe("b");
        dsm.subscribe("c");

        Thread.sleep(1000);

        dsm.compareAndExchange("a", 0, 33);

        Thread.sleep(1000);

        dsm.compareAndExchange("c", 1, 15);

        Thread.sleep(1000);

        dsm.updateVariable("b", 50);

        Thread.sleep(2000);

        dsm.close();
        thread.join();
    }

    private static void worker(final DSM dsm) throws InterruptedException {
        int me = MPI.COMM_WORLD.Rank();
        final Thread thread = new Thread(new Listener(dsm));
        thread.start();
        if (me == 1) {

            Thread.sleep(1000);

            dsm.subscribe("a");
            dsm.subscribe("c");

            Thread.sleep(1000);

            dsm.compareAndExchange("a", 33, 420);
            dsm.compareAndExchange("c", 15, 32);

        } else {

            Thread.sleep(2000);

            dsm.subscribe("b");

            Thread.sleep(2000);

            dsm.compareAndExchange("b", 50, 100);

            Thread.sleep(1000);

        }
        thread.join();
    }

    private static class Listener implements Runnable {

        private final DSM dsm;

        public Listener(final DSM dsm) {
            this.dsm = dsm;
        }

        @Override
        public void run() {
            final int me = MPI.COMM_WORLD.Rank();
            System.out.printf("%s - Started.%n", me);

            while (true) {
                final Object[] messageBuffer = new Object[1];

                MPI.COMM_WORLD.Recv(messageBuffer, 0, 1, MPI.OBJECT, MPI.ANY_SOURCE, MPI.ANY_TAG);
                final DSM.Message message = (DSM.Message) messageBuffer[0];
                final DSM.Message.Type messageType = (DSM.Message.Type) message.getField(DSM.Message.Fields.TYPE);

                if (messageType.equals(DSM.Message.Type.QUIT)) {
                    System.out.printf("%s - Received QUIT message.%n", me);
                    System.out.printf("%s - Final DSM state: %s.%n", me, dsm);
                    return;
                } else if (messageType.equals(DSM.Message.Type.SUBSCRIBE)) {
                    System.out.printf("%s - Received SUBSCRIBE message (%s -> %s).%n", me, message.getField(DSM.Message.Fields.RANK), message.getField(DSM.Message.Fields.VARIABLE));
                    dsm.syncSubscription((String) message.getField(DSM.Message.Fields.VARIABLE), (int) message.getField(DSM.Message.Fields.RANK));
                } else if (messageType.equals(DSM.Message.Type.UPDATE)) {
                    System.out.printf("%s - Received UPDATE message (%s -> %s).%n", me, message.getField(DSM.Message.Fields.VARIABLE), message.getField(DSM.Message.Fields.VALUE));
                    dsm.setVariable((String) message.getField(DSM.Message.Fields.VARIABLE), message.getField(DSM.Message.Fields.VALUE));
                }
            }
        }
    }

}