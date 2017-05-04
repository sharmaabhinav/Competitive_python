noOfTestCases = int(raw_input())
def minUpdateCount(nos, K):
  minUpdate = K - min(nos)
  return minUpdate if minUpdate >= 0 else 0

for _ in range(noOfTestCases):
  N, K = map(int, raw_input().split(" "))
  nos = map(int, raw_input().split(" "))
  print minUpdateCount(nos, K)

