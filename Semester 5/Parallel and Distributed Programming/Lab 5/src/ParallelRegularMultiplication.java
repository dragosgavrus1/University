import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ParallelRegularMultiplication {
    public static int[] multiplyParallel(int[] poly1, int[] poly2) throws InterruptedException {
        int n1 = poly1.length;
        int n2 = poly2.length;
        int[] result = new int[n1 + n2 - 1];
        ExecutorService executor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());

        for (int i = 0; i < n1; i++) {
            int finalI = i;
            executor.execute(() -> {
                for (int j = 0; j < n2; j++) {
                    synchronized (result) {
                        result[finalI + j] += poly1[finalI] * poly2[j];
                    }
                }
            });
        }
        executor.shutdown();
        while (!executor.isTerminated()) {
            Thread.sleep(10);
        }
        return result;
    }
}
