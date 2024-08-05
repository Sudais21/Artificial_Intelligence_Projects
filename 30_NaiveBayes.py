import numpy as np
import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import metrics

data = {
  "Outlook": ["Sunny","Sunny","Overcast","Rain","Rain","Rain","Overcast","Sunny","Sunny","Rain","Sunny","Overcast","Overcast","Rain"],
  "Temperature": ["Hot","Hot","Hot","Mild","Cool","Cool","Cool","Mild","Cool","Mild","Mild","Mild","Hot","Mild"],
  "Humidity":["High","High","High","High","Normal","Normal","Normal","High","Normal","Normal","Normal","High","Normal","High"],
  "Wind":["Weak","Strong","Weak","Weak","Weak","Strong","Strong","Weak","Weak","Weak","Strong","Strong","Weak","Strong"],
  "Play_Tennis":["No","No","Yes","Yes","Yes","No","Yes","No","Yes","Yes","Yes","Yes","Yes","No"]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3","day4","day5","day6","day7","day8","day9","day10","day11","day12","day13","day14"])

print(df)
string_to_int= LabelEncoder()
df=df.apply(string_to_int.fit_transform)
print(df)
feature_cols = ['Outlook','Temperature','Humidity','Wind']
X = df[feature_cols ]
y = df.Play_Tennis
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.3,random_state=3)
model = CategoricalNB()
model.fit(X_train, Y_train)
prediction = model.predict(X_test)

print("CategoricalNB")
print("Accuracy:", metrics.accuracy_score(prediction, Y_test))
prediction=model.predict([[1,1,0,1]])
print("prediction",prediction)

print("GaussianNB")
model = GaussianNB()
model.fit(X_train, Y_train)
prediction = model.predict(X_test)
print("Accuracy:", metrics.accuracy_score(prediction, Y_test))
prediction=model.predict([[1,1,0,1]])
print("prediction",prediction)