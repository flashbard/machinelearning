#Pickling is used to store vars, classifiers or related data in a file, so that it can be used later, even after program termination.
#Very useful when you want to train a classifier once, but use it many times, in different programs.
import pickle

a="Just some data"

with open('mydata.pickle', 'wb') as f:
	pickle.dump(a,f)	#Replace a with the name of the classifier you want to pickle

pickle_in=open('mydata.pickle', 'rb')
a=pickle.load(pickle_in)

print a