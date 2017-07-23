statSinhala = {}
statTamil = {}

def calculateDistributionForStats(statsFile, statsData):

    with open(statsFile, 'r') as f:
        data = [line.strip() for line in f]
        totalLetters = eval(data[0].split('-')[1].strip())
        letterCounts = eval(data[1].split('-')[1].strip())
        cvCount = eval(data[2].split('-')[1].strip())
        cvvCount = eval(data[3].split('-')[1].strip())
        cvcvvCount = eval(data[4].split('-')[1].strip())

        statsData['totalLetters']  = totalLetters
        statsData['letterCounts']  = letterCounts
        statsData['cvCount']  = cvCount
        statsData['cvvCount']  = cvvCount
        statsData['cvcvvCount']  = cvcvvCount


def calculateDistributions(sinhala, tamil):
    calculateDistributionForStats(sinhala, statSinhala)
    calculateDistributionForStats(tamil, statTamil)
