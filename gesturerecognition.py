# Creating and testing a SVM model for gesture classification.
# importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

# Importing data
df = pd.read_csv('totdata.csv')
df.head

# Separating dependant (Gesture) and independant (Features) vairables.
y = df['Gesture']
x = df.drop(['Gesture'], axis=1)
x.head()

# splitting the data into test and train data with 80/20 ratio.
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.20, random_state=0)

# Creating a SVM model
classifier = svm.SVC(kernel='linear', gamma='auto', C=2)
classifier.fit(x_train, y_train)
# predicting the gestures using test data
y_predict = classifier.predict(x_test)
# Calculating the accuracy by comparing the predicted data with actual data.
accuracy = accuracy_score(y_test, y_predict)
# converting accuracy to percentage and printing results
print(f"accuracy = {accuracy*100}%")
