pathMatrix = [
    list(".BBB.B.BB"),
    list(".....B.B."),
    list("B.B.B.BSB"),
    list(".DB......")
]

S = [2,7]
path = []
visited = {}

def isInValidMove(x, y, m, n):
    return x < 0 or x > m - 1 or y < 0 or y > n - 1

def posId(x, y):
    return "#" + str(x) + "#" + str(y)

def traverse(pathMatrix, path, Sx, Sy):
    if(visited.has_key(posId(x,y) == True):
        return False

    visited[posId(x,y)] = 1

    if(isInValidMove(Sx,Sy,4,9)):
        return False
    if(pathMatrix[Sx][Sy] == 'D'):
        return True
    if(pathMatrix[Sx][Sy] == 'B'):
        return False

    isPathFromUp =  traverse(pathMatrix, path, Sx - 1, Sy)
    isPathFromDown = traverse(pathMatrix, path, Sx + 1, Sy)
    isPathFromLeft = traverse(pathMatrix, path, Sx, Sy - 1)
    isPathFromRight = traverse(pathMatrix, path, Sx, Sy + 1)

    if(isPathFromUp):
        path.append([Sx - 1, Sy])
    if(isPathFromDown):
        path.append([Sx + 1, Sy])
    if(isPathFromLeft):
        path.append([Sx, Sy - 1])
    if(isPathFromRight):
        path.append([Sx, Sy + 1])

    return isPathFromUp or isPathFromDown or isPathFromLeft or isPathFromRight

traverse(pathMatrix, path, S[0], S[1])
print path
