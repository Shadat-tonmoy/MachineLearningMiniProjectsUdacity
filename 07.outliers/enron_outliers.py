#!/usr/bin/python

import pickle
import sys
import math
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn import linear_model
from sklearn.cross_validation import train_test_split

def findError(prediction,actual):
    return math.pow((actual-prediction),2)

### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["bonus","salary"]
data = featureFormat(data_dict, features)
target,feature = targetFeatureSplit(data)
target_train,target_test,feature_train,feature_test = train_test_split(target,feature,test_size=0.5,random_state=42)
print "train feature ",len(feature_train)," train label ",len(target_train)
print "test feature ",len(feature_test)," test lablel ",len(target_test)
for key in data_dict:
    print key," Salary ",data_dict[key]['salary']," Bonus ",data_dict[key]['bonus']

for f,t in zip(feature,target):
    print "feature ",f," Target ",t

for point in data:
    salary = point[1]
    bonus = point[0]
    plt.scatter(salary,bonus)
reg = linear_model.LinearRegression()
reg.fit(feature,target)
predictions = reg.predict(feature)

max_error = 0
max_error_actual = -1
max_error_salary = -1
for prediction,actual,salary in zip(predictions,target,feature):
    print "Predictionn ",prediction," Actual ",actual," Error ",findError(prediction,actual)," Salary ",salary
    error = findError(prediction,actual)
    if error > max_error:
        max_error = error
        max_error_actual = actual
        max_error_salary = salary
        print "Checking ",max_error_actual
print "max_error ",max_error," max_error_actual ",max_error_actual," max error salary ",max_error_salary

for key in data_dict:
    if data_dict[key]['salary'] == max_error_salary[0]:
        print key," ",data_dict[key]['salary']
        break



try:
    plt.plot(feature,reg.predict(feature))
except Exception:
    pass

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()





### your code below



