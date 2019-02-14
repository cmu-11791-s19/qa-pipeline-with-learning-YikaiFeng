# Report

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

The table above showed several comparison among two Featurizers and three Classifiers using metrics of Accuracy (a), Precision (p), Recall (r) and F-measure (f).

### Count based vs Tf-idf based

Different featurizers performed on datasets have different influence on a, p, r and f. However the selection of featurizers did not seem to be the main aspect to affect the overall performance. From the table, Count based featurizer outperformed Tf-idf featurizer under MNB and MLP classifier, while in SVM, Count based performed worse than Tf-idf featurizer. Therefore, I assumed that either different model has a different preference on the featurizer or the selection of classifiers played a more important role in this QA task than the one of featurizers.

### MNB vs SVM vs MLP

The performance of different classifier model is quite varied than each other on the a, p, r and f metrics. Support Vector Machine (SVM) achieved the first place Multinomial Naive Bayes (MNB)

## Error Analysis

Comparing the prediction results output by the six models, I observed that there are 