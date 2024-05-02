import random
import csv

def generate_maze(width, height):
    maze = [[0] * width for _ in range(height)]  # Inizializza il labirinto con tutti i percorsi percorribili
    
    # Imposta i muri lungo il perimetro del labirinto
    for i in range(width):
        maze[0][i] = 1
        maze[height - 1][i] = 1
    for i in range(height):
        maze[i][0] = 1
        maze[i][width - 1] = 1

    # Aggiungi i muri interni
    for i in range(2, height - 2, 2):
        for j in range(2, width - 2, 2):
            maze[i][j] = 1

    # Posiziona l'inizio del percorso
    maze[1][1] = 3

    return maze

def save_maze_to_csv(maze, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in maze:
            writer.writerow(row)

def print_maze(maze):
    for row in maze:
        print(' '.join(map(str, row)))

def main():
    width = 7  # Larghezza del labirinto
    height = 7  # Altezza del labirinto

    maze = generate_maze(width, height)
    save_maze_to_csv(maze, 'maze.csv')
    print("Labirinto generato e salvato come 'maze.csv'")
    print("Labirinto:")
    print_maze(maze)

if __name__ == "__main__":
    main()
