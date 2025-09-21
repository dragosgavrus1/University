import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.Condition;

public class ScalarProduct {

    private static final int SIZE = 5;
    private int[] vectorA = {1, 2, 3, 4, 5};
    private int[] vectorB = {6, 7, 8, 9, 10};

    private int product = 0;
    private int sum = 0;
    private boolean productAvailable = false;

    private final Lock lock = new ReentrantLock();
    private final Condition condition = lock.newCondition();

    class Producer extends Thread {
        @Override
        public void run() {
            for (int i = 0; i < SIZE; i++) {
                lock.lock();
                try {
                    product = vectorA[i] * vectorB[i];
                    productAvailable = true;

                    condition.signal();

                    while (productAvailable) {
                        condition.await();
                    }
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                } finally {
                    lock.unlock();
                }
            }
        }
    }

    class Consumer extends Thread {
        @Override
        public void run() {
            for (int i = 0; i < SIZE; i++) {
                lock.lock();
                try {
                    while (!productAvailable) {
                        condition.await();
                    }

                    sum += product;
                    productAvailable = false;

                    condition.signal();
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                } finally {
                    lock.unlock();
                }
            }
        }
    }

    public void computeScalarProduct() throws InterruptedException {
        Producer producer = new Producer();
        Consumer consumer = new Consumer();

        producer.start();
        consumer.start();

        producer.join();
        consumer.join();

        System.out.println("Scalar Product: " + sum);
    }

    public static void main(String[] args) throws InterruptedException {
        new ScalarProduct().computeScalarProduct();
    }
}
