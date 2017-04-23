noOfrows, Q = map(int, raw_input().split(" "))
frequencies = [map(int, raw_input().split(" ")) for x in range(1, noOfrows + 1)]

def countOfCellsOfColor(params):
  snapTime = int(params[0])
  startx, starty = int(params[1])-1, int(params[2])-1
  endx, endy = int(params[3])-1, int(params[4])-1
  colorToFind = params[5]

  redCount, greenCount, blueCount = 0, 0, 0

  while(startx <= endx):
    while(starty <= endy):
        noOfTimesColorChanged = snapTime / frequencies[startx][starty]
        newColor = noOfTimesColorChanged % 3
        if(newColor == 0):
          redCount += 1
        if(newColor == 1):
          greenCount += 1
        if(newColor == 2):
          blueCount += 1


  if(colorToFind == 'R'):
    return redCount
  if(colorToFind == 'G'):
    return greenCount
  if(colorToFind == 'B'):
    return blueCount

for q in range(1, Q + 1):
  params = raw_input().split(" ")
  print countOfCellsOfColor(params)
