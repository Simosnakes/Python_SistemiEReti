def celleLibereAdiacenti(mappa):
    diz = {}
    for i, riga in enumerate(mappa):
        for j, colonna in enumerate(riga):
            if mappa[i][j] > -1:
                diz[mappa[i][j]] = []
                if i > 0:
                    if mappa[i - 1][j] > -1:
                        diz[mappa[i][j]].append(mappa[i - 1][j])
                if i+1 < len(mappa):
                    if mappa[i + 1][j] > -1:
                        diz[mappa[i][j]].append(mappa[i + 1][j])
                if j > 0:
                    if mappa[i][j - 1] > -1:
                        diz[mappa[i][j]].append(mappa[i][j - 1])
                if j + 1 < len(riga):
                    if mappa[i][j + 1] > -1:
                        diz[mappa[i][j]].append(mappa[i][j + 1])
    return diz

def main():
    matrice = [
    [0, 1, 2, -1, 3, -1],
    [4, -1, 5, 6, -1, 7],
    [-1, 8, 9, -1, 10, -1],
    [-1, 11, -1, -1, 12, -1],
    [13, -1, -1, 14, 15, -1],
    [-1, 16, 17, 18, -1, -1]
    ]
    print(celleLibereAdiacenti(matrice))

if __name__ == "__main__":
    main()