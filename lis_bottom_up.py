def lis_bottom_up(A: list):
    n = len(A)
    D = [None] * n
    for i in range(n):
        D[i] = 1
        for j in range(i):
            if A[i] % A[j] == 0 and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
    
    res = max(D)
    return res

def main():
    # n = int(input())
    # A = list(map(int, input().split()))
    A = [3, 6, 7, 12]
    k = lis_bottom_up(A)
    print(k)
    
if __name__ == "__main__":
    main()