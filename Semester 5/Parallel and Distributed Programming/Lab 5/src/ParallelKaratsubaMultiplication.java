import java.util.Arrays;
import java.util.concurrent.RecursiveTask;
import java.util.concurrent.ForkJoinPool;

public class ParallelKaratsubaMultiplication {

    public static int[] karatsubaParallel(int[] poly1, int[] poly2) {
        ForkJoinPool pool = new ForkJoinPool();
        return pool.invoke(new KaratsubaTask(poly1, poly2));
    }

    private static class KaratsubaTask extends RecursiveTask<int[]> {
        private final int[] poly1, poly2;

        public KaratsubaTask(int[] poly1, int[] poly2) {
            this.poly1 = poly1;
            this.poly2 = poly2;
        }

        @Override
        protected int[] compute() {
            int n = poly1.length;

            // Base case
            if (n == 1) {
                return new int[] { poly1[0] * poly2[0] };
            }

            // Split the polynomials into two halves
            int half = n / 2;
            int[] low1 = Arrays.copyOfRange(poly1, 0, half);
            int[] high1 = Arrays.copyOfRange(poly1, half, n);
            int[] low2 = Arrays.copyOfRange(poly2, 0, half);
            int[] high2 = Arrays.copyOfRange(poly2, half, n);

            // Create tasks for z0 and z2
            KaratsubaTask taskZ0 = new KaratsubaTask(low1, low2);
            KaratsubaTask taskZ2 = new KaratsubaTask(high1, high2);

            // Fork the tasks
            taskZ0.fork();
            taskZ2.fork();

            // Compute z1 (sums of halves) in the current thread
            int[] z1 = new KaratsubaTask(add(low1, high1), add(low2, high2)).compute();

            // Join the results of z0 and z2
            int[] z0 = taskZ0.join();
            int[] z2 = taskZ2.join();

            // Subtract z0 and z2 from z1
            z1 = subtract(z1, add(z0, z2));

            // Combine results
            return combine(z0, z1, z2, half);
        }
    }

    // Helper Methods
    private static int[] add(int[] poly1, int[] poly2) {
        int maxLength = Math.max(poly1.length, poly2.length);
        int[] result = new int[maxLength];
        for (int i = 0; i < poly1.length; i++) result[i] += poly1[i];
        for (int i = 0; i < poly2.length; i++) result[i] += poly2[i];
        return result;
    }

    private static int[] subtract(int[] poly1, int[] poly2) {
        int maxLength = Math.max(poly1.length, poly2.length);
        int[] result = new int[maxLength];
        for (int i = 0; i < poly1.length; i++) result[i] += poly1[i];
        for (int i = 0; i < poly2.length; i++) result[i] -= poly2[i];
        return result;
    }

    private static int[] combine(int[] z0, int[] z1, int[] z2, int half) {
        int resultSize = z0.length + z2.length + half;
        int[] result = new int[resultSize];

        // Add z0
        for (int i = 0; i < z0.length; i++) {
            result[i] += z0[i];
        }

        // Add z1
        for (int i = 0; i < z1.length; i++) {
            result[i + half] += z1[i];
        }

        // Add z2
        for (int i = 0; i < z2.length; i++) {
            result[i + 2 * half] += z2[i];
        }

        return result;
    }
}
