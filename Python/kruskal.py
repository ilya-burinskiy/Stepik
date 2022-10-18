V, E = map(int, input().split())
edges = []

for i in range(E):
	start, end, weihgt = map(int, input().split())
	edges.append([weihgt, start, end])

edges.sort()
comp = {i: i for i in range(1, V + 1)}

answer = 0
for weihgt, start, end in edges:
	if comp[start] != comp[end]:
		answer += weihgt
		a = comp[start]
		b = comp[end]
		for i in range(1, V + 1):
			if comp[i] == b:
				comp[i] = a

print(answer)

