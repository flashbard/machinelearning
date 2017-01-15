#Decision Trees from sklearn to implement simple truth table prediction, where the first column corelates to the output.
#NOTE: DTs have a few important parameters.
#1) min_sample_split -> how far do we go down the tree before we stop splitting. default is 2 (meaning splitting stops when no of leaves is 2). More splitting means more overfitting.
#2) criterion (impurity) -> gini or entropy (information gain).   
import numpy as np
from sklearn import tree

X = np.array([[0,0], 
			  [0,1], 
			  [1,1]])
Y = np.array([0, 
			  0,
			  1])

clf = tree.DecisionTreeClassifier()	#set the classifier.
clf.fit(X,Y)	#Train, X-input, Y-output

print clf.predict([[1,0]])	#Predict

#print clf.score(X, Y) #For accuracy scores. Obviously use this on test data!