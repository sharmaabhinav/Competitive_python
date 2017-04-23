from operator import itemgetter, attrgetter

N, M, k = map(int, raw_input().split(" "))
vals = map(int, raw_input().split(" "))


def convertVertexToIndex(vertex):
  return vertex - 1

adjancyMat = {}
for vertexNo in range(1, N + 1):
  adjancyMat[vertexNo] = []


edges = []

for edgeNo in range(1, M + 1):
  x, y = map(int, raw_input().split(" "))
  edges.append([x, y])

for edge in edges:
  ver1, ver2 = edge[0], edge[1]
  adjancyMat[ver1].append([ ver2, vals[convertVertexToIndex(ver2)] ])
  adjancyMat[ver2].append([ ver1, vals[convertVertexToIndex(ver1)] ])

for vertex in adjancyMat:
  neighbours = sorted(adjancyMat[vertex], key=itemgetter(1, 0), reverse=True)
  if(k > len(neighbours)):
    print -1
  else:
    print neighbours[k - 1][0]

