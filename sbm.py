import numpy as np
import random as rn

def stochastic_block_model(block_matrix, node_labels):
    """
    Returns an undirected adjaceny matrix based on block probabilities provided
    
    Parameters:
        block_matrix: square matrix indicating community-to-community edge probabilities
             Sample: [
                      [.7, .1, .05],
                      [.1, .7, .1],
                      [.05, .1, .7],
                    ]

        node_labels: list of zero-indexed community labels where each index-value 
                     pair represents a node-community pair.
             Sample: [0, 3, 0, 2, 4, 2, 1, 0, 4, 0] where node 0 is in 
                     community 0, node 1 in community 3 and so on.
             
    """
    num_communities = len(set(node_labels))
    num_nodes = len(node_labels)
    
    if not all([len(row) == len(block_matrix) for row in block_matrix]):
        raise Exception("Block matrix must be square.")
        
    if num_communities != len(block_matrix):
        raise Exception("Block matrix dimensions must match number of community labels.")
        
    adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)
    
    for node_i in range(num_nodes):
        for node_j in range(num_nodes):
            com_i = node_labels[node_i]
            com_j = node_labels[node_j]  
            cutoff = rn.random()
            if cutoff <= block_matrix[com_i][com_j]:
                adj_matrix[node_i][node_j] = 1
            if cutoff <= block_matrix[com_j][com_i]:
                adj_matrix[node_j][node_i] = 1
    return adj_matrix
