def bin_search(A, key):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (high - low) // 2
        if A[mid] == key:
            return mid + 1
        elif A[mid] < key:
            high = mid - 1
        elif A[mid] > key:
            low = mid + 1
        else:
            return -1


if __name__ == "__main__":
    n, *A = map(int, input().split())
    k, *keys = map(int, input().split())

    for key in keys:
        idx = bin_search(A, key)
        if idx is None:
            idx = -1
        print(idx, end=' ')
