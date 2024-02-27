import numpy as np

# Custom dataset (replace this with your own dataset)
# Here, I'm creating a simple dataset with four instances and two attributes
data = np.array([
    [1.2, 2.3],
    [3.5, 4.8],
    [2.0, 1.5],
    [4.0, 3.0]
])

# Function to compute Euclidean distance between two points
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

# Compute dissimilarity matrix using Euclidean distance
num_instances = len(data)
dissimilarity_matrix = np.zeros((num_instances, num_instances))

for i in range(num_instances):
    for j in range(num_instances):
        dissimilarity_matrix[i][j] = euclidean_distance(data[i], data[j])

# Display dissimilarity matrix
print("Dissimilarity Matrix:")
print(dissimilarity_matrix)
