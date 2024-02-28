import java.util.Scanner;
import java.util.Stack;

public class StackOperations1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();
        
        while (true) {
            System.out.println("Stack Operations:");
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Peek");
            System.out.println("4. Display");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
            
            switch (choice) {
                case 1:
                    System.out.print("Enter element to push: ");
                    int element = scanner.nextInt();
                    stack.push(element);
                    System.out.println("Element pushed to stack.");
                    break;
                case 2:
                    if (!stack.isEmpty()) {
                        int poppedElement = stack.pop();
                        System.out.println("Popped element: " + poppedElement);
                    } else {
                        System.out.println("Stack is empty.");
                    }
                    break;
                case 3:
                    if (!stack.isEmpty()) {
                        int peekedElement = stack.peek();
                        System.out.println("Peeked element: " + peekedElement);
                    } else {
                        System.out.println("Stack is empty.");
                    }
                    break;
                case 4:
                    if (!stack.isEmpty()) {
                        System.out.println("Elements in stack:");
                        for (int i = stack.size() - 1; i >= 0; i--) {
                            System.out.println(stack.get(i));
                        }
                    } else {
                        System.out.println("Stack is empty.");
                    }
                    break;
                case 5:
                    System.out.println("Exiting program.");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please enter a valid option.");
            }
        }
    }
}
