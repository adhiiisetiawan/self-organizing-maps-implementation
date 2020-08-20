import pandas as pd
import numpy as np

iris_data = pd.read_csv('iris.csv')
atribute = iris_data.drop(columns='species')
# print(atribute.head())

alpha = 0.6
beta = 0.5
epoch = 0
maxEpoch = 100

np_data = np.array(atribute)
np_weight = np.around(np.random.uniform(low=0, high=1, size=(3,4)), 3)
# print(np_data)
# print(np_weight)

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

dataTest = [[5.1, 3.8, 1.9, 0.4],
            [7.0, 3.2, 4.7, 1.4],
            [1.1, 2.3, 1.2, 1.2],
            [9.4, 3.3, 7.5, 1.3]]

print("------------------ Testing ------------------")
cluster1 = []
cluster2 = []
cluster3 = []
for xTest in dataTest:
    testing = [sum((weightTesting - xTest) ** 2) for weightTesting in np_weight]
    print("Euclidian Distance 1:", testing[0])
    print("Euclidian Distance 2", testing[1])
    print("Euclidian Distance 3", testing[2])
    print("")
    print("--------------- Pemenang --------------")
    if testing[0] <= testing[1] and testing[0] <= testing[2]:
        print("pemenang =", testing[0], "termasuk cluster 1")
        cluster1.append(testing[0])

    elif testing[1] <= testing[0] and testing[1] <= testing[2]:
        print("pemenang =", testing[1], "termasuk cluster 2")
        cluster2.append(testing[1])
    elif testing[2] <= testing[0] and testing[2] <= testing[1]:
        print("pemenang =", testing[2], "termasuk cluster 3")
        cluster3.append(testing[2])
    print("===============================")
    print("")
    print("---------------------Hasil cluster --------------------------")
    print("cluster 1: ", cluster1)
    print("cluster 2: ", cluster2)
    print("cluster 3: ", cluster3)