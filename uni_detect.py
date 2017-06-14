import string
import sys
import codecs


# Reading data and obtaining the array of data
def readData(fileName):
    f = codecs.open(fileName, encoding='utf-8')
    for line in f:
        data = ' '.join([l.strip() for l in line.split()])
        # Cleaning data
        translator = str.maketrans('','',string.punctuation)
        data = data.translate(translator)
        dataArray = data.strip().split()
        for word in dataArray:
            detect(word)
            
    print('Sinhala or Tamil not present')

# Detect Sinhala or Tamil or any other language using unicode
def detect(word):
    
   # maxchar = max(word)
    if u'\u0d80' <= word <= u'\u0dff':
        print('Sinhala language detected')
        sys.exit()
    elif u'\u0b80' <= word <= u'\u0bff':
        print ('Tamil language detected')
        sys.exit()
  
    

initialParams = sys.argv
if len(initialParams) != 2:
    print ("Use python uni_detect.py <LANGUAGE DATA>")
else:
    dataFilename = initialParams[1]
    readData(dataFilename)
