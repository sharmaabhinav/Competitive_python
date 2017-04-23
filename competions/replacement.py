noOfStrings = int(raw_input())
data = [raw_input() for caseNo in range(1, noOfStrings + 1)]
def isVowel(s):
    s = s.lower()
    return (s == 'a' or s == 'i' or s == 'e' or s == 'o' or s == 'u')
def replaceString(string):
    modifiedString = ""
    for s in string:
        if(isVowel(s) == True):
            modifiedString += "venturesity"
        else:
            modifiedString += s
    return modifiedString
def processTestData(data):
    for d in data:
        print replaceString(d)
processTestData(data)