Link to Data Set: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

The project focuses on credit card fraud detection using a Crisp DM (Cross-Industry Standard Process for Data Mining) approach. It addresses the challenge of class imbalance, where the number of fraud transactions is much lower than legitimate transactions.

The project aims to build a model that can effectively detect credit card fraud in real-time by treating it as an anomaly detection problem. The dataset used for this project is the Kaggle Credit Card Fraud Detection Dataset.

The data consists of 32 features, including V1-V28 (unknown features for confidentiality), Time, Amount, and Class. The target variable is "Class," where 0 represents legitimate transactions and 1 represents fraud transactions.

The project involves several steps:

Business Understanding: Describes the problem of credit card fraud detection, the class imbalance issue, and the need for an anomaly detection approach.

Data Understanding: Provides an overview of the dataset, including the features, target variable, and the absence of missing values. It also mentions that the features are numerical and need to be standardized for comparison.

Data Preparation: Highlights that no missing values need to be handled. It mentions that the data should be standardized for comparison and states the mean and standard deviation of the transaction amounts. It also mentions that the time feature is distributed equitably and serves as an independent feature.

Model Selection and Evaluation: The project utilizes various classification algorithms, including Logistic Regression, SVM, K-Nearest Neighbors, Decision Tree, Random Forest, and SGD Classifier. It employs evaluation metrics such as precision, recall, F1 score, ROC AUC score, accuracy, and Matthews Correlation Coefficient. Cross-validation techniques like K-Fold and Stratified K-Fold are used for robust evaluation. Grid search is employed for hyperparameter tuning.

Data Balancing: The project addresses the class imbalance issue by using the Synthetic Minority Over-sampling Technique (SMOTE) to balance the data and avoid overfitting on legitimate transactions.

The provided code demonstrates the implementation of the project, including data loading, data description, and the use of various libraries and techniques for data analysis, model training, and evaluation.

Overall, the project aims to build a robust credit card fraud detection model by addressing class imbalance and utilizing an anomaly detection approach
