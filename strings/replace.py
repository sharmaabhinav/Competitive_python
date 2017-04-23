noOfStrings = int(raw_input())
strings = [raw_input() for x in range(1, noOfStrings + 1)]

vowels = ['a', 'i', 'e','o', 'u']

def isVowel(c):
  return contains(vowels, c)

def contains(arr, value):
  contain = False
  for a in arr:
    if(a == value):
      contain = True
  return contain

def convertString(string):
  s = ""
  for c in string:
    c = c.lower()
    if(isVowel(c) == False):
      s += "." + c
  return s

def processStrings(strings):
  for string in strings:
    print convertString(string)

processStrings(strings)
