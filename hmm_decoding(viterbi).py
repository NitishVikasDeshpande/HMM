import numpy as np
import math
import sys

def viterbi (A, B, P, O):
    viterbi_matrix = np.zeros((A.shape[1], O.shape[0]))
    back_pointer= np.zeros((A.shape[1], O.shape[0]),dtype=np.int)
    best_path = np.zeros(O.shape[0],dtype=np.int)
    for state in range(0,A.shape[1]):
        viterbi_matrix[state,0]= (P[state]) * (B[state,int(O[0])])
        back_pointer[state,0]=state
    for t in range(1, O.shape[0]):
        for state in range(0, A.shape[1]):
            viterbi_matrix[state, t] = np.max([B[state,int(O[t])]* A[q,state]*viterbi_matrix[q,t-1] for q in range(A.shape[0])])
            back_pointer[state, t] = np.argmax( [(A[q,state])*(viterbi_matrix[q,t-1]) for q in range(A.shape[0])])
    best_path[O.shape[0]-1]= np.argmax([(viterbi_matrix[q,O.shape[0]-1]) for q in range(A.shape[0])])
    back_track = best_path[-1]
    
    for x in np.arange(O.shape[0])[: : -1]:
        best_path[x]= back_track
        back_track = back_pointer[back_track, x]
        
    print best_path
    
    
def main():
    state_transition_prob = "state_transition_prob.txt"
    state_transition_prob_matrix = np.loadtxt(state_transition_prob)
    emission_prob = "emission_prob.txt"
    emission_prob_matrix = np.loadtxt(emission_prob)
    initial_prob = "initial_prob.txt"
    initial_prob_sequence = np.loadtxt(initial_prob)
    observations = "observations.txt"
    observation_sequence = np.loadtxt(observations)
    viterbi(state_transition_prob_matrix, emission_prob_matrix, initial_prob_sequence, observation_sequence)
  
if __name__ == "__main__":
    main()

