import numpy as np

A = np.array([
    [1,2,3],
    [9,2,5],
    [7,8,9]
])
sorted_mat = np.argsort(A[1, :])
sort_A = A[:, sorted_mat]
print(A)

print(sort_A)