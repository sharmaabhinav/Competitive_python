arr1 = [1, 5, 11, 5]
arr2 = [1, 5, 3]
arr3 = [1, 1, 1, 1, 1]
arr4 = [2, 2, 2, 2, 4, 4, 2, 1, 1]
arr5 = [3, 3, 6]
arr6 = [1, 2, 3, 4]


def isPartitionPossible(arr):
  returnVal = False
  arr = sorted(arr)
  Sum = sum(arr, 0)

  if(Sum % 2 != 0):
    return returnVal

  halfSum = Sum / 2

  start = 0
  end = len(arr) - 1
  while(start <= end):
    halfSum  = halfSum - arr[start]
    if(halfSum == 0):
      returnVal = True
    start += 1
  return returnVal


print isPartitionPossible(arr1)
print isPartitionPossible(arr2)

print isPartitionPossible(arr3)
print isPartitionPossible(arr4)

print isPartitionPossible(arr5)

print isPartitionPossible(arr6)
#print isPartitionPossible(arr2)
#isPartitionPossible(arr3)
