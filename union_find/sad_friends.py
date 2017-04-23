noOfFriends, noOfRelationships = map(int, raw_input().split(" "))
relationships = [map(int, raw_input().split(" ")) for no in range(1, noOfRelationships + 1)]

states = [x for x in range(0, noOfFriends)]
sizes = [1 for x in range(0, noOfFriends)]

def findRoot(states, x):
  while(x != states[x]):
    x = states[x]
  return x

def union(states, x, y):
  x_root = findRoot(states, x)
  y_root = findRoot(states, y)
  if(x_root == y_root):
    return

  if(sizes[y_root] < sizes[x_root]):
    states[y_root] = states[x_root]
    sizes[x_root] += sizes[y_root]
    sizes[y_root] = 0
  else:
    states[x_root] = states[y_root]
    sizes[y_root] += sizes[x_root]
    sizes[x_root] = 0

for relationship in relationships:
  union(states, relationship[0] - 1, relationship[1] -1)

noOfWays = 1
for s in sizes:
  if(s != 0):
    noOfWays *= s

print noOfWays % (pow(10,9) + 7)
