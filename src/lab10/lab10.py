""" Lab 10: Save people
You can save people from heart disease by training a model to predict whether a person has heart disease or not.
The dataset is available at src/lab8/heart.csv
Train a model to predict whether a person has heart disease or not and test its performance.
You can usually improve the model by normalizing the input data. Try that and see if it improves the performance. 
"""
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import ConfusionMatrixDisplay

from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

data = pd.read_csv("src/lab10/heart.csv")

# Transform the categorical variables into dummy variables.
print(data.head())
string_col = data.select_dtypes(include="object").columns
df = pd.get_dummies(data, columns=string_col, drop_first=False)
print(data.head())

y = df.HeartDisease.values
x = df.drop(["HeartDisease"], axis=1)
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=25
)

""" Train a sklearn model here. """
clf = KNeighborsClassifier(n_neighbors=3)
sklearn_model = clf.fit(x_train, y_train)

# Accuracy
print("Accuracy of model: {}\n".format(sklearn_model.score(x_test, y_test)))

""" Improve the model by normalizing the input data. """
normalized_df=(df-df.min())/(df.max()-df.min())


y = normalized_df.HeartDisease.values
x = normalized_df.drop(["HeartDisease"], axis=1)
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=25
)

clf = KNeighborsClassifier(n_neighbors=3)
sklearn_model = clf.fit(x_train, y_train)

print("Accuracy of improved model: {}\n".format(sklearn_model.score(x_test, y_test)))

predictions = clf.predict(x_test)
cm = confusion_matrix(y_test, predictions, labels=clf.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=np.array(["Heart Disease","No Heart Disease"]))
disp.plot()
plt.show()
