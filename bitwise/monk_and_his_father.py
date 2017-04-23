noOfTestCases = int(raw_input())
pValues = [int(raw_input()) for _ in range(noOfTestCases)]
def minimumDollar(value):
  noOfBitsSet = 0
  startMask = 1
  for _ in range(64):
    if(value & startMask == startMask):
      noOfBitsSet += 1
    startMask = startMask << 1
  print noOfBitsSet
map(minimumDollar, pValues)
