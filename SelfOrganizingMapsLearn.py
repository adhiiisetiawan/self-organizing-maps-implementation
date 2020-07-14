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