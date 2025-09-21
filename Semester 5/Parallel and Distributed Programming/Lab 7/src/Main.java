import mpi.*;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

@SuppressWarnings("DuplicatedCode")
public class Main {

    private static final Boolean USE_KARATSUBA = false;
    private static final int POLYNOMIAL_ORDER = 5;

    private static void multiplicationMaster(Polynomial p, Polynomial q, int nrProcs) {
        long startTime = System.currentTimeMillis();
        int start, finish = 0;
        int len = p.getLength() / (nrProcs - 1);

        for (int i = 1; i < nrProcs; i++) {
            start = finish;
            finish += len;
            if (i == nrProcs - 1) {
                finish = p.getLength();
            }
            /* Send */
            MPI.COMM_WORLD.Send(new Object[]{p}, 0, 1, MPI.OBJECT, i, 0);
            MPI.COMM_WORLD.Send(new Object[]{q}, 0, 1, MPI.OBJECT, i, 0);

            MPI.COMM_WORLD.Send(new int[]{start}, 0, 1, MPI.INT, i, 0);
            MPI.COMM_WORLD.Send(new int[]{finish}, 0, 1, MPI.INT, i, 0);
        }

        Object[] results = new Object[nrProcs - 1];
        for (int i = 1; i < nrProcs; i++) {
            /* Receive */
            MPI.COMM_WORLD.Recv(results, i - 1, 1, MPI.OBJECT, i, 0);
        }

        Polynomial result = Operation.buildResult(results);
        long endTime = System.currentTimeMillis();
        System.out.println("result:\n" + result.toString());
        System.out.println("time: " + (endTime - startTime) + " ms");
    }

    private static void multiplySimpleWorker() {
        System.out.println("Worker started\n");

        Object[] p = new Object[2];
        Object[] q = new Object[2];
        int[] begin = new int[1];
        int[] end = new int[1];

        /* Receive */
        MPI.COMM_WORLD.Recv(p, 0, 1, MPI.OBJECT, 0, 0);
        MPI.COMM_WORLD.Recv(q, 0, 1, MPI.OBJECT, 0, 0);

        MPI.COMM_WORLD.Recv(begin, 0, 1, MPI.INT, 0, 0);
        MPI.COMM_WORLD.Recv(end, 0, 1, MPI.INT, 0, 0);

        Polynomial result = Operation.multiplySimple(p[0], q[0], begin[0], end[0]);

        /* Send */
        MPI.COMM_WORLD.Send(new Object[]{result}, 0, 1, MPI.OBJECT, 0, 0);

    }

    private static void multiplyKaratsubaWorker() {
        System.out.println("Worker started\n");

        Object[] p = new Object[2];
        Object[] q = new Object[2];
        int[] begin = new int[1];
        int[] end = new int[1];

        /* Receive */
        MPI.COMM_WORLD.Recv(p, 0, 1, MPI.OBJECT, 0, 0);
        MPI.COMM_WORLD.Recv(q, 0, 1, MPI.OBJECT, 0, 0);

        MPI.COMM_WORLD.Recv(begin, 0, 1, MPI.INT, 0, 0);
        MPI.COMM_WORLD.Recv(end, 0, 1, MPI.INT, 0, 0);

        Polynomial first = (Polynomial) p[0];
        Polynomial second = (Polynomial) q[0];

        for (int i = 0; i < begin[0]; i++) {
            first.coefficients.set(i, 0);
        }
        for (int j = end[0]; j < first.coefficients.size(); j++) {
            first.coefficients.set(j, 0);
        }

        Polynomial result = Operation.karatsubaSequential(first, second);

        /* Send */
        MPI.COMM_WORLD.Send(new Object[]{result}, 0, 1, MPI.OBJECT, 0, 0);
    }

    public static void main(String[] args) {
        /* Set up */
        MPI.Init(args);
        /* Local process index */
        int rank = MPI.COMM_WORLD.Rank();
        /* Total processes */
        int size = MPI.COMM_WORLD.Size();
        int[] poly1 = {1, 2, 3};
        int[] poly2 = {4, 5, 6};
        List<Integer> coefficients1 = Arrays.stream(poly1).boxed().collect(Collectors.toList());
        List<Integer> coefficients2 = Arrays.stream(poly2).boxed().collect(Collectors.toList());
        if (rank == 0) {
            Polynomial p = new Polynomial(coefficients1);
            System.out.println(p);
            Polynomial q = new Polynomial(coefficients2);
            System.out.println(q);
            multiplicationMaster(p, q, size);
        } else {
            if (USE_KARATSUBA) {
                multiplyKaratsubaWorker();
            } else {
                multiplySimpleWorker();
            }
        }
        /* Tear down */
        MPI.Finalize();
    }
}