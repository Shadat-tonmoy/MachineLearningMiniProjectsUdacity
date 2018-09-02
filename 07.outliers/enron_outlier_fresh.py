
import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
import numpy as np
from sklearn import linear_model
import math
from matplotlib import pyplot as plt



### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL",0)
data = featureFormat(data_dict, features)
feature,target = targetFeatureSplit(data)
feature = np.array(feature)
feature = np.reshape(feature,(len(feature),1))
target = np.array(target)
target = np.reshape(target,(len(target)))

for key in data_dict:
    print "Key ",key," Salary ",data_dict[key]["salary"]," Bonus ",data_dict[key]["bonus"]

for point in data:
    salary = point[0]
    bonus = point[1]
    plt.scatter( salary, bonus )

reg = linear_model.LinearRegression()
reg.fit(feature,target)
predictions = reg.predict(feature)

# print predictions
# print target


try:
    plt.plot(feature,predictions)
except Exception:
    pass


plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()

### your code below
