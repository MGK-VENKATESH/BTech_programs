import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class QueueOperations {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Queue<Integer> queue = new LinkedList<>();

        while (true) {
            System.out.println("\nQueue Operations:");
            System.out.println("1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Peek");
            System.out.println("4. Display");
            System.out.println("5. Size");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter element to enqueue: ");
                    int element = scanner.nextInt();
                    queue.add(element);
                    System.out.println("Element enqueued successfully.");
                    break;
                case 2:
                    if (!queue.isEmpty()) {
                        int removedElement = queue.remove();
                        System.out.println("Element dequeued: " + removedElement);
                    } else {
                        System.out.println("Queue is empty. Dequeue operation failed.");
                    }
                    break;
                case 3:
                    if (!queue.isEmpty()) {
                        int peekedElement = queue.peek();
                        System.out.println("Peeked element: " + peekedElement);
                    } else {
                        System.out.println("Queue is empty. Peek operation failed.");
                    }
                    break;
                case 4:
                    System.out.println("Queue elements: " + queue);
                    break;
                case 5:
                    System.out.println("Queue size: " + queue.size());
                    break;
                case 6:
                    System.out.println("Exiting program...");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please enter a valid option.");
            }
        }
    }
}
