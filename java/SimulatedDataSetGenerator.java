import java.util.HashSet;
import java.util.Random;
import java.util.Set;

class SimulatedData {
    private int id;
    private String name;
    private double value;

    public SimulatedData(int id, String name, double value) {
        this.id = id;
        this.name = name;
        this.value = value;
    }

    @Override
    public String toString() {
        return "SimulatedData{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", value=" + value +
                '}';
    }
}

public class SimulatedDataSetGenerator {
    public static void main(String[] args) {
        // Generate a simulated data set with unique instances
        Set<SimulatedData> dataSet = generateSimulatedDataSet(10);

        // Display the generated data set
        for (SimulatedData data : dataSet) {
            System.out.println(data);
        }
    }

    private static Set<SimulatedData> generateSimulatedDataSet(int size) {
        Set<SimulatedData> dataSet = new HashSet<>();
        Random random = new Random();

        for (int i = 1; i <= size; i++) {
            int id = i;
            String name = "Item" + i;
            double value = random.nextDouble() * 100; // Generating a random value

            SimulatedData data = new SimulatedData(id, name, value);

            // Check for uniqueness before adding to the set
            while (!dataSet.add(data)) {
                // If not unique, regenerate the values
                id = random.nextInt(size) + 1;
                name = "Item" + id;
                value = random.nextDouble() * 100;
                data = new SimulatedData(id, name, value);
            }
        }

        return dataSet;
    }
}
