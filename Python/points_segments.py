import bisect
from algs.sorting.qsort3 import qsort3

def main():
    n, m = tuple(map(int, input().split()))
    A = []; B = []
    for _ in range(n):
        a, b = tuple(map(int, input().split()))
        A.append(a); B.append(b)
    dots = list(map(int, input().split()))
    qsort3(A, 0, n)
    qsort3(A, 0, n)
    for dot in dots:
        a = bisect.bisect_right(A, dot)
        b = bisect.bisect_left(B, dot)
        num_segments = a - b
        print("%d " % (num_segments), end='')
    print()

if __name__ == "__main__":
    main()
