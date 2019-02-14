# qa-pipeline-with-learning-YikaiFeng

qa-pipeline-with-learning-YikaiFeng created by GitHub Classroom

## Overview

In this assignment, I implemented a QA pipeline with the extension of the tf-idf Featurizer, SVM classifier and MLP classifier. The data set used to train on is quasar-s_train which consists of 37,000 cloze-style questions. After completing training on different featurizers and classifiers, six models were applied to the development dataset, quasar-s_dev, which consists of 3139 questions. Then, the evaluator compared the prediction outputs by the models to the ground truth label and computed the accuracy, precision, recall and F-measure.

## Performance Comparison

| Features 	   | Classifier | Accuracy            | Precision             | Recall              | F-measure            |
| ------------ | ---------- | ------------------- | --------------------- | ------------------- | -------------------- |
| Count based  | MNB		| 0.062758840395      | 0.0429797493249       | 0.062758840395      | 0.0301701298451      |
| Count based  | SVM		| 0.0745460337687     | **0.0685281155679**   | 0.0745460337687     | 0.0628445053033      |
| Count based  | MLP		| 0.0302644154189     | 0.00259956980684      | 0.0302644154189     | 0.00335852741917     |
| Tf-idf based | MNB		| 0.0477859190825     | 0.00596826147975      | 0.0477859190825     | 0.00932774947469     |
| Tf-idf based | SVM		| **0.0949346925773** | 0.0676321735188       | **0.0949346925773** | **0.0640987975182**  |
| Tf-idf based | MLP		| 0.0296272698312     | 0.000877775117648     | 0.0296272698312     | 0.00170503471182     |

## Analysis

The table above shows several comparison among Featurizers and Classifiers with 

### Count based vs Tf-idf based

Different featurizers performed on datasets have different influence on a, p, r and f. However the selection of featurizers did not seem to be the main aspect to affect the overall performance. From the table, Count based featurizer outperforms Tf-idf featurizer under MNB and MLP classifier, while in SVM, Count based is worse than Tf-idf featurizer.

### MNB vs SVM vs MLP

It is showed by the table that different classifier model is more influencial on the a, p, r and f scores. Support Vector Machine (SVM) achieved the first place Multinomial Naive Bayes (MNB)

## Error Analysis

1. What are the broad insights? Does one category of features outperform another in all cases?

2. Relative Performance Analysis. A baseline system S and a new system S' can be compared by partitioning the dataset elements into four categories, given with mnemonic below: