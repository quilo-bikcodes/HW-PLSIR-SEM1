import numpy as np
import pandas as pd
import seaborn as sns
sns.set_palette('husl')
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import threading

iris_dataframe = pd.read_csv('iris.csv')

X = iris_dataframe.drop(['Id', 'Species'], axis=1)
Y = iris_dataframe['Species']

k_range = list(range(1,100))
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X, Y)
    y_pred = knn.predict(X)
    scores.append(metrics.accuracy_score(Y, y_pred))
    
plt.plot(k_range, scores)
plt.xlabel('Value of k for KNN')
plt.ylabel('Accuracy Score')
plt.title('Accuracy Scores for Values of k of k-Nearest-Neighbors')
plt.show()

logreg = LogisticRegression()
logreg.fit(X, Y)
y_pred = logreg.predict(X)
print(metrics.accuracy_score(Y, y_pred))