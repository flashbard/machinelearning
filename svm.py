#SVM from sklearn to implement simple truth table prediction, where the first column corelates to the output.
#NOTE: SVC has a few important properties in addition to the kernel. These are: 
#1) gamma -> Controls the smoothness of the boundary. Greater gamma means less smooth
#2) C -> tradeoff between smooth decision boundary and correct classification. Large C means more training points correct.
import numpy as np
from sklearn.svm import SVC	#We're using Support Vector Classifier

X = np.array([[0,0], 
			  [0,1], 
			  [1,1]])
Y = np.array([0, 
			  0,
			  1])

clf = SVC(kernel='linear')	#set the classifier. Here kernel decides whether to draw a linear/non-linear boundary. kernel="rbf" or "sigmoid" or "poly".
clf.fit(X,Y)	#Train, X-input, Y-output

print clf.predict([[1,0]])	#Predict

#print clf.score(X, Y) #For accuracy scores. Obviously use this on test data!