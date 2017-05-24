import string
import sys

# Meta Data
data = []
vSet = ['a', 'e', 'i', 'o', 'u']
cSet = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
aphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cvCombinations = {}
cvvCombinations = {}

totalWords = 0
cvcvvCount = {'cv' : {}, 'cvv' : {}}
letterCounts = {}
cvCount = 0
cvvCount = 0


def initializeStats():
    global cSet, vSet, cvcvvCount, aphabet, letterCounts, cvCount, cvvCount

    for l in alphabet:
        letterCounts[l] = 0

    for c in cSet:
        for v1 in vSet:
            cvcvvCount['cv'][c + v1] = 0
            cvCount += 1
            for v2 in vSet:
                cvcvvCount['cvv'][c + v1 + v2] = 0
                cvvCount += 1


# Reading data and obtaining the array of data
def readData(fileName):
    print "Operation Started!!"
    global totalWords
    with open (fileName, "r") as f:
        for line in f:
            data = ' '.join([l.strip() for l in line.split()])
            # cleaning data
            data = data.translate(string.maketrans("",""), string.punctuation)
            dataArray = data.strip().split()
            for word in dataArray:
                print word
                if len(word) == 0: continue
                totalWords+=1
                word = word.lower()
                cvSet(word)
                cvvSet(word)
                letterCount(word)
    print "Operation Completed!!"
            

            # return dataArray

# Get the set if CV set for a word
def cvSet(word):
    global vSet, cSet
    for i in range(len(word)-1):
        c, v = word[i], word[i+1]
        if v in vSet and c in cSet:
            key = c + v
            if cvcvvCount['cv'].has_key(key):
                cvcvvCount['cv'][key] += 1
            else:
                cvcvvCount['cv'][key] = 1
    return True


# Get the set of CVV set for a word
def cvvSet(word):
    global vSet, cSet, cvcvvCount
    for i in range(len(word)-2):
        c, v1, v2 = word[i], word[i+1], word[i+2]
        if v1 in vSet and v2 in vSet and c in cSet:
            key = c + v1 + v2
            if cvcvvCount['cvv'].has_key(key):
                cvcvvCount['cvv'][key] += 1
            else:
                cvcvvCount['cvv'][key] = 1
    return True

# Get the letter count
def letterCount(word):
    global letterCounts
    for i in word:
        letterCounts[i] += 1
    return True

# data = readData()

initializeStats()
initialData = sys.argv
print initialData
if len(initialData) != 4:
    print "Use python detector.py <LANGUAGE DATA> <TARGET DATA>"
else:
    targetFilename = initialData[2]
    dataFilename = initialData[1]
    # Excecute algorithm
    # Write information on to a file

# for word in data:
# print data
# print cvcvvCount
# print letterCounts
