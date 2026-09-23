import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A = np.array(A)
    m, n = A.shape

    result = np.zeros((n, m))

    for i in range(m):
        for j in range(n):
            result[j][i] = A[i][j]
    return result
    
    pass
