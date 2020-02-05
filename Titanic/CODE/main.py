import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error


plt.style.use('bmh')
pd.options.mode.chained_assignment = None
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)



training_data_file = '../DATA/train.csv'

data = pd.read_csv(training_data_file)
test_data = pd.read_csv("../DATA/test.csv")
data = data.dropna(axis = 0)
test_data = data.dropna(axis = 0)
y = data.Survived # thing we are going to predict





features = ['Pclass', 'Age', 'Sex', 'SibSp', 'Parch']
X = pd.get_dummies(data[features])


# print(X.describe())
# print(X.head())
# print(data.columns)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)#, test_size=0.33, random_state=42)

# print(y_train)

def get_mae(estimators = 100):
    model = AdaBoostClassifier(n_estimators=estimators, random_state=1)#max_depth=5, random_state=1)
    model.fit(X_train,y_train)
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    return mae


for i in np.arange(10, 100, 1):
    print(i, get_mae(i))
# plt.show()
