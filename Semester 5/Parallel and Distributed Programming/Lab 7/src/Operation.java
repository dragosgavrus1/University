import java.util.ArrayList;
import java.util.List;

public class Operation {
    public static Polynomial multiplySimple(Object o, Object o1, int begin, int end) {
        Polynomial p = (Polynomial) o;
        Polynomial q = (Polynomial) o1;
        Polynomial result = Polynomial.buildEmptyPolynomial(p.degree*2 + 1);
        for (int i = begin; i < end; i++) {
            for (int j = 0; j < q.coefficients.size(); j++) {
                result.coefficients.set(i + j, result.coefficients.get(i + j) + p.coefficients.get(i) * q.coefficients.get(j));
            }
        }
        return result;
    }

    public static Polynomial buildResult(Object[] polynomials) {
        int degree = ((Polynomial) polynomials[0]).degree;
        Polynomial result = Polynomial.buildEmptyPolynomial(degree+1);
        for (int i = 0; i < result.coefficients.size(); i++) {
            for (Object polynomial : polynomials) {
                result.coefficients.set(i, result.coefficients.get(i) + ((Polynomial) polynomial).coefficients.get(i));
            }
        }
        return result;
    }

    public static Polynomial simpleSequential(Polynomial p1, Polynomial p2) {
        int sizeOfResultCoefficientList = p1.degree + p2.degree + 1;
        List<Integer> coefficients = new ArrayList<>();
        for (int i = 0; i < sizeOfResultCoefficientList; i++) {
            coefficients.add(0);
        }
        for (int i = 0; i < p1.coefficients.size(); i++) {
            for (int j = 0; j < p2.coefficients.size(); j++) {
                int index = i + j;
                int value = p1.coefficients.get(i) * p2.coefficients.get(j);
                coefficients.set(index, coefficients.get(index) + value);
            }
        }
        return new Polynomial(coefficients);
    }

    public static Polynomial karatsubaSequential(Polynomial p1, Polynomial p2) {
        if (p1.degree < 2 || p2.degree < 2) {
            return simpleSequential(p1, p2);
        }

        int len = Math.max(p1.degree, p2.degree) / 2;
        Polynomial lowP1 = new Polynomial(p1.coefficients.subList(0, len));
        Polynomial highP1 = new Polynomial(p1.coefficients.subList(len, p1.getLength()));
        Polynomial lowP2 = new Polynomial(p2.coefficients.subList(0, len));
        Polynomial highP2 = new Polynomial(p2.coefficients.subList(len, p2.getLength()));

        Polynomial z1 = karatsubaSequential(lowP1, lowP2);
        Polynomial z2 = karatsubaSequential(Polynomial.add(lowP1, highP1), Polynomial.add(lowP2, highP2));
        Polynomial z3 = karatsubaSequential(highP1, highP2);

        //calculate the final result
        Polynomial r1 = Polynomial.addZeros(z3, 2 * len);
        Polynomial r2 = Polynomial.addZeros(Polynomial.subtract(Polynomial.subtract(z2, z3), z1), len);
        return Polynomial.add(Polynomial.add(r1, r2), z1);
    }
}