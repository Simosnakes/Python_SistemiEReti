import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

anno = []
nati = []
anno1 = []
temp = []

data_file = open("./causalitaCorrelazione3.csv")
data_reader = csv.reader(data_file, delimiter=',')

data_file1 = open("./causalitaCorrelazione2.csv")
data_reader1 = csv.reader(data_file1, delimiter=',')
for row in data_reader:
    anno.append(int(row[0]))
    nati.append(int(row[1]))

for row in data_reader1:
    anno1.append(int(row[0]))
    temp.append(float(row[2]))

data_file.close()
data_file1.close()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (14, 7))

ax1.plot(anno, nati, 'red', linewidth = 2.5)
ax1.set_xlabel('Anno')
ax1.set_ylabel('Numero bambini nati\nin italia con il nome Marco')
ax1.grid()

ax2.plot(anno1, temp, 'green', linewidth = 3)
ax2.set_xlabel('Anno')
ax2.set_ylabel('emissione di co2 in\nmilioni di tonnellate')
ax2.grid()

years = range(min(anno), max(anno)+1, 1)
ax1.set_xticks(years)
ax1.set_xticklabels(years)


plt.show()