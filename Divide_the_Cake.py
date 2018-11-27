import numpy as np
import matplotlib.pyplot as plt

propotion1 = [0.0544685, 0.236312, 0.0560727, 0.0469244, 0.0562243, 0.0703294, 0.151136, 0.162231, 0.0098273, 0.111366, 0.0451093]
C = 10
iteration = 50
adder = 0
for i in range(iteration):
    W = np.zeros(C+1)
    for demand_i in range(C+1):
        for demand_j in range(C+1):
            if demand_i + demand_j <= 10:
                adder =         