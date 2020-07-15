import numpy as np

data = [[1, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 0, 1, 1]]
alpha = 0.6
beta = 0.5
epoch = 0
maxEpoch = 1

weight = [[0.2, 0.6, 0.5, 0.9],
          [0.8, 0.4, 0.7, 0.3]]

np_data = np.array(data)
np_weight = np.array(weight)

while epoch < maxEpoch:
    for x in np_data:
        euclidianDistance = [sum((w - x) ** 2) for w in np_weight]
        minimum = np.argmin(euclidianDistance)
        np_weight[minimum] += alpha * (x - np_weight[minimum])
        print(np_weight)
    alpha *= beta
    epoch +=1

dataTest = [[0.1, 0.2, 0.3, 0.4],
            [0.5, 0.6, 0.7, 0.8],
            [0.9, 0.10, 0.11, 0.12]]
for xTest in dataTest:
    testing = [sum((weightTesting - xTest) ** 2) for weightTesting in np_weight]
    minimumTesting = np.argmin(testing)
    print("===============Testing================")
    print(testing[minimumTesting])

