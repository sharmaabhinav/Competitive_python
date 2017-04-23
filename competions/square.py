import math
noOfTestCases = int(raw_input())
data = [map(int, raw_input().split(" ")) for x in range(1, noOfTestCases + 1)]


def distance(point1, point2):
  return math.sqrt( (point1[0] - point2[0]) * (point1[0] - point2[0])  + (point1[1] - point2[1]) * (point1[1] - point2[1]) )

def squareCheck(d):
  A = [d[0], d[1]]
  B = [d[2], d[3]]
  C = [d[4], d[5]]
  D = [d[6], d[7]]
  distanceAB = distance(A,B)
  distanceBC = distance(B,C)
  distanceCD = distance(C,D)
  distanceDA = distance(D,A)

  sumOfAllSides = distanceAB + distanceBC + distanceCD + distanceDA
  sideLen = sumOfAllSides / 4
  if(distanceAB == sideLen and  distanceBC == sideLen and distanceCD == sideLen and distanceDA == sideLen and distance(A,C) == distance(B, D)):
      return True
  return False


def processData(data):
  for d in data:
    if(squareCheck(d)):
      print 1
    else:
      print 0

processData(data)
