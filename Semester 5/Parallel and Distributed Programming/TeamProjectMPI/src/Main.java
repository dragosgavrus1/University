import mpi.*;

import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    public static void main(String[] args) throws IOException {
        /* Set up */
        MPI.Init(args);
        /* Local process index */
        int rank = MPI.COMM_WORLD.Rank();
        if (rank == 0) {
            // master
            Matrix matrix = Matrix.readFromFile();
            searchMaster(matrix);
        } else {
            // worker
            searchWorker();
        }
        /* Tear down */
        MPI.Finalize();
    }

    private static void searchMaster(Matrix root) {
        /*Total processes*/
        int size = MPI.COMM_WORLD.Size();
        int workers = size - 1;
        int minBound = root.manhattan;
        boolean found = false;
        long time = System.currentTimeMillis();

        // generate the start configurations
        Queue<Matrix> matrixQueue = new LinkedList<>();
        matrixQueue.add(root);
        while (true) {
            assert matrixQueue.peek() != null;
            if (!(matrixQueue.size() + matrixQueue.peek().generateMoves().size() - 1 <= workers)) break;
            Matrix current = matrixQueue.poll();
            assert current != null;
            matrixQueue.addAll(current.generateMoves());
        }

        while (!found) {
            // send data to all workers
            Queue<Matrix> temporaryQueue = new LinkedList<>(matrixQueue);
            for (int i = 0; i < matrixQueue.size(); i++) {
                // for each worker, send a "root"
                Matrix curr = temporaryQueue.poll();
                /* Send */
                MPI.COMM_WORLD.Send(new boolean[]{false}, 0, 1, MPI.BOOLEAN, i + 1, 0);
                MPI.COMM_WORLD.Send(new Object[]{curr}, 0, 1, MPI.OBJECT, i + 1, 0);
                MPI.COMM_WORLD.Send(new int[]{minBound}, 0, 1, MPI.INT, i + 1, 0);
            }

            Object[] pairs = new Object[size + 5];
            // receive data
            for (int i = 1; i <= matrixQueue.size(); i++) {
                /* Receive */
                MPI.COMM_WORLD.Recv(pairs, i - 1, 1, MPI.OBJECT, i, 0);
            }

            // check if any node found a solution
            int newMinBound = Integer.MAX_VALUE;
            for (int i = 0; i < matrixQueue.size(); i++) {
                Pair<Integer, Matrix> pair = (Pair<Integer, Matrix>) pairs[i];
                if (pair.getFirst() == -1) {
                    // found solution
                    System.out.println("Solution found in " + pair.getSecond().numberOfSteps + " steps");
                    System.out.println("Solution is: ");
                    System.out.println(pair.getSecond());
                    System.out.println("Execution time: " + (System.currentTimeMillis() - time) + "ms");
                    found = true;
                    break;
                } else if (pair.getFirst() < newMinBound) {
                    newMinBound = pair.getFirst();
                }
            }
            if(!found){
                System.out.println("Depth " + newMinBound + " reached in " + (System.currentTimeMillis() - time) + "ms");
                minBound = newMinBound;
            }
        }

        // shut down workers
        for (int i = 1; i < size; i++) {
            Matrix curr = matrixQueue.poll();
            /* Send */
            MPI.COMM_WORLD.Send(new boolean[]{true}, 0, 1, MPI.BOOLEAN, i, 0);
            MPI.COMM_WORLD.Send(new Object[]{curr}, 0, 1, MPI.OBJECT, i, 0);
            MPI.COMM_WORLD.Send(new int[]{minBound}, 0, 1, MPI.INT, i, 0);
        }
    }

    private static void searchWorker() {
        while (true) {
            Object[] matrix = new Object[1];
            int[] bound = new int[1];
            boolean[] end = new boolean[1];
            /* Receive */
            MPI.COMM_WORLD.Recv(end, 0, 1, MPI.BOOLEAN, 0, 0);
            MPI.COMM_WORLD.Recv(matrix, 0, 1, MPI.OBJECT, 0, 0);
            MPI.COMM_WORLD.Recv(bound, 0, 1, MPI.INT, 0, 0);
            if (end[0]) {
                // solution found
                return;
            }
            int minBound = bound[0];
            Matrix current = (Matrix) matrix[0];
            Pair<Integer, Matrix> result = search(current, current.numberOfSteps, minBound);
            /* Send */
            MPI.COMM_WORLD.Send(new Object[]{result}, 0, 1, MPI.OBJECT, 0, 0);
        }
    }

    /**
     * Simple search
     * @param current the current matrix object
     * @param numSteps the number of steps needed to reach current matrix
     * @param bound manhattan estimation
     * @return the fastest solution
     */
    public static Pair<Integer, Matrix> search(Matrix current, int numSteps, int bound) {
        int estimation = numSteps + current.manhattan;
        if (estimation > bound) {
            return new Pair<>(estimation, current);
        }
        if (estimation > 80) {
            return new Pair<>(estimation, current);
        }
        if (current.manhattan == 0) {
            return new Pair<>(-1, current);
        }
        int min = Integer.MAX_VALUE;
        Matrix solution = null;
        for (Matrix next : current.generateMoves()) {
            Pair<Integer, Matrix> result = search(next, numSteps + 1, bound);
            int t = result.getFirst();
            if (t == -1) {
                return new Pair<>(-1, result.getSecond());
            }
            if (t < min) {
                min = t;
                solution = result.getSecond();
            }
        }
        return new Pair<>(min, solution);
    }
}