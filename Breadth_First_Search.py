import json
import random
from collections import deque

# carrega o arquivo
with open('walls_data.json', 'r') as file:
    maze = json.load(file)

# organizar as celulas
cells = {(cell['x'], cell['y']): cell['walls'] for cell in maze}
def get_neighbors(x, y, walls):
    """Return accessible neighbors based on walls.""" #Chat gpt tá falando barras.
    directions = {
        "cima": (x, y - 1),
        "baixo": (x, y + 1), #basicamnete as direções apresentadas.
        "esquerda": (x - 1, y),
        "direita": (x + 1, y),
    }
    neighbors = []
    for wall, (nx, ny) in directions.items():
        if not walls.get(wall, True):  # Sem uma parede, dá pra passar. É o que é possível andar.
            neighbors.append((nx, ny))
    return neighbors

def BFS (start,goal):
    """Perform BFS using lists from start to goal."""
    queue = [start]
    visitado = []
    parente = {start : None}
    while queue:
        current = queue.pop(0)  # Tira da lista o primeiro elemento
        if current == goal:     # Verifica se é o objetivo final
            break
        visitado.append(current) # Marca o atual como visitado
        # Pega os dados do bloco atual
        walls = cells.get(current, {})
        # Acha os vizinhos
        for neighbor in get_neighbors(*current, walls):
            if neighbor not in visitado and neighbor not in queue:
                queue.append(neighbor)  # Adiciona na lista
                parente[neighbor] = current  # Anda o caminho
    #constroi o caminho ideal para ser seguido
    path = []
    while goal is not None:
        path.append(goal)
        goal = parente.get(goal)
    return path[::-1]  # Faz o caminho ser o correto, pois a lista adiciona do objetivo até o inicio

start = (0, 0)  # Inicio
goal = (random.randrange(38), random.randrange(28))   # Objetivo aleatório

if goal in cells:
    path = BFS(start, goal)
    print(f"Caminho de {start} para {goal}: {path}")
else:
    print(f"O objetivo {goal} não existe.")