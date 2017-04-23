N, M, R = map(int, raw_input().split(" "))
exclusive_departments = map(int, raw_input().split(" "))

adjancyList = {}
for i in range(1, N + 1):
  adjancyList[i] = []
for i in range(1, R + 1):
  x,y = map(int, raw_input().split(" "))
  adjancyList[x].append(y)
  adjancyList[y].append(x)

def traverse(adjancyList, vertex,  visited, componentCount):
  queue = []
  queue.append(vertex)
  visited[vertex] = componentCount
  while(len(queue) != 0):
    ver = queue.pop(0)
    for v in adjancyList[ver]:
      if(visited.has_key(v) == False):
        queue.append(v)
        visited[v] = componentCount


componentCount = 1
visited = { }
for vertex in range(1, N+1):
  if(visited.has_key(vertex) == False):
    traverse(adjancyList, vertex, visited, componentCount)
    componentCount += 1


components = {}

for ver in visited.keys():
  if(components.has_key(visited[ver])):
    components[visited[ver]].append(ver)
  else:
    components[visited[ver]] = [ver]

su = 0

def intersection(arr1, arr2):
  return list(set(arr1) & set(arr2))
for root in components.keys():
  su += len(components[root]) * len(intersection(components[root], exclusive_departments))


print su




