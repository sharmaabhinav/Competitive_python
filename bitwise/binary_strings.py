noOfTestCases = int(raw_input())
def noOfWays(no):
  return no.count('1')

for _ in range(noOfTestCases):
  length = int(raw_input())
  print noOfWays(raw_input().strip())
