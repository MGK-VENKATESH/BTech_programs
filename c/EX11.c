#include <stdio.h>
#include <stdbool.h>

#define INF 9999
#define MAX_NODES 10

// Function to find the minimum of two numbers
int min(int a, int b) {
    return (a < b) ? a : b;
}

// Function to initialize the routing table
void initialize(int costMatrix[MAX_NODES][MAX_NODES], int n, int sourceNode, int distance[MAX_NODES], int nextHop[MAX_NODES]) {
    for (int i = 0; i < n; i++) {
        distance[i] = costMatrix[sourceNode][i];
        nextHop[i] = (costMatrix[sourceNode][i] != INF) ? i : -1;
    }
}

// Function to perform the Distance Vector Routing algorithm
void distanceVector(int costMatrix[MAX_NODES][MAX_NODES], int n, int sourceNode) {
    int distance[MAX_NODES];
    int nextHop[MAX_NODES];

    // Initialize the routing table
    initialize(costMatrix, n, sourceNode, distance, nextHop);

    // Update the routing table iteratively until convergence
    bool updated;
    do {
        updated = false;
        for (int i = 0; i < n; i++) {
            if (i != sourceNode) {
                for (int j = 0; j < n; j++) {
                    if (costMatrix[i][j] + distance[j] < distance[i]) {
                        distance[i] = costMatrix[i][j] + distance[j];
                        nextHop[i] = j;
                        updated = true;
                    }
                }
            }
        }
    } while (updated);

    // Print the routing table
    printf("Routing Table for Node %d:\n", sourceNode);
    printf("Destination\tDistance\tNext Hop\n");
    for (int i = 0; i < n; i++) {
        printf("%d\t\t%d\t\t%d\n", i, distance[i], nextHop[i]);
    }
}

int main() {
    int n; // Number of nodes in the subnet graph
    int costMatrix[MAX_NODES][MAX_NODES]; // Cost matrix indicating delay between nodes

    printf("Enter the number of nodes: ");
    scanf("%d", &n);

    // Read the cost matrix
    printf("Enter the cost matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &costMatrix[i][j]);
            if (costMatrix[i][j] == 0) {
                costMatrix[i][j] = INF; // Set 0 weight as infinity
            }
        }
    }

    // Perform Distance Vector Routing for each node
    for (int i = 0; i < n; i++) {
        distanceVector(costMatrix, n, i);
        printf("\n");
    }

    return 0;
}