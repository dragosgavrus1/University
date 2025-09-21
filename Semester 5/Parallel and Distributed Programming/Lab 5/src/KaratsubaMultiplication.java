import java.util.Arrays;

public class KaratsubaMultiplication {

    public static int[] karatsubaSequential(int[] poly1, int[] poly2) {
        int n = poly1.length;

        // Base case: Single coefficient multiplication
        if (n == 1) {
            return new int[] { poly1[0] * poly2[0] };
        }

        // Split the polynomials into two halves
        int half = n / 2;
        int[] low1 = Arrays.copyOfRange(poly1, 0, half);
        int[] high1 = Arrays.copyOfRange(poly1, half, n);
        int[] low2 = Arrays.copyOfRange(poly2, 0, half);
        int[] high2 = Arrays.copyOfRange(poly2, half, n);

        // Recursive calls
        int[] z0 = karatsubaSequential(low1, low2); // Product of lower halves
        int[] z2 = karatsubaSequential(high1, high2); // Product of higher halves
        int[] z1 = karatsubaSequential(add(low1, high1), add(low2, high2)); // Product of sums

        // Subtract z0 and z2 from z1
        z1 = subtract(z1, add(z0, z2));

        // Combine results
        return combine(z0, z1, z2, half);
    }

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
        int n = z0.length + z1.length + z2.length; // Maximum result size
        int[] result = new int[2 * half + z2.length];

        // Add z0 (low terms)
        for (int i = 0; i < z0.length; i++) {
            result[i] += z0[i];
        }

        // Add z1 (middle terms)
        for (int i = 0; i < z1.length; i++) {
            result[i + half] += z1[i];
        }

        // Add z2 (high terms)
        for (int i = 0; i < z2.length; i++) {
            result[i + 2 * half] += z2[i];
        }

        return result;
    }

}
