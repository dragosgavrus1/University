import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Matrix {
    private static final byte[] moveVertically = new byte[]{0, -1, 0, 1};
    private static final byte[] moveHorizontally = new byte[]{-1, 0, 1, 0};
    private static final String[] MOVES = new String[]{"left", "up", "right", "down"};

    private final byte[][] values;

    public final int numberOfSteps;
    private final int freeI;
    private final int freeJ;

    private final Matrix previousState;
    public final int manhattan;
    private final String move;


    public Matrix(byte[][] values, int freeI, int freeJ, int numberOfSteps, Matrix previousState, String move) {
        this.values = values;
        this.freeI = freeI;
        this.freeJ = freeJ;
        this.numberOfSteps = numberOfSteps;
        this.previousState = previousState;
        this.move = move;
        this.manhattan = manhattanDistance();
    }

    /**
     * Read values one by one from the file and create a Matrix.
     * @return The matrix resulted from the input file
     */
    public static Matrix readFromFile() throws IOException {
        byte[][] values = new byte[4][4];
        int freeI = -1, freeJ = -1;
        Scanner scanner = new Scanner(new BufferedReader(new FileReader("input.in")));
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                values[i][j] = Integer.valueOf(scanner.nextInt()).byteValue();
                if (values[i][j] == 0) {
                    freeI = i;
                    freeJ = j;
                }
            }
        }
        return new Matrix(values, freeI, freeJ, 0, null, "");
    }

    /**
     * The sum where each term is how far is a value from it's correct position with both vertical and horizontal
     * measures. This is a heuristic. Also there are slightly better alternatives such as "The Manhattan Pair Distance".
     * @return Manhattan Distance for 15 puzzle problem
     */
    public int manhattanDistance() {
        int sum = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (values[i][j] != 0) {
                    int targetI = (values[i][j] - 1) / 4;
                    int targetJ = (values[i][j] - 1) % 4;
                    sum += Math.abs(i - targetI) + Math.abs(j - targetJ);
                }
            }
        }
        return sum;
    }

    /**
     * Generate a list of possible states performing one of the "left", "up", "right", "down" moves.
     * (possible - free position must be kept within bounds and does not repeat ex: "up"-"down"-"up")
     * @return The list of possible future states
     */
    public List<Matrix> generateMoves() {
        List<Matrix> possibleFutureStates = new ArrayList<>();
        for (int k = 0; k < 4; k++) {
            if (freeI + moveVertically[k] >= 0 && freeI + moveVertically[k] < 4 && freeJ + moveHorizontally[k] >= 0 && freeJ + moveHorizontally[k] < 4) {
                int movedFreePosI = freeI + moveVertically[k];
                int movedFreePosJ = freeJ + moveHorizontally[k];
                if (previousState != null && movedFreePosI == previousState.freeI && movedFreePosJ == previousState.freeJ) {
                    continue;
                }
                byte[][] movedTiles = Arrays.stream(values)
                        .map(byte[]::clone)
                        .toArray(byte[][]::new);
                movedTiles[freeI][freeJ] = movedTiles[movedFreePosI][movedFreePosJ];
                movedTiles[movedFreePosI][movedFreePosJ] = 0;

                possibleFutureStates.add(new Matrix(movedTiles, movedFreePosI, movedFreePosJ, numberOfSteps + 1, this, MOVES[k]));
            }
        }
        return possibleFutureStates;
    }

    /**
     * Go from the final state in each previous state, append them to the result and reverse the result in order to
     * start with the initial state and end with the final one.
     * @return The string representation
     */
    @Override
    public String toString() {
        Matrix current = this;
        List<String> strings = new ArrayList<>();
        while (current != null) {
            StringBuilder sb = new StringBuilder();
            sb.append("\n");
            sb.append(current.move);
            sb.append("\n");
            Arrays.stream(current.values).forEach(row -> sb.append(Arrays.toString(row)).append("\n"));
            strings.add(sb.toString());
            current = current.previousState;
        }
        Collections.reverse(strings);
        return "Moves\n" +
                String.join("", strings) + "\n" +
                numberOfSteps + " steps";
    }
}