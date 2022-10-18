import random

def partition(A, l, r):
    rnd = random.randint(l, r - 1)
    A[l], A[rnd] = A[rnd], A[l]
    p = A[l]
    j = k = l
    for i in range(l + 1, r):
        if A[i] < p:
            j = j + 1
            k = k + 1
            A[j], A[i] = A[i], A[j]
            if j < k:
                A[k], A[i] = A[i], A[k]

        elif A[i] == p:
            k = k + 1
            A[k], A[i] = A[i], A[k]

    A[l], A[j] = A[j], A[l]
    return j, k


def qsort3(A, l, r):
    if l < r:
        j, k = partition(A, l, r)
        qsort3(A, l, j)
        qsort3(A, k + 1, r)