import java.util.*;

public class StackOperations {
    private static final int MAX_SIZE = 100;
    private int[] stackArray;
    private int top;

    public StackOperations() {
        stackArray = new int[MAX_SIZE];
        top = -1;
    }

    // Method to check if the stack is empty
    public boolean isEmpty() {
        return (top == -1);
    }

    // Method to check if the stack is full
    public boolean isFull() {
        return (top == MAX_SIZE - 1);
    }

    // Method to push an element onto the stack
    public void push(int data) {
        if (isFull()) {
            System.out.println("Stack overflow. Cannot push element onto the stack.");
            return;
        }
        stackArray[++top] = data;
        System.out.println("Pushed element: " + data);
    }

    // Method to pop an element from the stack
    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack underflow. Cannot pop element from an empty stack.");
            return -1;
        }
        int poppedElement = stackArray[top--];
        System.out.println("Popped element: " + poppedElement);
        return poppedElement;
    }

    // Method to peek at the top element of the stack
    public int peek() {
        if (isEmpty()) {
            System.out.println("Stack is empty. No elements to peek.");
            return -1;
        }
        System.out.println("Top element: " + stackArray[top]);
        return stackArray[top];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StackOperations stack = new StackOperations();

        while (true) {
            System.out.println("\nStack Operations:");
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Peek");
            System.out.println("4. Check if the stack is empty");
            System.out.println("5. Exit");

            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter element to push: ");
                    int element = scanner.nextInt();
                    stack.push(element);
                    break;
                case 2:
                    stack.pop();
                    break;
                case 3:
                    stack.peek();
                    break;
                case 4:
                    System.out.println("Stack is empty: " + stack.isEmpty());
                    break;
                case 5:
                    System.out.println("Exiting program.");
                    System.exit(0);
                default:
                    System.out.println("Invalid choice. Please enter a valid option.");
            }
        }
    }
}
