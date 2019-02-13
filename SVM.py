from Classifier import Classifier
from sklearn import svm


#This is a subclass that extends the abstract class Classifier.
class SVM(Classifier):

	#The abstract method from the base class is implemeted here to return multinomial naive bayes classifier
	def buildClassifier(self, X_features, Y_train):
		clf = svm.SVC(kernel='linear').fit(X_features, Y_train)
		return clf