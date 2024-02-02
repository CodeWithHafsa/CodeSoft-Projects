# Import necessary libraries
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Load the Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Fit the Decision Tree classifier with default hyper-parameters
clf = DecisionTreeClassifier(random_state=1234)
model = clf.fit(X, y)

# Print the text representation of the Decision Tree
text_representation = tree.export_text(clf)
print(text_representation)

# Visualize the Decision Tree
plt.figure(figsize=(12, 8))
tree.plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.title("Decision Tree Classifier - Iris Dataset")
plt.show()
