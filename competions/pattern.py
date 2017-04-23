noOfTestCases = int(raw_input())
data =[raw_input().split(" ") for x in range(1, noOfTestCases + 1)]

def pattern(d):
  ch , count  = d[0], int(d[1])

  for i in range(0, count - 1 + 1):
    s =  " " * i
    s += ch
    if(i != (count - 1)):
      s += " " * (2 * count - 1 - 2 - 2 * i)
      s += ch
    print s

def processTestData(data):
  for d in data:
    pattern(d)

processTestData(data)


