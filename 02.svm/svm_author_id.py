#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score



### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
# features_train = features_train[:len(features_train)/100] 
# labels_train = labels_train[:len(labels_train)/100] 

classifier = SVC(C=10000.0)
t0 = time() 
classifier.fit(features_train,labels_train)
trainingTime = round(time()-t0,3)
print "training time:", round(time()-t0, 3), "s"
t0 = time()
prediction = classifier.predict(features_test)
testingTime = round(time()-t0,3)
print "Testing Time "+str(testingTime)
print prediction
accuracy = accuracy_score(labels_test,prediction)
print accuracy
cris1 = 0
sara0 = 0
for i in prediction:
    if i == 1:
        cris1+=1
    elif i==0:
        sara0+=1
print "Cris "+str(cris1)+" Sara "+str(sara0)+" of Total "+str(len(prediction))






#########################################################
### your code goes here ###

#########################################################


