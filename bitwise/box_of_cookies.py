noOfTestCases = int(raw_input())

def processTestCase(nos):
  bitCounts = { _ : 0 for _ in range(32)}

  for no in nos:
    start = 1
    for _ in range(32):
      if(start & no == start):
        bitCounts[_] += 1
      start = start << 1
  return max(bitCounts, key=bitCounts.get)


for caseNo in range(1, noOfTestCases + 1):
  N = int(raw_input())
  nos = [int(raw_input().strip()) for _ in range(N)]
  print processTestCase(nos)
