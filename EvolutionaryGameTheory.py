"""
Paper link: https://plato.stanford.edu/entries/game-evolutionary/#SenFai
This code implements section 2.2 of the paper.
Ref: https://www.researchgate.net/profile/Martin_Nowak2/publication/216634494_Evolutionary_Games_and_Spatial_Chaos/links/54217b730cf274a67fea8e60/Evolutionary-Games-and-Spatial-Chaos.pdf
"""
import numpy as np
import matplotlib.pyplot as plt

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
    return  np.random.choice(2, size=(N, N), p=(0.9, 0.1))

def PrisonerDilemma(N,parameters_1,people_matrix):
    
    payoff_matrix = payoff_matrix2x2(parameters_1)
    score_matrix = np.zeros([N,N])
    for r in range(N):
        for c in range(N):
            p_strategy = people_matrix[r, c]
            for n_r in [r - 1, r, r + 1]:
                for n_c in [c - 1, c, c + 1]:
                    if (n_r == r and n_c == c) or (n_r < 0 or n_r >= N) or (n_c < 0 or n_c >= N):
                        continue
                    else:
                        neighbor = people_matrix[n_r, n_c]
                        score_matrix[r, c] += payoff_matrix[p_strategy][neighbor][0]
                        score_matrix[n_r, n_c] += payoff_matrix[p_strategy][neighbor][1]
    # update the p_strategy
    for r in range(N):
        for c in range(N):

            p_strategy = people_matrix[r, c]
            max_neighbor_score = score_matrix[r,c]
            update_strategy = people_matrix[r, c]

            for n_r in [r - 1, r, r + 1]:
                for n_c in [c - 1, c, c + 1]:
                    if (n_r == r and n_c == c) or (n_r < 0 or n_r >= N) or (n_c < 0 or n_c >= N):
                        continue
                    else:
                        neighbor = people_matrix[n_r, n_c]
                        if score_matrix[n_r,n_c] > max_neighbor_score:
                            max_neighbor_score = score_matrix[n_r,n_c]
                            update_strategy = neighbor
            people_matrix[r,c] = update_strategy
    return people_matrix

if __name__ == "__main__":
    # parameters for (T,R,P,S)
    parameters_1 = (2.8,1.1,0.1,0)
    parameters_2 = (1.2,1.1,0.1,0)
    # Population N*N
    N = 200

    people_matrix = init_people_matrix(N)
    plt.imshow(people_matrix, cmap = plt.cm.gray, vmin=0, vmax=1)
    filename = str(parameters_2) + '_' +str(0)
    plt.savefig('./img/%s.png' % filename)
    for i in range(20):
        people_matrix = PrisonerDilemma(N,parameters_2,people_matrix)
        plt.imshow(people_matrix,cmap=plt.cm.gray, vmin=0, vmax=1)
        filename = str(parameters_2) + '_' +str(i+1)
        plt.savefig('./img/%s.png' % filename)