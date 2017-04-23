noOfTestCases = int(raw_input())
def dimention_coordinates(coordinates, index):
  return [coordinate[index] for coordinate in coordinates]

def maxDiff(arr):
  return max(arr) - min(arr)

def minSquareSize(coordinates):
  x_coords = dimention_coordinates(coordinates, 0)
  y_coords = dimention_coordinates(coordinates, 1)
  max_diff_in_x = maxDiff(x_coords)
  max_diff_in_y = maxDiff(y_coords)
  return max(max_diff_in_x, max_diff_in_y)

for caseNo in range(1, noOfTestCases + 1):
  noOfPoints = int(raw_input())
  coordinates = [map(int, raw_input().split(" ")) for x in range(1, noOfPoints + 1)]
  print minSquareSize(coordinates)
