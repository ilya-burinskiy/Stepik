def build_min_heap(A):
    log = []
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, i, n, log)
        
    return log
        
def heapify(A, idx, n, log):
    smallest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2
    
    if left < n and A[left] < A[idx]:
        smallest = left
    if right < n and A[right] < A[smallest]:
        smallest = right
    if smallest != idx:
        log.append((A[smallest], A[idx]))
        A[idx], A[smallest] = A[smallest], A[idx]
        
        heapify(A, smallest, n, log)

    


def main():
    n = int(input())
    A = input().split()
    A = list(map(int, A))
    log = build_min_heap(A)
    
    for i, j in log:
        print(i + ' ' + j, end=' ')
    print('\n')

main()