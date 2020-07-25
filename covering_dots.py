def cover_segments(S):
    covering_dots = []
    i = 0
    n = len(S)

    while i < n:
        r = S[i][1]
        covering_dots.append(r)
        i += 1

        while i < n and r >= S[i][0]:
            i += 1
    return covering_dots


if __name__ == "__main__":

    n = int(input())
    segments = []

    for _ in range(n):
        segment = input().split()
        l, r = map(int, segment)

        segments.append((l, r))

    sorted_segments = sorted(segments, key=lambda tup: tup[1])
    covering_dots = cover_segments(sorted_segments)

    print(len(covering_dots))
    for dot in covering_dots:
        print(dot, end=' ')
