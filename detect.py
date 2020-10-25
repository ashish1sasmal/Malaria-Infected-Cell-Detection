# @Author: ASHISH SASMAL <ashish>
# @Date:   22-10-2020
# @Last modified by:   ashish
# @Last modified time: 22-10-2020

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import joblib

df = pd.read_csv("malaria.csv")
print(df.head())

x = df.drop(["Label"],axis=1)
y = df["Label"]

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = RandomForestClassifier(n_estimators=100,max_depth=5)
model.fit(x_train,y_train)

joblib.dump(model,"malaria.pkl")

preds = model.predict(x_test)

print(metrics.classification_report(preds, y_test))
