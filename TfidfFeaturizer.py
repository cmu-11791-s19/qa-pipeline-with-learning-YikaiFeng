from Featurizer import Featurizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


#This is a subclass that extends the abstract class Featurizer.
class TfidfFeaturizer(Featurizer):

	#The abstract method from the base class is implemeted here to return count features
	def getFeatureRepresentation(self, X_train, X_val):
		vectorizer = TfidfVectorizer()
		X_train_counts = vectorizer.fit_transform(X_train)
		X_val_counts = vectorizer.transform(X_val)
		return X_train_counts, X_val_counts