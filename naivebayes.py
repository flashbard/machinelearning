#Naive Bayes from sklearn to implement simple truth table prediction, where the first column corelates to the output.
#NOTE: GaussianNB requires INT values for class labels, so does not work with float values.
import numpy as np
from sklearn.naive_bayes import GaussianNB

X = np.array([[0,0], 
			  [0,1], 
			  [1,1]])
Y = np.array([0, 
			  0,
			  1])

clf = GaussianNB()	#set the classifier
clf.fit(X,Y)	#Train, X-input, Y-output

print clf.predict([[1,0]])	#Predict

print clf.score(X, Y) #For accuracy scores. Obviously use this on test data!