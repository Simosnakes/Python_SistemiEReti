import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import csv

mese = []
temp =[]
giacca = []
scuola = []
mesi_n = []
gioco = []
data_file = open("./causalitaCorrelazione.csv")
data_reader = csv.reader(data_file, delimiter=',')
for row in data_reader:
    mese.append(str(row[0]))
    temp.append(float(row[1]))
    giacca.append(float(row[2]))
    scuola.append(float(row[3]))
    gioco.append(float(row[4]))
data_file.close()

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize = (12, 7))
#fig.suptitle('Media dei voti di tutte le materie e ore di studio giornaliere medie nel periodo Gennaio-Giugno')

ax1.plot(mese, temp, 'red', linewidth = 3)
ax1.set_xlabel('Mese')
ax1.set_ylabel('Temperatura \nmedia °C')
ax1.grid()

ax2.plot(mese, giacca, 'green', linewidth = 3)
ax2.set_xlabel('Mese')
ax2.set_ylabel('Mesi con \nla giacca')
ax2.grid()

ax3.plot(mese, scuola, 'blue', linewidth = 3)
ax3.set_xlabel('Mese')
ax3.set_ylabel('Giorni di scuola\n nel mese')
ax3.grid()

ax4.plot(mese, gioco, 'yellow', linewidth = 3)
ax4.set_xlabel('Mese')
ax4.set_ylabel('Giorni nei quali ho \ngiocato in un mese')
ax4.grid()
ax4.set_ylim([0, 40])

plt.show()