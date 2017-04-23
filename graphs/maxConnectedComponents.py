noOfVertex, noOfEdges = map(int, raw_input().split(" "))
edges = []
for eno in range(1, noOfEdges + 1):
  edges.append( map( int, raw_input().split(" ") ) )

def buildAdjancyMatrix(edges):

  adjancyMat = {}

  for vertex  in range(1, noOfVertex + 1):
    adjancyMat[vertex] = []

  for edge in edges:
    ver1, ver2 = edge[0], edge[1]
    adjancyMat[ver1].append(ver2)
    adjancyMat[ver2].append(ver1)

  return adjancyMat


adjancyMat = buildAdjancyMatrix(edges)
visited  = {}

# iterative way of graph traversal
def BFS(sourceVertex, adjancyMat, visited):
  processedQueue = []
  traversed = []
  processedQueue.append(sourceVertex)
  visited[sourceVertex] = True

  while(len(processedQueue) != 0):
    ver = processedQueue.pop(0)
    traversed.append(ver)
    start = 0
    end = len(adjancyMat[ver]) - 1
    while(start <= end):
      neighbour = adjancyMat[ver][start]
      if(visited.has_key(neighbour) == False):
        visited[neighbour] = True
        processedQueue.append(neighbour)
      start += 1
  return traversed

connetedComponents = []

for vertexNo in range(1, noOfVertex + 1):
  if(visited.has_key(vertexNo) == False):
    component = BFS(vertexNo, adjancyMat, visited)
    connetedComponents.append(component)

maxEdgeCount = -1
for component in connetedComponents:
  edgeCount = 0
  for vertex  in component:
    edgeCount += len(adjancyMat[vertex])
  edgeCount /= 2
  maxEdgeCount = max(maxEdgeCount, edgeCount)

print maxEdgeCount
