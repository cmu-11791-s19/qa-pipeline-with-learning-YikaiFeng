import sys
import json
from sklearn.externals import joblib

from Retrieval import Retrieval
from Featurizer import Featurizer
from CountFeaturizer import CountFeaturizer
from TfidfFeaturizer import TfidfFeaturizer
from Classifier import Classifier
from MultinomialNaiveBayes import MultinomialNaiveBayes
from SVM import SVM
from MLP import MLP
from Evaluator import Evaluator



class Pipeline(object):
	def __init__(self, trainFilePath, valFilePath, retrievalInstance, featurizerInstance, classifierInstance, predFilePath):
		self.retrievalInstance = retrievalInstance
		self.featurizerInstance = featurizerInstance
		self.classifierInstance = classifierInstance
		self.predFile = predFilePath
		trainfile = open(trainFilePath, 'r')
		self.trainData = json.load(trainfile)
		trainfile.close()
		valfile = open(valFilePath, 'r')
		self.valData = json.load(valfile)
		valfile.close()
		self.question_answering()

	def makeXY(self, dataQuestions):
		X = []
		Y = []
		for question in dataQuestions:
			
			long_snippets = self.retrievalInstance.getLongSnippets(question)
			short_snippets = self.retrievalInstance.getShortSnippets(question)
			
			X.append(short_snippets)
			Y.append(question['answers'][0])
			
		return X, Y


	def question_answering(self):
		dataset_type = self.trainData['origin']
		candidate_answers = self.trainData['candidates']
		X_train, Y_train = self.makeXY(self.trainData['questions'][0:6000])
		X_val, Y_val_true = self.makeXY(self.valData['questions'])

		#featurization
		X_features_train, X_features_val = self.featurizerInstance.getFeatureRepresentation(X_train, X_val)
		self.clf = self.classifierInstance.buildClassifier(X_features_train, Y_train)
		
		#Prediction
		Y_val_pred = self.clf.predict(X_features_val)

		self.evaluatorInstance = Evaluator()
		a =  self.evaluatorInstance.getAccuracy(Y_val_true, Y_val_pred)
		p,r,f = self.evaluatorInstance.getPRF(Y_val_true, Y_val_pred)

		# write to file: comparison, pred, true
		print self.predFile
		predfile = open(self.predFile, 'w')
		for i in range(len(Y_val_true)):
			if Y_val_true[i] == Y_val_pred[i]:
				predfile.write("1 " + str(Y_val_pred[i]) + " " + str(Y_val_true[i]) + '\n')
			elif Y_val_true[i] != Y_val_pred[i]:
				predfile.write("0 " + str(Y_val_pred[i]) + " " + str(Y_val_true[i]) + '\n')

		print "Accuracy: " + str(a)
		print "Precision: " + str(p)
		print "Recall: " + str(r)
		print "F-measure: " + str(f)
		


if __name__ == '__main__':
	trainFilePath = sys.argv[1] #please give the path to your reformatted quasar-s json train file
	valFilePath = sys.argv[2] # provide the path to val file
	retrievalInstance = Retrieval()
	featurizerInstance_count = CountFeaturizer()
	featurizerInstance_tfidf = TfidfFeaturizer()
	classifierInstance_mnb = MultinomialNaiveBayes()
	classifierInstance_svm = SVM()
	classifierInstance_mlp = MLP()
	predFilePath_1 = "../Count_MNB_pred"
	predFilePath_2 = "../Tfidf_MNB_pred"
	predFilePath_3 = "../Count_SVM_pred"
	predFilePath_4 = "../Tfidf_SVM_pred"
	predFilePath_5 = "../Count_MLP_pred"
	predFilePath_6 = "../Tfidf_MLP_pred"
	print "----- Count + MNB -----"
	trainInstance_1 = Pipeline(trainFilePath, valFilePath, retrievalInstance, featurizerInstance_count, classifierInstance_mnb, predFilePath_1)
	print "\n----- Tfidf + MNB -----"
	trainInstance_2 = Pipeline(trainFilePath, valFilePath, retrievalInstance, featurizerInstance_tfidf, classifierInstance_mnb, predFilePath_2)
	print "\n----- Count + SVM -----"
	trainInstance_3 = Pipeline(trainFilePath, valFilePath, retrievalInstance, featurizerInstance_count, classifierInstance_svm, predFilePath_3)
	print "\n----- Tfidf + SVM -----"
	trainInstance_4 = Pipeline(trainFilePath, valFilePath, retrievalInstance, featurizerInstance_tfidf, classifierInstance_svm, predFilePath_4)
	print "\n----- Count + MLP -----"
	trainInstance_5 = Pipeline(trainFilePath, valFilePath, retrievalInstance, featurizerInstance_count, classifierInstance_mlp, predFilePath_5)
	print "\n----- Tfidf + MLP -----"
	trainInstance_6 = Pipeline(trainFilePath, valFilePath, retrievalInstance, featurizerInstance_tfidf, classifierInstance_mlp, predFilePath_6)
