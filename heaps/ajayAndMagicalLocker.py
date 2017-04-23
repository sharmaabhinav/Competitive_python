noOfTestCases = int(raw_input())

def swap(elements, index1, index2):
  elements[index1], elements[index2] = elements[index2], elements[index1]

def heapify(elements, index, end):
  curMax = elements[index]
  curMaxIndex = index
  leftChild = 2 * index + 1
  rightChild = 2 * index + 2
  if(leftChild <= end and curMax <= elements[leftChild]):
    curMaxIndex = leftChild
    curMax = elements[leftChild]
  if(rightChild <= end and curMax <= elements[rightChild]):
    curMaxIndex = rightChild
    curMax = elements[rightChild]
  if(curMaxIndex != index):
    swap(elements, curMaxIndex, index)
    heapify(elements, curMaxIndex, end)

def getExtremeFromHeap(elements):
  return elements[0]

def setValueInHeap(elements, index, value):
  elements[index] = value

def buildHeap(elements, N):
  start = N - 1
  while(start >= 0):
    heapify(elements, start, N-1)
    start -= 1


for caseNo in range(1, noOfTestCases + 1):
  N, M = map(int, raw_input().split(" "))
  elements = map(int, raw_input().split(" "))

  buildHeap(elements, N)

  timeStart = 1
  maxMoney = 0
  start = 0
  curMax = getExtremeFromHeap(elements)
  while(timeStart <= M and curMax != 0):
    maxMoney += curMax
    setValueInHeap(elements, 0, curMax / 2)
    heapify(elements, 0, N-1)
    curMax = getExtremeFromHeap(elements)
    timeStart += 1
  print maxMoney
