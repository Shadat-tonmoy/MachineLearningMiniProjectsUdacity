#!/usr/bin/python
import math
from operator import attrgetter



def getKey(item):
    return item[2]
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    data_objects = []
    for prediction,actual,age in zip(predictions,net_worths,ages):
        data_objects.append((age,actual,findError(prediction,actual)))
    data_objects = sorted(data_objects,key=getKey)
    cleaned_data = data_objects[0:81]    
    return cleaned_data

def findError(predictedValue,actualValue):
    return math.pow((actualValue-predictedValue),2)
