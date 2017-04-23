import math
noOfTestCases = int(raw_input())
strings = []
def isPrime(n):
  if(n == 1):
    return False
  for x in range(2, int(math.sqrt(n)) + 1):
    if(n % x == 0):
      return False
  return True

magicAlphabets = [[chr(x),x] for x in range(65, 90 + 1) if isPrime(x)] + [[chr(x), x] for x in range(97, 122 + 1) if isPrime(x)]
def shiftOperation(c):
  ashii_val = ord(c)
  diffs = [abs(ashii_val - x[1]) for x in magicAlphabets]
  minDiffIndex = 0
  minDiff = diffs[0]
  start = 0
  end = len(diffs) - 1
  while(start <= end):
    if(diffs[start] < minDiff):
      minDiff = diffs[start]
      minDiffIndex = start
    start += 1
  return magicAlphabets[minDiffIndex][0]

for x in range(1, noOfTestCases + 1):
  l = int(raw_input())
  strings.append(raw_input())

def convertString(string):
  returnString = ""
  for s in string:
    returnString += shiftOperation(s)
  return returnString

def processData(strings):
  for string in strings:
    print convertString(string)

processData(strings)
