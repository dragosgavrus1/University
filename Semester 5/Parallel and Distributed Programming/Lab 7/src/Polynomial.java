import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

@SuppressWarnings("DuplicatedCode")
public class Polynomial implements Serializable {
    public final List<Integer> coefficients;
    public final int degree;
    private final int MAX = 10;

    public Polynomial(List<Integer> coefficients) {
        this.coefficients = coefficients;
        this.degree = coefficients.size() - 1;
    }

    public Polynomial(int degree) {
        this.degree = degree;
        coefficients = new ArrayList<>(degree + 1);

        // generate random coefficients
        Random random = new Random();
        for (int i = 0; i < degree; i++) {
            coefficients.add(random.nextInt(MAX));
        }
        coefficients.add(random.nextInt(MAX) + 1);
    }

    public static Polynomial addZeros(Polynomial polynomial, int offset) {
        List<Integer> coefficients = IntStream.range(0, offset).mapToObj(i -> 0).collect(Collectors.toList());
        coefficients.addAll(polynomial.coefficients);
        return new Polynomial(coefficients);
    }
    public static Polynomial add(Polynomial first, Polynomial second) {
        int degreeOfSmallerPolynomial = Math.min(first.degree, second.degree);
        int degreeOfBiggerPolynomial = Math.max(first.degree, second.degree);
        Polynomial biggerPolynomial = ((first.degree > second.degree) ? first : second);
        List<Integer> coefficients = new ArrayList<>(degreeOfBiggerPolynomial + 1);

        for (int i = 0; i <= degreeOfSmallerPolynomial; i++) {
            coefficients.add(first.coefficients.get(i) + second.coefficients.get(i));
        }

        addRemainingCoefficients(biggerPolynomial, degreeOfSmallerPolynomial, degreeOfBiggerPolynomial, coefficients);

        return new Polynomial(coefficients);
    }

    public static Polynomial subtract(Polynomial first, Polynomial second) {
        int degreeOfSmallerPolynomial = Math.min(first.degree, second.degree);
        int degreeOfBiggerPolynomial = Math.max(first.degree, second.degree);
        Polynomial biggerPolynomial = ((first.degree > second.degree) ? first : second);

        List<Integer> coefficients = new ArrayList<>(degreeOfBiggerPolynomial + 1);

        //Subtract the 2 polynomials
        for (int i = 0; i <= degreeOfSmallerPolynomial; i++) {
            coefficients.add(first.coefficients.get(i) - second.coefficients.get(i));
        }

        addRemainingCoefficients(biggerPolynomial, degreeOfSmallerPolynomial, degreeOfBiggerPolynomial, coefficients);

        //remove coefficients starting from biggest power if coefficient is 0
        int i = coefficients.size() - 1;
        while (coefficients.get(i) == 0 && i > 0) {
            coefficients.remove(i);
            i--;
        }

        return new Polynomial(coefficients);
    }

    private static void addRemainingCoefficients(Polynomial polynomial, int minDegree, int maxDegree, List<Integer> coefficients) {
        if (minDegree != maxDegree) {
            for (int i = minDegree + 1; i <= maxDegree; i++) {
                coefficients.add(polynomial.coefficients.get(i));
            }
        }
    }


    public static Polynomial buildEmptyPolynomial(int degree){
        List<Integer> zeros = IntStream.range(0, degree).mapToObj(i -> 0).collect(Collectors.toList());
        return new Polynomial(zeros);
    }

    public int getLength() {
        return this.coefficients.size();
    }

    @Override
    public String toString() {
        StringBuilder str = new StringBuilder();
        int power = 0;
        for (int i = 0; i <= this.degree; i++) {
            if (coefficients.get(i) == 0) {
                power++;
                continue;
            }
            str.append(" ").append(coefficients.get(i)).append("x^").append(power).append(" +");
            power++;
        }
        str.deleteCharAt(str.length() - 1); //delete last +
        return str.toString();
    }
}