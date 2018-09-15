from sklearn.preprocessing import MinMaxScaler
import numpy as np
weights = np.array([[200000.],[1000000.],[175]])
row = weights.shape[0]
col = weights.shape[1]
print "Row ",row," Col ",col

scaler = MinMaxScaler()
rescaledWeights=scaler.fit_transform(weights)
print rescaledWeights
