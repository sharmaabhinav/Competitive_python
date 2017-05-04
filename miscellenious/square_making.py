import math
noOfTestCases = int(raw_input())

def factors(n):
    limit = int(math.sqrt(n))
    factors = 0
    for i in range(1, limit+1):
        if(limit % i == 0):
            factors += 2
    if(limit * limit == n):
        factors -= 1
    return factors

for _ in range(noOfTestCases):
    n = int(raw_input())
    ans = 0
    for i in range(1, n + 1):
        ans += factors(i)
    print ans
