import java.io.IOException;
import java.util.List;
import java.util.concurrent.*;
import java.util.stream.Collectors;

public class Main {

    private static final int NR_THREADS = 5;
    private static final int NR_TASKS = 5;

    private static ExecutorService executorService;

    public static void main(String[] args) throws IOException, InterruptedException, ExecutionException {
        Matrix initialState = Matrix.readFromFile();

        executorService = Executors.newFixedThreadPool(NR_THREADS);
        Matrix solution = solve(initialState);
        System.out.println(solution);
        executorService.shutdown();
        executorService.awaitTermination(1000000, TimeUnit.SECONDS);
    }

    public static Matrix solve(Matrix root) throws ExecutionException, InterruptedException {
        long time = System.currentTimeMillis();
        int minimumBound = root.manhattan;
        int distance;
        while (true) {
            Pair<Integer, Matrix> solution = searchParallel(root, 0, minimumBound, NR_TASKS);
            distance = solution.getFirst();
            if (distance == -1) {
                System.out.println(solution.getSecond().numberOfSteps + " steps - " + (System.currentTimeMillis() - time) + "ms");
                return solution.getSecond();
            } else {
                System.out.println(distance + " steps - " + (System.currentTimeMillis() - time) + "ms");
            }
            minimumBound = distance;
        }
    }

    private static Pair<Integer, Matrix> checkEstimation(int estimation, int bound, Matrix matrix) {
        if (estimation > bound) {
            return new Pair<>(estimation, matrix);
        }
        if (estimation > 80) {
            return new Pair<>(estimation, matrix);
        }
        if (matrix.manhattan == 0) {
            return new Pair<>(-1, matrix);
        }
        return null;
    }

    /**
     * Parallel search
     * @param current the current matrix object
     * @param numSteps the number of steps needed to reach current matrix
     * @param bound manhattan estimation
     * @return the fastest solution
     */
    public static Pair<Integer, Matrix> searchParallel(Matrix current, int numSteps, int bound, int nrThreads) throws ExecutionException, InterruptedException {
        if (nrThreads <= 1)
            return search(current, numSteps, bound);

        var checkResult = checkEstimation(numSteps + current.manhattan, bound, current);
        if (checkResult != null) return checkResult;

        int minimum = Integer.MAX_VALUE;
        List<Matrix> moves = current.generateMoves();
        var futures = moves.stream()
                .map(next -> executorService.submit(() -> searchParallel(next, numSteps + 1, bound, nrThreads / moves.size())))
                .collect(Collectors.toList());

        for (Future<Pair<Integer, Matrix>> future : futures) {
            Pair<Integer, Matrix> result = future.get();
            int t = result.getFirst();
            if (t == -1) {
                return new Pair<>(-1, result.getSecond());
            }
            if (t < minimum) {
                minimum = t;
            }
        }
        return new Pair<>(minimum, current);
    }

    /**
     * Simple search
     * @param current the current matrix object
     * @param numSteps the number of steps needed to reach current matrix
     * @param bound manhattan estimation
     * @return the fastest solution
     */
    public static Pair<Integer, Matrix> search(Matrix current, int numSteps, int bound) {
        var checkResult = checkEstimation(numSteps + current.manhattan, bound, current);
        if (checkResult != null) return checkResult;

        int minimum = Integer.MAX_VALUE;
        Matrix solution = null;
        for (Matrix next : current.generateMoves()) {
            // for each possible moves we have to perform the same search
            Pair<Integer, Matrix> result = search(next, numSteps + 1, bound);
            int currentMinimum = result.getFirst();
            if (currentMinimum == -1) {
                // stop condition reached
                return new Pair<>(-1, result.getSecond());
            }
            if (currentMinimum < minimum) {
                // compare to the minimum and store the faster solution
                minimum = currentMinimum;
                solution = result.getSecond();
            }
        }
        return new Pair<>(minimum, solution);
    }
}