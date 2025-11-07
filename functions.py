import heapq
import numpy as np
import random as rd

def generate_adjacency_matrix_neor(n, density=0.3, weight_range=(0, 100)):
    matrix = np.array([[0 for _ in range(n)] for _ in range(n)]).reshape(n, n)
    
    for i in range(n):
        for j in range(n):
            if i != j:  # без петель
                if rd.random() < density:
                    weight = rd.randint(weight_range[0], weight_range[1])
                    matrix[i][j] = weight
                    matrix[j][i] = weight
    print(matrix)
    return matrix.tolist()


def generate_adjacency_matrix_or(n, density=0.3, weight_range=(0, 100)):
    matrix = np.array([[0 for _ in range(n)] for _ in range(n)]).reshape(n, n)
    
    for i in range(n):
        for j in range(n):
            if i != j:  # без петель
                if rd.random() < density:
                    weight = rd.randint(weight_range[0], weight_range[1])
                    matrix[i][j] = weight
    print(matrix)
    return matrix.tolist()


def matrix_from_file(filename):
    return np.loadtxt(filename).tolist()

def matrix_to_file(filename, G):
    with open(filename, 'a') as filename:
        for i in range(len(G)):
            filename.write(' '.join(str(G[i]) + '\n'))
    # np.savetxt("graf.txt", np.matrix(G, dtype="int32", copy=True), fmt='%d')


def matrix_and_path_to_file(filename, G, path):
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write("Матрица смежности:\n")
            for row in G:
                f.write(' '.join(map(str, row)) + '\n')
            
            if path:
                f.write(f"\nКратчайший путь: {' -> '.join(map(str, path))}\n")
                # Вычисляем длину пути
                path_length = 0
                for i in range(len(path) - 1):
                    path_length += G[path[i]][path[i+1]]
                f.write(f"Длина пути: {path_length}\n")
            else:
                f.write("\nПуть не найден\n")
        print(f"Матрица и путь сохранены в файл {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")

def matrix_to_adj_dict(matrix):
    n = len(matrix)
    graph = {}
    
    for i in range(n):
        graph[i] = {}  # инициализируем словарь для вершины i
        for j in range(n):
            weight = matrix[i][j]
            if weight != 0:  # ребро существует
                graph[i][j] = weight
    
    return graph


def deikstra(graph, start, end):
    # Инициализация
    distances = {vertex: float('inf') for vertex in graph}
    previous = {vertex: None for vertex in graph}  # для восстановления пути
    distances[start] = 0
    pq = [(0, start)]  # (расстояние, вершина)
    
    while pq:
        current_dist, current_vertex = heapq.heappop(pq)
        
        # Пропускаем, если нашли лучший путь ранее
        if current_dist > distances[current_vertex]:
            continue
            
        # Если достигли цели — можно досрочно завершить
        if current_vertex == end:
            break
            
        # Проверяем соседей
        for neighbor, weight in graph.get(current_vertex, {}).items():
            distance = current_dist + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
    
    # Восстанавливаем путь
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()
    
    # Если путь не найден (недостижима или нет пути)
    if path[0] != start:
        return float('inf'), []
    
    return distances[end], path


def choose_1(var):
    if var == 1:
        razm = int(input("Введите количество вершин в графе:\t"))
        vai = int(input("Выберите ориентированный(ввод 1) или неориентированный граф(ввод 2)"))
        return choose_2(razm, vai)
    if var == 2:
        return matrix_from_file("matrica.txt")
    
def choose_2(n, vari):
    if vari ==1:
        return generate_adjacency_matrix_or(n)
    if vari == 2:
        return generate_adjacency_matrix_neor(n)

def choose_3(vari, G):
    if vari ==1:
        matrix_to_file("graf.txt", G)
    if vari ==2:
        pass