N, M, Q = map(int, raw_input().split(" "))
costs = map(int, raw_input().split(" "))

pieToPersonMapping = {}
personToPieMapping = {}


for x in range(1, M + 1):
    pieToPersonMapping[x] = []
for x in range(1, N + 1):
    personToPieMapping[x] = []


def processQuery(query):
    if(query[0] == 1):
        pieToPersonMapping[query[2]].append(query[1])
        personToPieMapping[query[1]].append(query[2])
    if(query[0] == 2):
        if(len(personToPieMapping[query[1]]) != 0 ):
            pieToPersonMapping[personToPieMapping[query[1]][0]].append(query[2])
            personToPieMapping[query[2]].append(personToPieMapping[query[1]][0])
        else:
            pieToPersonMapping[personToPieMapping[query[2]][0]].append(query[1])
            personToPieMapping[query[1]].append(personToPieMapping[query[2]][0])


for q in range(1, Q + 1):
    processQuery(map(int, raw_input().split(" ")))

print pieToPersonMapping, personToPieMapping