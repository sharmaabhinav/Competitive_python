noOfPieces = int(raw_input())
def noOfWays(noOfPieces):
  powerOf2 = 1
  count = 1
  for _ in range(noOfPieces):
    count *= (pow(2, powerOf2) + 1)
    powerOf2 *= 2
  return count % (pow(10, 9) + 7)

print noOfWays(noOfPieces)
