testStr = raw_input().strip()
charmap = {}


for ch in testStr:
  if(charmap.has_key(ch) == True):
    charmap[ch] += 1
  else:
    charmap[ch] = 1
frequencies = charmap.values()
minfreq = min(frequencies)

if(frequencies.count(1) == 1):
    frequencies.remove(1)
    if(len(set(frequencies)) <= 1):
      print 'Yes'
    else:
      print 'No'
else:
  diffs = []
  minfreq = min(frequencies)
  for freq in frequencies:
    diffs.append(freq - minfreq)
  if(sum(diffs) > 1):
    print 'No'
  else:
    print 'Yes'









