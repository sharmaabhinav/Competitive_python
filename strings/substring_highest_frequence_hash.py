hayStack = raw_input().strip()
subStrings = { }
start = 0
end = len(hayStack) - 1

while(start <= end):
  innerStart = start
  while(innerStart <= end):
    string = hayStack[start: innerStart + 1]
    if(subStrings.has_key(string)):
      subStrings[string] += 1
    else:
      subStrings[string] = 1
    innerStart += 1
  start += 1


def processSubStrings(subStringshash):
  maxProduct = -1
  for key  in subStringshash.keys():
    l = len(key) * subStringshash[key]
    if(maxProduct < l):
      maxProduct = l
  return maxProduct

print processSubStrings(subStrings)
