import matplotlib.pyplot as plt

data = __import__('stat_builder')

data.calculateDistributions('out_sinhala.txt', 'out_tamil.txt')

# Plotting letter distributions
# Filtering zero probable parameters
for key in [x for x in data.statSinhala['letterCounts'].keys()]:
    if data.statTamil['letterCounts'][key] == data.statTamil['letterCounts'][key] == 0:
        del data.statSinhala['letterCounts'][key]
        del data.statTamil['letterCounts'][key]
# Plotting letter distributions sinhala
x_letter_sin = []
y_letter_sin = []

for key, value in data.statSinhala['letterCounts'].items():
    x_letter_sin.append(key)
    y_letter_sin.append(value/float(data.statSinhala['totalLetters']))

plt.plot(y_letter_sin, color='r', label='sinhala letter distribution')
plt.xticks(range(len(x_letter_sin)), x_letter_sin)

# Plotting letter distributions tamil
x_letter_tam = []
y_letter_tam = []

for key, value in data.statTamil['letterCounts'].items():
    x_letter_tam.append(key)
    y_letter_tam.append(value/float(data.statTamil['totalLetters']))

plt.plot(y_letter_tam, color='b', label='Tamil letter distribution')
plt.plot([abs(y_letter_tam[x]-y_letter_sin[x]) for x in range(len(x_letter_tam))], color='g', label='Variation distribution')
plt.xticks(range(len(x_letter_tam)), x_letter_tam)
plt.legend(loc='upper right')


# Plotting CV distributions
# Filtering zero probable parameters
for key in [x for x in data.statSinhala['cvcvvCount']['cv'].keys()]:
    if data.statTamil['cvcvvCount']['cv'][key] == data.statTamil['cvcvvCount']['cv'][key] == 0:
        del data.statSinhala['cvcvvCount']['cv'][key]
        del data.statTamil['cvcvvCount']['cv'][key]
# Plotting CV distributions sinhala
x_cv_sin = []
y_cv_sin = []

for key, value in data.statSinhala['cvcvvCount']['cv'].items():
    x_cv_sin.append(key)
    y_cv_sin.append(value/float(data.statSinhala['cvCount']))

plt.figure()
plt.plot(y_cv_sin, color='r', label='sinhala CV distribution')
plt.xticks(range(len(x_cv_sin)), x_cv_sin)

# Plotting CV distributions tamil
x_cv_tam = []
y_cv_tam = []

for key, value in data.statTamil['cvcvvCount']['cv'].items():
    x_cv_tam.append(key)
    y_cv_tam.append(value/float(data.statTamil['cvCount']))

plt.plot(y_cv_tam, color='b', label='Tamil CV distribution')
plt.plot([abs(y_cv_tam[x]-y_cv_sin[x]) for x in range(len(x_cv_tam))], color='g', label='Variation distribution')
plt.xticks(range(len(x_cv_tam)), x_cv_tam, rotation=90, fontsize=8)
plt.legend(loc='upper right')

# Plotting CVV distributions
# Filtering zero probable parameters
for key in [x for x in data.statSinhala['cvcvvCount']['cvv'].keys()]:
    if data.statTamil['cvcvvCount']['cvv'][key] == data.statTamil['cvcvvCount']['cvv'][key] == 0:
        del data.statSinhala['cvcvvCount']['cvv'][key]
        del data.statTamil['cvcvvCount']['cvv'][key]
# Plotting CVV distributions sinhala
x_cvv_sin = []
y_cvv_sin = []

for key, value in data.statSinhala['cvcvvCount']['cvv'].items():
    x_cvv_sin.append(key)
    y_cvv_sin.append(value/float(data.statSinhala['cvvCount']))

plt.figure()
plt.plot(y_cvv_sin, color='r', label='sinhala CVV distribution')
plt.xticks(range(len(x_cvv_sin)), x_cvv_sin)

# Plotting CV distributions tamil
x_cvv_tam = []
y_cvv_tam = []

for key, value in data.statTamil['cvcvvCount']['cvv'].items():
    x_cvv_tam.append(key)
    y_cvv_tam.append(value/float(data.statTamil['cvvCount']))

plt.plot(y_cvv_tam, color='b', label='Tamil CVV distribution')
plt.plot([abs(y_cvv_tam[x]-y_cvv_sin[x]) for x in range(len(x_cvv_tam))], color='g', label='Variation distribution')
plt.xticks(range(len(x_cvv_tam)), x_cvv_tam, rotation=90, fontsize=8)
plt.legend(loc='upper right')

plt.show()