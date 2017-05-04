import math

noOfTestCases = int(raw_input())

def lcm(no1, no2):
  upperLimit = min(no1, no2)
  hcf = 1
  for _ in range(1, upperLimit + 1):
    if(no1 % _ == 0 and no2 % _ == 0):
      hcf = _

  return (no1 * no2) / hcf


def smallest_target(targets):
  if(len(targets) == 1):
    return targets[0]
  lc = lcm(targets[0], targets[1])
  upperLimit = len(targets)
  for _ in range(2, upperLimit):
    lc = lcm(lc, targets[_])
  return lc



for _ in range(noOfTestCases):
  count = int(raw_input())
  targets = map(int, raw_input().split(" "))
  print smallest_target(targets)
