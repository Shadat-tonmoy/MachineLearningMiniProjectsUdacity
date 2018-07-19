from sklearn import svm
X = [[0,0],[1,1]]
Y = [0,1]
classifer = svm.SVC()
print (classifer.fit(X,Y))
