import sys

statSinhala = {}
statTamil = {}
statTarged = {}

meanAbsoluteError = {'sinhala': 0, 'tamil': 0}

detectedLanguage = ''

cvcvvCountStatsSinhala = {'cv': {}, 'cvv': {}, 'letters': {}}
cvcvvCountStatsTamil = {'cv': {}, 'cvv': {}, 'letters': {}}
cvcvvCountStatsTarget = {'cv': {}, 'cvv': {}, 'letters': {}}

def calculateDistributions(sinhala, tamil, target):
    global cvcvvCountStatsSinhala, cvcvvCountStatsTamil, cvcvvCountStatsTarget

    with open(sinhala, 'r') as f:
        data = [line.strip() for line in f]
        totalLetters = eval(data[0].split('-')[1].strip())
        letterCounts = eval(data[1].split('-')[1].strip())
        cvCount = eval(data[2].split('-')[1].strip())
        cvvCount = eval(data[3].split('-')[1].strip())
        cvcvvCount = eval(data[4].split('-')[1].strip())

        # Updating sinhala stats
        for key, value in cvcvvCount['cv'].iteritems():
            cvcvvCountStatsSinhala['cv'][key] = float(value)/cvCount
        
        for key, value in cvcvvCount['cvv'].iteritems():
            cvcvvCountStatsSinhala['cvv'][key] = float(value)/cvvCount
        
        for key, value in letterCounts.iteritems():
            cvcvvCountStatsSinhala['letters'][key] = float(value)/totalLetters

    with open(tamil, 'r') as f:
        data = [line.strip() for line in f]
        totalLetters = eval(data[0].split('-')[1].strip())
        letterCounts = eval(data[1].split('-')[1].strip())
        cvCount = eval(data[2].split('-')[1].strip())
        cvvCount = eval(data[3].split('-')[1].strip())
        cvcvvCount = eval(data[4].split('-')[1].strip())

        # Updating tamil stats
        for key, value in cvcvvCount['cv'].iteritems():
            cvcvvCountStatsTamil['cv'][key] = float(value)/cvCount
        
        for key, value in cvcvvCount['cvv'].iteritems():
            cvcvvCountStatsTamil['cvv'][key] = float(value)/cvvCount
        
        for key, value in letterCounts.iteritems():
            cvcvvCountStatsTamil['letters'][key] = float(value)/totalLetters

    with open(target, 'r') as f:
        data = [line.strip() for line in f]
        totalLetters = eval(data[0].split('-')[1].strip())
        letterCounts = eval(data[1].split('-')[1].strip())
        cvCount = eval(data[2].split('-')[1].strip())
        cvvCount = eval(data[3].split('-')[1].strip())
        cvcvvCount = eval(data[4].split('-')[1].strip())

        # Updating target stats
        for key, value in cvcvvCount['cv'].iteritems():
            cvcvvCountStatsTarget['cv'][key] = float(value)/cvCount
        
        for key, value in cvcvvCount['cvv'].iteritems():
            cvcvvCountStatsTarget['cvv'][key] = float(value)/cvvCount
        
        for key, value in letterCounts.iteritems():
            cvcvvCountStatsTarget['letters'][key] = float(value)/totalLetters


def calculateError():
    global cvcvvCountStatsSinhala, cvcvvCountStatsTamil, cvcvvCountStatsTarget, meanAbsoluteError
    for key, value in cvcvvCountStatsTarget['cv'].iteritems():
        meanAbsoluteError['sinhala'] += abs(cvcvvCountStatsSinhala['cv'][key] - cvcvvCountStatsTarget['cv'][key])
        meanAbsoluteError['tamil'] += abs(cvcvvCountStatsTamil['cv'][key] - cvcvvCountStatsTarget['cv'][key])
    
    for key, value in cvcvvCountStatsTarget['cvv'].iteritems():
        meanAbsoluteError['sinhala'] += abs(cvcvvCountStatsSinhala['cvv'][key] - cvcvvCountStatsTarget['cvv'][key])
        meanAbsoluteError['tamil'] += abs(cvcvvCountStatsTamil['cvv'][key] - cvcvvCountStatsTarget['cvv'][key])
    
    for key, value in cvcvvCountStatsTarget['letters'].iteritems():
        meanAbsoluteError['sinhala'] += abs(cvcvvCountStatsSinhala['letters'][key] - cvcvvCountStatsTarget['letters'][key])
        meanAbsoluteError['tamil'] += abs(cvcvvCountStatsTamil['letters'][key] - cvcvvCountStatsTarget['letters'][key])


initialParams = sys.argv

if len(initialParams) != 4:
    print "Use python detector.py <TARGET STATS> <SINHALA STATS> <TAMIL STATS>"
else:
    targetStats = initialParams[1]
    sinhalaStats = initialParams[2]
    tamilStats = initialParams[3]

    calculateDistributions(sinhalaStats, tamilStats, targetStats)
    calculateError()
    
    if meanAbsoluteError['sinhala'] < meanAbsoluteError['tamil']:
        print 'Language detected: SINHALA'
        print 'MAE: ' + str(meanAbsoluteError['sinhala']) + ' < ' + str(meanAbsoluteError['tamil'])
    elif meanAbsoluteError['sinhala'] > meanAbsoluteError['tamil']:
        print 'Language detected: TAMIL'
        print 'MAE: ' + str(meanAbsoluteError['tamil']) + ' < ' + str(meanAbsoluteError['sinhala'])
    else:
        print 'Language detection failed, please provide a larger data set for training/testing'

