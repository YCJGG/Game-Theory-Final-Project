import numpy as np
import matplotlib.pyplot as plt

propotion1 = [0.0544685, 0.236312, 0.0560727, 0.0469244, 0.0562243, 0.0703294, 0.151136, 0.162231, 0.0098273, 0.111366, 0.0451093]

def DivideCake(propotion1):
  C = 10
  iteration = 100
  adder = 0
  propotion = [propotion1]
  for i in range(iteration):
      W = np.zeros(C+1)
      for demand_i in range(C+1):
          for demand_j in range(C+1):
              if demand_i + demand_j <= 10:
                  adder = demand_i
              else:
                  adder = 0
              W[demand_i] += propotion1[demand_j] * adder 
      W = W * np.array(propotion1)
      W = W / np.sum(W)
      propotion1 = W
      propotion.append(W)
  legends = []
  propotion= np.array(propotion)
  plt.clf()
  for i in range(C + 1):
    #if i == 4 or i == 5 or i == 6 :
    legends.append('demand %d' % i)
    # else :
    #       pass
    plt.plot(propotion[:, i])
  plt.legend(legends)

  plt.yticks(np.arange(0, 1.2, 0.1))

  plt.show()


if __name__ == "__main__":
    
    propotion1 = [0.0544685, 0.236312, 0.0560727, 0.0469244, 0.0562243, 0.0703294, 0.151136, 0.162231, 0.0098273, 0.111366, 0.0451093] 
    DivideCake(propotion1)
    propotion2  = [0.410376, 0.107375, 0.0253916, 0.116684, 0.0813494, 0.00573677, 0.0277155, 0.0112791, 0.0163166, 0.191699, 0.00607705]
    DivideCake(propotion2)
