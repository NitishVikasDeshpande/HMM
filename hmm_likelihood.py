import numpy as np
import math
import sys

def forward (A, B, P, O):
    forward_prob_matrix = np.zeros((A.shape[1], O.shape[0]))
    for state in range(0,A.shape[1]):
        forward_prob_matrix[state,0]= (P[state]) * (B[state,int(O[0])])
    for t in range(1, O.shape[0]):
        for state in range(0, A.shape[1]):
            forward_prob_matrix[state, t] = B[state,int(O[t])]* (np.dot(A[:,state:state+1].T,forward_prob_matrix[:,t-1:t]))
    forward_prob= np.sum(forward_prob_matrix[:,B.shape[1]-1:B.shape[1]],axis=0)
    return forward_prob

def main():
    state_transition_prob = "state_transition_prob.txt"
    state_transition_prob_matrix = np.loadtxt(state_transition_prob)
    emission_prob = "emission_prob.txt"
    emission_prob_matrix = np.loadtxt(emission_prob)
    initial_prob = "initial_prob.txt"
    initial_prob_sequence = np.loadtxt(initial_prob)
    observations = "observations.txt"
    observation_sequence = np.loadtxt(observations)
    likelihood = forward(state_transition_prob_matrix, emission_prob_matrix, initial_prob_sequence, observation_sequence)
    print likelihood

if __name__ == "__main__":
    main()

