# qa-pipeline-with-learning-YikaiFeng
qa-pipeline-with-learning-YikaiFeng created by GitHub Classroom
## Overview
In this assignment, I implemented a QA pipline with the extension of the tf-idf Featurizer, SVM classifier and MLP classifier. The data set used to trained on is quasar-s_train which consists of 37,000 cloze-style questions. After completely training on different featurizers and classifiers, six models were applied on the development dataset, quasar-s_dev, which consists of 3139 questions. Then, the evaluator compared the prediction outputs by the models to the ground truth label and computed the accuracy, precision, recall and F-measure.
## Performance Comparison
| Features 	   | Classifier | Accuracy        | Precision         | Recall          | F-measure        |
| ------------ | ---------- | --------------- | ----------------- | --------------- | ---------------- |
| Count based  | MNB		| 0.062758840395  | 0.0429797493249   | 0.062758840395  | 0.0301701298451  |
| Count based  | SVM		| 0.0745460337687 | 0.0685281155679   | 0.0745460337687 | 0.0628445053033  |
| Count based  | MLP		| 0.0302644154189 | 0.00259956980684  | 0.0302644154189 | 0.00335852741917 |
| Tf-idf based | MNB		| 0.0477859190825 | 0.00596826147975  | 0.0477859190825 | 0.00932774947469 |
| Tf-idf based | SVM		| 0.0949346925773 | 0.0676321735188   | 0.0949346925773 | 0.0640987975182  |
| Tf-idf based | MLP		| 0.0296272698312 | 0.000877775117648 | 0.0296272698312 | 0.00170503471182 |