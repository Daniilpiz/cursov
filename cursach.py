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


def dijkstra(graph, start):
    # Инициализация расстояний
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Очередь с приоритетом
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Если найден более короткий путь, пропускаем
        if current_distance > distances[current_node]:
            continue
            
        # Обход соседей
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Если найден более короткий путь до соседа
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def shortest_path(graph, start, end):
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


def main():
    razm = int(input("Введитек количество вершин в графе:\t"))
    

    G = generate_adjacency_matrix(razm, density=0.4, weight_range=(0, 100))


    G = matrix_to_adj_dict(G)
    print(G)

    st = int(input("Введите вершину для старта:\t"))
    ed = int(input("Введите конечную вершину:\t"))

    # print(dijkstra(G, st))

    rasstoyanie, put = shortest_path(G, st, ed)

    print(rasstoyanie)
    print(put)


if __name__ == "__main__":
    main()