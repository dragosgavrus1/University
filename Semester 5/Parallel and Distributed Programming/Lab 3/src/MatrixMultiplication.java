import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class MatrixMultiplication {

    public static int[][] generateMatrix(int size) {
        Random rand = new Random();
        int[][] matrix = new int[size][size];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                matrix[i][j] = rand.nextInt(10) + 1;
            }
        }
        return matrix;
    }

    public static int computeElement(int[][] A, int[][] B, int row, int col) {
        int sum = 0;
        for (int i = 0; i < A.length; i++) {
            sum += A[row][i] * B[i][col];
        }
        return sum;
    }

    public static class MatrixTask implements Callable<Void> {
        private final int[][] A, B, C;
        private final List<int[]> taskIndices;

        public MatrixTask(int[][] A, int[][] B, int[][] C, List<int[]> taskIndices) {
            this.A = A;
            this.B = B;
            this.C = C;
            this.taskIndices = taskIndices;
        }

        @Override
        public Void call() {
            for (int[] index : taskIndices) {
                int row = index[0];
                int col = index[1];
                C[row][col] = computeElement(A, B, row, col);
            }
            return null;
        }
    }

    public static List<List<int[]>> rowSplit(int n, int numTasks) {
        int chunkSize = (n * n) / numTasks;
        List<List<int[]>> tasks = new ArrayList<>();
        int count = 0;
        List<int[]> currentTask = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                currentTask.add(new int[]{i, j});
                count++;
                if (count >= chunkSize && tasks.size() < numTasks - 1) {
                    tasks.add(currentTask);
                    currentTask = new ArrayList<>();
                    count = 0;
                }
            }
        }
        tasks.add(currentTask);
        return tasks;
    }

    public static int[][] matrixMultiplicationWithThreads(int[][] A, int[][] B, int size, List<List<int[]>> tasks) throws InterruptedException {
        int[][] C = new int[size][size];
        List<Thread> threads = new ArrayList<>();

        for (List<int[]> taskIndices : tasks) {
            Thread thread = new Thread(() -> {
                for (int[] index : taskIndices) {
                    int row = index[0];
                    int col = index[1];
                    C[row][col] = computeElement(A, B, row, col);
                }
            });
            threads.add(thread);
            thread.start();
        }

        for (Thread thread : threads) {
            thread.join();
        }
        return C;
    }

    public static int[][] matrixMultiplicationWithThreadPool(int[][] A, int[][] B, int size, List<List<int[]>> tasks, int poolSize) throws Exception {
        int[][] C = new int[size][size];
        ExecutorService executor = Executors.newFixedThreadPool(poolSize);
        List<Future<Void>> futures = new ArrayList<>();

        for (List<int[]> taskIndices : tasks) {
            MatrixTask task = new MatrixTask(A, B, C, taskIndices);
            futures.add(executor.submit(task));
        }

        for (Future<Void> future : futures) {
            future.get();
        }
        executor.shutdown();
        return C;
    }

    public static void main(String[] args) throws Exception {
        int size = 100;
        int numTasks = 4;

        int[][] A = generateMatrix(size);
        int[][] B = generateMatrix(size);

        List<List<int[]>> tasks = rowSplit(size, numTasks);

        // Using individual threads
        long startTime = System.currentTimeMillis();
        int[][] resultWithThreads = matrixMultiplicationWithThreads(A, B, size, tasks);
        long endTime = System.currentTimeMillis();
        // System.out.println("Result matrix (individual threads):");
        // System.out.println(java.util.Arrays.deepToString(resultWithThreads));
        System.out.printf("Time taken with individual threads: %d ms%n", (endTime - startTime));

        // Using thread pool
        int poolSize = 4;
        startTime = System.currentTimeMillis();
        int[][] resultWithThreadPool = matrixMultiplicationWithThreadPool(A, B, size, tasks, poolSize);
        endTime = System.currentTimeMillis();
        // System.out.println("Result matrix (thread pool):");
        // System.out.println(java.util.Arrays.deepToString(resultWithThreadPool));
        System.out.printf("Time taken with thread pool (size=%d): %d ms%n", poolSize, (endTime - startTime));
    }
}
