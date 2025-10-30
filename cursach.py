import heapq
import numpy as np
import random as rd

from collections import deque

def generator_smezh(razm):
    matr_sm = np.array([abs(rd.randint(-1000, 1000))%2 for _ in range(razm) for _ in range(razm)]).reshape(razm, razm)

    for i in range(razm):
        # matr_sm[i, i] = 0
        for j in range(razm):
            if i<=j:
                matr_sm[i, j] = matr_sm[j, i]


    return matr_sm.tolist()



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

# Пример использования
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

shortest_paths = dijkstra(graph, 'A')
print("Кратчайшие расстояния от A:", shortest_paths)