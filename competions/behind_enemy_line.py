needleLength = int(raw_input())
hayStacklength = int(raw_input())

needle = raw_input()
hayStack = raw_input()


def prepareHash(string):
  preparedHash = { ch: 0 for ch in string}
  for ch in string:
    preparedHash[ch] += 1
  return preparedHash


needleHash = prepareHash(needle)

start, end, count  = 0, hayStacklength - needleLength, 0
while(start <= end):
  currentHash = prepareHash(hayStack[start: start + needleLength])
  if (cmp(currentHash, needleHash) == 1):
    count += 1
  start += 1

print count
