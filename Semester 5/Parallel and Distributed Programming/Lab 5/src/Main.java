import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws InterruptedException {
        int[] poly1 = {1, 2, 3, 4};
        int[] poly2 = {4, 3, 2, 1};

        System.out.println("Input Polynomials:");
        System.out.println("Poly1: " + Arrays.toString(poly1));
        System.out.println("Poly2: " + Arrays.toString(poly2));

        long start = System.nanoTime();
        int[] resultRegularSequential = RegularMultiplication.multiplySequential(poly1, poly2);
        long end = System.nanoTime();
        System.out.println("\nRegular Sequential Result: " + Arrays.toString(resultRegularSequential));
        System.out.println("Time Taken (Regular Sequential): " + (end - start) / 1_000_000.0 + " ms");

        start = System.nanoTime();
        int[] resultRegularParallel = ParallelRegularMultiplication.multiplyParallel(poly1, poly2);
        end = System.nanoTime();
        System.out.println("\nRegular Parallel Result: " + Arrays.toString(resultRegularParallel));
        System.out.println("Time Taken (Regular Parallel): " + (end - start) / 1_000_000.0 + " ms");

        start = System.nanoTime();
        int[] resultKaratsubaSequential = KaratsubaMultiplication.karatsubaSequential(poly1, poly2);
        end = System.nanoTime();
        System.out.println("\nKaratsuba Sequential Result: " + Arrays.toString(resultKaratsubaSequential));
        System.out.println("Time Taken (Karatsuba Sequential): " + (end - start) / 1_000_000.0 + " ms");

        start = System.nanoTime();
        int[] resultKaratsubaParallel = ParallelKaratsubaMultiplication.karatsubaParallel(poly1, poly2);
        end = System.nanoTime();
        System.out.println("\nKaratsuba Parallel Result: " + Arrays.toString(resultKaratsubaParallel));
        System.out.println("Time Taken (Karatsuba Parallel): " + (end - start) / 1_000_000.0 + " ms");

    }
}
