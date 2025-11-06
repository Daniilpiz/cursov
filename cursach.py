import heapq
import numpy as np
import random as rd


def generate_adjacency_matrix(n, density=0.3, weight_range=()):
    matrix = np.array([[0 for _ in range(n)] for _ in range(n)]).reshape(n, n)
    
    for i in range(n):
        for j in range(n):
            if i != j:  # без петель
                if rd.random() < density:
                    weight = rd.randint(weight_range[0], weight_range[1])
                    matrix[i][j] = weight
    print(matrix)
    return matrix.tolist()


def matrix_from_file2(filename):
    return np.loadtxt(filename).tolist()

def matrix_to_file(filename, G):
    pass

def matrix_and_path_to_file(filename, G, path):
    pass

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


def choose(var):
    if var == 1:
        razm = int(input("Введите количество вершин в графе:\t"))
        return generate_adjacency_matrix(razm, density=0.4, weight_range=(0, 100))
    if var == 2:
        return matrix_from_file2("matrica.txt")

def main():
    G = choose(int(input("Выберите случайную генерацию графа(ввод 1) или ввод с файла(ввод 2)")))


    G = matrix_to_adj_dict(G)
    for vertex, neighbors in G.items():
        print(vertex, neighbors)

    st = int(input("Введите вершину для старта:\t"))
    ed = int(input("Введите конечную вершину:\t"))

    rasstoyanie, put = deikstra(G, st, ed)

    print(f"\nпройденное расстояние {rasstoyanie}\n\nпройденный путь {put}\n")


if __name__ == "__main__":
    main()


    """ пользовательский интерфейс
    возможность генереации матрицы
    возможность считывания с файла+
    возможность задания ориентированного и неоринтированного

    иметь возможность сохранить граф в файл+
    возможность сохранения результата+


    показ графа

    """
