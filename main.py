#Integrantes
#Vicente Echegaray 
#Maximiliano pereira
import heapq

def heuristica(node, salida):
    return abs(node[0] - salida[0]) + abs(node[1] - salida[1]) # calculo dist manhattan sumando dif de sus coordenadas


def vecinos(node, grid): #uso para evaluar vecinos validos
    vecinos = []
    direccion = [(0, 1), (0, -1), (1, 0), (-1, 0)] #asumo moviminetyos horizontales y verticales

    for dir_x, dir_y in direccion:
        new_x, new_y = node[0] + dir_x, node[1] + dir_y 

        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 0: #evaluo si vecino es valido(0) y si se está dentro del laberinto
            vecinos.append((new_x, new_y))
    return vecinos

def a_star(grid, entrada, salida):
    open_list = [(0, entrada)] #almacena nodos a explorar
    g_scores = {entrada: 0} #diccionario que almacena costo g
    f_scores = {entrada: heuristica(entrada, salida)} #diccionartio que almacena f

    while open_list:
        _, pos = heapq.heappop(open_list)

        if pos == salida:
            path = []
            while pos in came_from:
                path.insert(0, pos)
                pos = came_from[pos]
            return path

        for i in vecinos(pos, grid):
            tentative_g_score = g_scores[pos] + 1

            if i not in g_scores or tentative_g_score < g_scores[i]:
                came_from[i] = pos
                g_scores[i] = tentative_g_score
                f_scores[i] = tentative_g_score + heuristica(i, salida)
                heapq.heappush(open_list, (f_scores[i], i))

    return None



#Manejo archivo .txt
lab= "input.txt"
with open(lab, "r") as f: #leo el archivo
    lab = f.readlines()

matriz = [] #creo lista de arrays que contiene matriz
# variabole lab queda con espacios y salto de linea asiq se limpia
for line in lab:
    row = [int(cell) for cell in line.strip().split()]
    matriz.append(row)

#defino posicion entrada y salida
entrada = (2, 0)
salida = (3, 4)

came_from = {}

path = a_star(matriz, entrada, salida)

if path:
    print("Recorrido encontrado:")
    for step in path:
        print(step)
else:
    print("No hay recorrido")
