import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data = np.random.randn(1000)

# Create a histogram
plt.hist(data, bins=30, alpha=0.5, color='blue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()



# Create a box plot
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(1, 1, 100)
data = [data1, data2]


plt.boxplot(data)
plt.xticks([1, 2], ['Data 1', 'Data 2'])
plt.xlabel('Dataset')
plt.ylabel('Value')
plt.title('Box Plot')
plt.show()



# Create a bar chart
labels = ['A', 'B', 'C', 'D']
values = [5, 7, 3, 8]

plt.bar(labels, values, color='green')
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')
plt.show()




# Create a pie chart
sizes = [30, 20, 25, 25]
labels = ['Category 1', 'Category 2', 'Category 3', 'Category 4']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Pie Chart')
plt.show()
