N, M = map(int, raw_input().split())
edges = [ map(int, raw_input().split(" ")) for edgeNo in range(1, M + 1) ]
adjancyMat1 = { vertexNo : [] for vertexNo in range(1, N + 1)}
adjancyMat2 = { vertexNo : [] for vertexNo in range(1, N + 1)}

for u,v in edges:
  adjancyMat1[u].append(v)
  adjancyMat2[v].append(u)

count1 , count2 = 0,0
for key in adjancyMat1:
  if (len(adjancyMat1[key]) == 0):
    count1 += 1
for key in adjancyMat2:
  if(len(adjancyMat2[key]) == 0):
    count2 += 1

print max(count2, count1)
