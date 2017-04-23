noOfVertex, noOfQueries = map(int, raw_input().split(" "))
edges = []
for eno in range(1, noOfVertex):
  edges.append( map( int, raw_input().split(" ") ) )

def buildAdjancyMatrix(edges, noOfVertex):

  adjancyMat = {}

  for vertex  in range(1, noOfVertex + 1):
    adjancyMat[vertex] = []

  for edge in edges:
    ver1, ver2 = edge[0], edge[1]
    adjancyMat[ver1].append(ver2)
    adjancyMat[ver2].append(ver1)

  return adjancyMat


adjancyMat = buildAdjancyMatrix(edges, noOfVertex)


countOfNodesBelow = {}
visited = {}

def DFS(sourceVertex, adjancyMat, countOfNodesBelow, visited):
  visited[sourceVertex] = True
  cnt = 1

  for neighbour in adjancyMat[sourceVertex]:
    if(visited.has_key(neighbour) == False):
      cnt += DFS(neighbour, adjancyMat, countOfNodesBelow, visited)

  countOfNodesBelow[sourceVertex] = cnt
  return cnt

DFS(1, adjancyMat, countOfNodesBelow, visited)

for queryNo in range(1, noOfQueries + 1):
  edgeNo = int(raw_input())
  u, v = edges[edgeNo - 1]
  if(countOfNodesBelow[u] < countOfNodesBelow[v]):
    child = u
  else:
    child = v
  print (noOfVertex - countOfNodesBelow[child]) * (countOfNodesBelow[child])
