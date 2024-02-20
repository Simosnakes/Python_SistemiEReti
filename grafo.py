import networkx as nx
import matplotlib.pyplot as plt
def disegna_grafo(dizionario_grafo):
    # Creazione del grafo
    G = nx.Graph(dizionario_grafo)
    # Disegno del grafo
    pos = nx.spring_layout(G)  # Algoritmo per la disposizione dei nodi
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=8)
    # Mostra il grafico
    plt.show()

def mat_adiacenze(mat):
    return {i: [j for j, n in enumerate(mat[i]) if n] for i in range(len(mat))}

def main(): 
    d_adiacenze = {0:[2,3], 1:[2,4], 2:[0, 1, 3], 3:[0, 2, 4], 4:[1, 3]}

    #mat = [[0 for _ in d_adiacenze] for _ in d_adiacenze]
    mat = [[0] * len(d_adiacenze) for _ in d_adiacenze]
    for i, riga in d_adiacenze.items():
        for h in riga:
            mat[i][h] = 1
    for riga in mat:
        riga_str = [str(x) for x in riga]
        print((" ").join(riga_str))
    print(mat_adiacenze(mat))

    disegna_grafo(d_adiacenze)

if __name__ == "__main__":
    main()