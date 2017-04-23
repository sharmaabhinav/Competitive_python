from functools import reduce

countOfNo = int(raw_input())
nos = map(int, raw_input().split(" "))
product = reduce((lambda x, y: x * y), nos)

noOfQueries = int(raw_input())
queries = [[int(raw_input()), product] for q in range(1, noOfQueries + 1)]

def countOfZeros(query):
  base, product = query[0], query[1]
  noOfZeros = 0
  while(product % base == 0):
    noOfZeros += 1
    product = product / base
  return noOfZeros

answers = map(countOfZeros, queries)
for answer in answers:
  print answer
