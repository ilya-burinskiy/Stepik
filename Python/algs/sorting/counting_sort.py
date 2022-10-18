import random

def counting_sort(A, m=10):
    n = len(A)
    B = {i: 0 for i in range(1, m+1)}
    for j in range(1, n+1):
        B[A[j]] += 1

    for i in range(2, m+1):
        B[i] = B[i] + B[i - 1]

    C = {i: 0 for i in range(1, n+1)}
    for j in range(n, 0, -1):
        C[B[A[j]]] = A[j]
        B[A[j]] = B[A[j]] - 1

    return C