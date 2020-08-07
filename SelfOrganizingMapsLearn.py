import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# import somoclu
# %matplotlib inline

data = [[1, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 0, 1, 1]]
alpha = 0.6
beta = 0.5
epoch = 0
maxEpoch = 10

weight = [[0.2, 0.6, 0.5, 0.9],
          [0.8, 0.4, 0.7, 0.3]]

np_data = np.array(data)
np_weight = np.array(weight)

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
        print(np_weight)
    alpha *= beta
    epoch +=1

dataTest = [[0.1, 0.2, 0.3, 0.4],
            [0.5, 0.6, 0.7, 0.8],
            [0.9, 0.10, 0.11, 0.12]]
print("------------------ Testing ------------------")
cluster1 = []
cluster2 = []
for xTest in dataTest:
    testing = [sum((weightTesting - xTest) ** 2) for weightTesting in np_weight]
    print("Euclidian Distance 1:", testing[0])
    print("Euclidian Distance 2", testing[1])
    print("")
    print("--------------- Pemenang --------------")
    if testing[0] <= testing[1]:
        print("pemenang =", testing[0], "termasuk cluster 1")
        cluster1.append(testing[0])

    else:
        print("pemenang =", testing[1], "termasuk cluster 2")
        cluster2.append(testing[1])
    print("===============================")
    print("")
    print("---------------------Hasil cluster --------------------------")
    print("cluster 1: ", cluster1)
    print("cluster 2: ", cluster2)
c1 = np.array(cluster1)
c2 = np.array(cluster2)
print("--------------------------------final00000000000000")
print(c1)
print(c2)

# data = np.float32(np.concatenate((cluster1, cluster2)))
# colors = ["red"] * 50
# colors.extend(["green"] * 50)
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.scatter(data[:, 0], data[:, 0], c=colors)
# labels = range(150)

# plt.scatter(c1[0], c2[0])
# plt.show()