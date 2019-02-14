import numpy as np
import json
from Retrieval import Retrieval

retrievalInstance = Retrieval()

valfile = open("../../quasar-s_dev_formatted.json", 'r')
valData = json.load(valfile)
valfile.close()

Count_MNB_file = open("results/Count_MNB_pred", 'r')
Tfidf_MNB_file = open("results/Tfidf_MNB_pred", 'r')
Count_SVM_file = open("results/Count_SVM_pred", 'r')
Tfidf_SVM_file = open("results/Tfidf_SVM_pred", 'r')
Count_MLP_file = open("results/Count_MLP_pred", 'r')
Tfidf_MLP_file = open("results/Tfidf_MLP_pred", 'r')

Count_MNB = []
Tfidf_MNB = []
Count_SVM = []
Tfidf_SVM = []
Count_MLP = []
Tfidf_MLP = []
for i in Count_MNB_file:
    e = i.strip().split(' ')
    Count_MNB.append(e[0])
for i in Tfidf_MNB_file:
    e = i.strip().split(' ')
    Tfidf_MNB.append(e[0])
for i in Count_SVM_file:
    e = i.strip().split(' ')
    Count_SVM.append(e[0])
for i in Tfidf_SVM_file:
    e = i.strip().split(' ')
    Tfidf_SVM.append(e[0])
for i in Count_MLP_file:
    e = i.strip().split(' ')
    Count_MLP.append(e[0])
for i in Tfidf_MLP_file:
    e = i.strip().split(' ')
    Tfidf_MLP.append(e[0])

false = 0
true = 0
for j in range(len(Count_MNB)):
    if Count_MNB[j] == '0' and \
        Tfidf_MNB[j] == '0' and \
        Count_SVM[j] == '0' and \
        Tfidf_SVM[j] == '0' and \
        Count_MLP[j] == '0' and \
        Tfidf_MLP[j] == '0':
        false += 1
        if j < 10: # take some examples here not all
            print "Question {} is predicted false for all the six models.".format(j+1)
            question = valData["questions"][j]
            X = question['query']
            Y = question['answers'][0]
            print "Q:", X
            print "A:", Y
            print ""
    elif Count_MNB[j] == '1' and \
        Tfidf_MNB[j] == '1' and \
        Count_SVM[j] == '1' and \
        Tfidf_SVM[j] == '1' and \
        Count_MLP[j] == '1' and \
        Tfidf_MLP[j] == '1':
        true += 1
        print "Question {} is predicted true for all the six models.".format(j+1)
        question = valData["questions"][j]
        X = question['query']
        Y = question['answers'][0]
        print "Q:", X
        print "A:", Y
        print ""
    # else:
    #     print "All different."

print "==============================="
print "In total"
print "All false: {}".format(false)
print "All true: {}".format(true)