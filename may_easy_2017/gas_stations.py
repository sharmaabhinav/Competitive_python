countOfMileStones, initalFuel = map(int, raw_input().split(" "))
drainValues = map(int, raw_input().split(" "))

noOfMileStoneCrossed = 0

while(initalFuel > 0):
  initalFuel -= drainValues[noOfMileStoneCrossed]
  noOfMileStoneCrossed += 1
print noOfMileStoneCrossed
