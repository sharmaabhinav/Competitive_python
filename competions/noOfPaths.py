noOfTestCases = int(raw_input())

def processTestCase(pathMatrix):
    print pathMatrix

for caseNo in range(1, noOfTestCases + 1):
    N = int(raw_input())
    pathMatrix = []
    for n in range(1, N + 1):
        pathMatrix.append(map(int, raw_input().strip().split(" ")))
    processTestCase(pathMatrix)