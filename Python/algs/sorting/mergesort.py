_inv_count = 0

def merge(A, start, mid, end):
    ''' [start, end) '''

    global _inv_count
    L_len = mid - start + 1
    R_len = end - mid

    L = [None] * L_len
    R = [None] * R_len

    for i in range(L_len):
        L[i] = A[start + i]
    for i in range(R_len):
        R[i] = A[mid + i - 1]

    l = r = 0
    for k in range(start, end):
        if l == len(L):
            A[k] = R[r]
            r += 1 
        elif r == len(R):
            A[k] = L[l]
            l += 1

        elif L[l] <= R[r]:
            A[k] = L[l]
            l += 1
        else:
            _inv_count += 1
            A[k] = R[r]
            r += 1


def merge_sort(A, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(A, start, mid)
        merge_sort(A, mid + 1, end)
        merge(A, start, mid, end)

def get_inv_count():
    return _inv_count
