from queue import Queue

def readGraph():
    nodeNum = input()
    nodeNum = int(nodeNum) 
    edgeNum = nodeNum - 1

    graph = {x: [] for x in range(1, nodeNum + 1)} 
    for edge in range(edgeNum):
        edge = input()
        edge = [int(s) for s in edge.split() if s.isdigit()]
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph, nodeNum

def levelNodes(graph, nodeNum, start=1):
    levels = {l: 1 for l in range(1, nodeNum + 1)}
    visited = {i: False for i in range(1, nodeNum + 1)}
    q = Queue()
    q.put(start)

    visited[start] = True

    while not q.empty():
        parent = q.get()
        neighbours = graph[parent]
        for neighbour in neighbours:
            if visited[neighbour] == False:
                q.put(neighbour)
                levels[neighbour] = levels[parent] + 1
                visited[neighbour] = True

    return levels

graph, nodeNum = readGraph()
levels = levelNodes(graph, nodeNum)

inputLevel = input()
inputLevel = int(inputLevel)
sameLevelNum = 0

for node, level in levels.items():
    if level == inputLevel:
        sameLevelNum += 1

print(sameLevelNum) 