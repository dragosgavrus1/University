import java.util.*;
import java.util.concurrent.*;

public class HamiltonianCycle {
    private final int[][] graph; // Adjacency matrix
    private final int vertices;
    private final ExecutorService executor;

    public HamiltonianCycle(int[][] graph) {
        this.graph = graph;
        this.vertices = graph.length;
        this.executor = Executors.newCachedThreadPool();
    }

    public List<Integer> findHamiltonianCycle(int start) throws InterruptedException {
        List<Integer> path = Collections.synchronizedList(new ArrayList<>());
        path.add(start);

        Future<List<Integer>> result = executor.submit(() -> search(start, path, new HashSet<>()));
        try {
            return result.get(); // Wait for the result
        } catch (ExecutionException e) {
            e.printStackTrace();
            return null;
        } finally {
            executor.shutdown();
        }
    }

    private List<Integer> search(int current, List<Integer> path, Set<Integer> visited) {
        visited.add(current);

        // Base case: Check if path forms a cycle
        if (path.size() == vertices && graph[current][path.get(0)] == 1) {
            path.add(path.get(0)); // Close the cycle
            return path;
        }

        // Explore neighbors
        List<Future<List<Integer>>> futures = new ArrayList<>();
        for (int neighbor = 0; neighbor < vertices; neighbor++) {
            if (!visited.contains(neighbor) && graph[current][neighbor] == 1) {
                List<Integer> newPath = new ArrayList<>(path);
                newPath.add(neighbor);
                Set<Integer> newVisited = new HashSet<>(visited);

                int finalNeighbor = neighbor;
                futures.add(executor.submit(() -> search(finalNeighbor, newPath, newVisited)));
            }
        }

        // Wait for results
        for (Future<List<Integer>> future : futures) {
            try {
                List<Integer> result = future.get();
                if (result != null) {
                    return result; // Return the first valid cycle
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        return null; // No cycle found
    }

    public static void main(String[] args) throws InterruptedException {
        // Example graph (Adjacency matrix)
        int[][] graph = {
                {0, 1, 0, 1},
                {1, 0, 1, 1},
                {0, 1, 0, 1},
                {1, 1, 1, 0}
        };

        HamiltonianCycle hc = new HamiltonianCycle(graph);

        System.out.println("Starting Hamiltonian Cycle search...");
        long startTime = System.currentTimeMillis(); // Record start time

        List<Integer> cycle = hc.findHamiltonianCycle(0);

        long endTime = System.currentTimeMillis(); // Record end time
        System.out.println("Hamiltonian Cycle search completed.");

        if (cycle != null) {
            System.out.println("Hamiltonian Cycle: " + cycle);
        } else {
            System.out.println("No Hamiltonian Cycle found.");
        }

        long executionTime = endTime - startTime; // Calculate execution time
        System.out.println("Execution Time: " + executionTime + " ms");
    }

}
