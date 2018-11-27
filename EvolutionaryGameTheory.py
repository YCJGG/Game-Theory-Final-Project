import numpy as np
import matplotlib.pyplot as plt

# parameters for (T,R,P,S)
parameters_1 = (2.8,1.1,0.1,0)

# Population N*N
N = 200

def payoff_matrix2x2(parameters_1):
    T = parameters_1[0]
    R = parameters_1[1]
    P = parameters_1[2]
    S = parameters_1[3]
    return np.array([[(R,R),(S,T)],[(T,S),(P,P)]])


def PrisonerDilemma2x2(payoff_matrix,s1,s2):
    (v1,v2) = payoff_matrix[s1,s2]

    return v1, v2


def init_people_matrix(N):
    people_matrix = np.zeros([N,N],dtype = np.int)
    for i in range(N):
        for j in range(N):
            if j < 20:
                people_matrix[i,j] = 1
    return people_matrix

def PrisonerDilemma(N):
    people_matrix = init_people_matrix(N)
    for i in range(N):
        for j in range(N):
            p = people_matrix[i,j]
            if i-1 >=0 and j-1>=0 and j+1<=N-1 and i+1<=N-1:
                neighbors = [people_matrix[i-1,j-1],people_matrix[i,j-1],people_matrix[i+1,j-1], \
                people_matrix[i-1,j],people_matrix[i+1,j],people_matrix[i-1,j+1],people_matrix[i,j+1],people_matrix[i+1,j+1]]
            elif i-1<0 and j-1>=0 and j+1<=N-1 and i+1<=N-1:
                neighbors = [people_matrix[i,j-1],people_matrix[i+1,j-1], \
                people_matrix[i+1,j],people_matrix[i,j+1],people_matrix[i+1,j+1]]
            elif i-1<0 and j-1<0 and j+1<=N-1 and i+1<=N-1:
                neighbors = [people_matrix[i+1,j],people_matrix[i,j+1],people_matrix[i+1,j+1]]
                
PrisonerDilemma(N)