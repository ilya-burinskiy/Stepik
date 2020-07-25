from dstructs.disjoint_set import DisjointSet, SetObject

if __name__ == '__main__':
    n, m = input().split()
    n = int(n); m = int(m)

    tables_sizes = list(map(int, input().split()))
    
    S = DisjointSet()
    S.make_set(tables_sizes)

    for _ in range(m):
        destination, source = input().split()
        destination = int(destination); source = int(source)

        S.union(destination - 1, source - 1)
        print(S.get_max())
        
