import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

anno = []
temp =[]
co2 = []

data_file = open("./causalitaCorrelazione2.csv")
data_reader = csv.reader(data_file, delimiter=',')
for row in data_reader:
    anno.append(int(row[0]))
    temp.append(float(row[1]))
    co2.append(float(row[2]))

data_file.close()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (13, 7))

ax1.plot(anno, temp, 'red', linewidth = 2.5)
ax1.set_xlabel('Anno')
ax1.set_ylabel('Variazione temperatura °C')
ax1.grid()

ax2.plot(anno, co2, 'green', linewidth = 3)
ax2.set_xlabel('Anno')
ax2.set_ylabel('emissione di co2 in\nmilioni di tonnellate')
ax2.grid()

years = range(min(anno), max(anno)+1, 10)
ax1.set_xticks(years)
ax1.set_xticklabels(years)

ax2.set_xticks(years)
ax2.set_xticklabels(years)

plt.show()