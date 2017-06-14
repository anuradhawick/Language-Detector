import sys

statSinhala = {}
statTamil = {}
statTarget = {}

meanAbsoluteError = {'sinhala': 0, 'tamil': 0}

detectedLanguage = ''

cvcvvCountStatsSinhala = {'cv': {}, 'cvv': {}, 'letters': {}}
cvcvvCountStatsTamil = {'cv': {}, 'cvv': {}, 'letters': {}}
cvcvvCountStatsTarget = {'cv': {}, 'cvv': {}, 'letters': {}}
error = False
def calculateDistributions(sinhala, tamil, target):
    global cvcvvCountStatsSinhala, cvcvvCountStatsTamil, cvcvvCountStatsTarget

    with open(sinhala, 'r') as f:
        data = [line.strip() for line in f]
        totalLetters = eval(data[0].split('-')[1].strip())
        letterCounts = eval(data[1].split('-')[1].strip())
        cvCount = eval(data[2].split('-')[1].strip())
        cvvCount = eval(data[3].split('-')[1].strip())
        cvcvvCount = eval(data[4].split('-')[1].strip())

        statSinhala['totalLetters']  = totalLetters
        statSinhala['letterCounts']  = letterCounts
        statSinhala['cvCount']  = cvCount
        statSinhala['cvvCount']  = cvvCount
        statSinhala['cvcvvCount']  = cvcvvCount

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

        statTamil['totalLetters']  = totalLetters
        statTamil['letterCounts']  = letterCounts
        statTamil['cvCount']  = cvCount
        statTamil['cvvCount']  = cvvCount
        statTamil['cvcvvCount']  = cvcvvCount

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

        statTarget['totalLetters']  = totalLetters
        statTarget['letterCounts']  = letterCounts
        statTarget['cvCount']  = cvCount
        statTarget['cvvCount']  = cvvCount
        statTarget['cvcvvCount']  = cvcvvCount

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

targetStats = ''
sinhalaStats = ''
tamilStats = ''

if len(initialParams) != 4:
    print "Use python detector.py <TARGET STATS> <SINHALA STATS> <TAMIL STATS>"
    error = True
else:
    targetStats = initialParams[1]
    sinhalaStats = initialParams[2]
    tamilStats = initialParams[3]

    calculateDistributions(sinhalaStats, tamilStats, targetStats)
    calculateError()
    
    if meanAbsoluteError['sinhala'] < meanAbsoluteError['tamil']:
        print 'Language detected: SINHALA'
        print 'MAE: ' + str(meanAbsoluteError['sinhala']) + ' < ' + str(meanAbsoluteError['tamil'])
        detectedLanguage = 'SINHALA'
    elif meanAbsoluteError['sinhala'] > meanAbsoluteError['tamil']:
        print 'Language detected: TAMIL'
        print 'MAE: ' + str(meanAbsoluteError['tamil']) + ' < ' + str(meanAbsoluteError['sinhala'])
        detectedLanguage = 'TAMIL'
    else:
        error = True
        print 'Language detection failed, please provide a larger data set for training/testing'

if not error:
    print 'Was the prediction true and you need to update the stats? (Y/N) [N]'
    if raw_input() == 'Y':
        if detectedLanguage == 'SINHALA':
            # Updating sinhala stats
            statSinhala['totalLetters']  += statTarget['totalLetters']

            for key, value in statTarget['letterCounts'].iteritems():
                statSinhala['letterCounts'][key] += value

            statSinhala['cvCount']  += statTarget['cvCount']
            statSinhala['cvvCount']  += statTarget['cvvCount']
            
            for key, value in statTarget['cvcvvCount']['cv'].iteritems():
                statSinhala['cvcvvCount']['cv'][key] += value
            
            for key, value in statTarget['cvcvvCount']['cvv'].iteritems():
                statSinhala['cvcvvCount']['cvv'][key] += value
            
            with open(sinhalaStats, 'wb') as f:
                f.writelines("totalLetters- " + str(statSinhala['totalLetters']))
                f.writelines("\nletterCounts- " + str(statSinhala['letterCounts']))
                f.writelines("\ncvCount- " + str(statSinhala['cvCount']))
                f.writelines("\ncvvCount- " + str(statSinhala['cvvCount']))
                f.writelines("\ncvcvvCount- " + str(statSinhala['cvcvvCount']))

        elif detectedLanguage == 'TAMIL':
            # Updating tamil statis
            statTamil['totalLetters']  += statTarget['totalLetters']

            for key, value in statTarget['letterCounts'].iteritems():
                statTamil['letterCounts'][key] += value

            statTamil['cvCount']  += statTarget['cvCount']
            statTamil['cvvCount']  += statTarget['cvvCount']
            
            for key, value in statTarget['cvcvvCount']['cv'].iteritems():
                statTamil['cvcvvCount']['cv'][key] += value
            
            for key, value in statTarget['cvcvvCount']['cvv'].iteritems():
                statTamil['cvcvvCount']['cvv'][key] += value
            
            with open(tamilStats, 'wb') as f:
                f.writelines("totalLetters- " + str(statTamil['totalLetters']))
                f.writelines("\nletterCounts- " + str(statTamil['letterCounts']))
                f.writelines("\ncvCount- " + str(statTamil['cvCount']))
                f.writelines("\ncvvCount- " + str(statTamil['cvvCount']))
                f.writelines("\ncvcvvCount- " + str(statTamil['cvcvvCount']))
        print 'Updated the language library'
    