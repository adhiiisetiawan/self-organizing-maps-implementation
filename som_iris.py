import pandas as pd
import numpy as np

iris_data = pd.read_csv('iris.csv')
atribute = iris_data.drop(columns='species')
# print(atribute.head())

alpha = 0.6
beta = 0.5
epoch = 0
maxEpoch = 1

np_data = np.array(atribute)
np_weight = np.around(np.random.uniform(low=0, high=1, size=(3,4)), 2)
# print(np_data)
# print(weight)

while epoch < maxEpoch:
    print("------------------------- Epoch ke", epoch + 1, "--------------------------------")
    for x in np_data:
        euclidianDistance = [sum((w - x) ** 2) for w in np_weight]
        print("============= Euclidian Distance ================")
        print("")
        print(euclidianDistance)
        print("")
        print("Euclidian Distance 1:", euclidianDistance[0])
        print("Euclidian Distance 2:", euclidianDistance[1])

        print("")
        print("============= Jarak terdekat dari Euclidian Distance ==============")
        print("")
        minimum = np.argmin(euclidianDistance)
        print("pemenang = ", euclidianDistance[minimum])
        print("=========== Update Bobot ============")
        print("")
        np_weight[minimum] += alpha * (x - np_weight[minimum])
        print(np.around(np_weight, 2))
    alpha *= beta
    epoch +=1