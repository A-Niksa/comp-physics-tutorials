# defining the average calculator function:
def calculate_neighboring_nodes_average(nodes_matrix, i, j):
    return (nodes_matrix[i, j-1] + nodes_matrix[i, j+1] + nodes_matrix[i-1, j] + nodes_matrix[i+1, j]) / 4
