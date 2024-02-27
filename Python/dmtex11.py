from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

# Load the Iris dataset (you can replace this with your dataset)
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Naive Bayes classifier (Gaussian Naive Bayes for continuous features)
model = GaussianNB()

# Train the classifier using the training data
model.fit(X_train, y_train)

# Predict the classes for test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = metrics.accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Classification report
print("\nClassification Report:")
print(metrics.classification_report(y_test, y_pred))

# Confusion matrix
print("\nConfusion Matrix:")
print(metrics.confusion_matrix(y_test, y_pred))
