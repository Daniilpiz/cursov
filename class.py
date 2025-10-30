class AdjacencyGraph:
    def __init__(self, adj_list):
        self.adj_list = adj_list
        self.size = len(adj_list)

    def __str__(self):
        """Строковое представление графа в виде списков смежности"""
        result = "Граф (списки смежности):\n"
        for i, neighbors in enumerate(self.adj_list):
            result += f"Вершина {i}: {neighbors}\n"
        return result
    
    def identify_vertices(self, v1, v2):
        """Отождествление вершин v1 и v2"""
        if v1 == v2 or v1 >= self.size or v2 >= self.size:
            print("Ошибка: неверные номера вершин")
            return None
        
        new_adj_list = []
        
        for i in range(self.size):
            if i == v2:
                continue
                
            neighbors = []
            for neighbor in self.adj_list[i]:
                if neighbor == v2:
                    neighbors.append(v1)
                elif neighbor > v2:
                    neighbors.append(neighbor - 1)
                else:
                    neighbors.append(neighbor)
            
            # Убираем дубликаты и сортируем
            neighbors = sorted(list(set(neighbors)))
            new_adj_list.append(neighbors)
        
        # Объединяем списки смежности для v1
        v1_neighbors = set(new_adj_list[v1])
        for neighbor in self.adj_list[v2]:
            if neighbor != v2:
                adjusted_neighbor = neighbor if neighbor < v2 else neighbor - 1
                if adjusted_neighbor != v1:
                    v1_neighbors.add(adjusted_neighbor)
        
        new_adj_list[v1] = sorted(list(v1_neighbors))
        
        return AdjacencyGraph(new_adj_list)
    
    # def contract_edge(self, v1, v2):
    #     """Стягивание ребра между v1 и v2"""
    #     if v1 == v2 or v1 >= self.size or v2 >= self.size or v2 not in self.adj_list[v1]:
    #         print("Ошибка: между вершинами нет ребра или неверные номера")
    #         return None
        
    #     new_adj_list = []
        
    #     for i in range(self.size):
    #         if i == v2:
    #             continue
                
    #         neighbors = []
    #         for neighbor in self.adj_list[i]:
    #             if neighbor == v2:
    #                 neighbors.append(v1)
    #             elif neighbor > v2:
    #                 neighbors.append(neighbor - 1)
    #             else:
    #                 neighbors.append(neighbor)
            
    #         # Убираем дубликаты и сортируем
    #         neighbors = sorted(list(set(neighbors)))
    #         new_adj_list.append(neighbors)
        
    #     # Объединяем списки смежности для v1
    #     v1_neighbors = set(new_adj_list[v1])
    #     for neighbor in self.adj_list[v2]:
    #         if neighbor != v2 and neighbor != v1:
    #             adjusted_neighbor = neighbor if neighbor < v2 else neighbor - 1
    #             v1_neighbors.add(adjusted_neighbor)
        
    #     new_adj_list[v1] = sorted(list(v1_neighbors))
        
    #     return AdjacencyGraph(new_adj_list)


    def contract_edge(self, v1, v2):
    # Базовые проверки
        if v1 == v2 or v1 >= self.size or v2 >= self.size:
            print("Ошибка: неверные номера вершин")
            return None
        if v2 not in self.adj_list[v1]:
            print("Ошибка: между вершинами нет ребра")
            return None

        new_size = self.size - 1
        new_adj_list = [[] for _ in range(new_size)]  # Теперь список пустых списков

    # Создаём карту пересчёта индексов (старый → новый)
        index_map = {}
        for old_idx in range(self.size):
            if old_idx == v2:
                continue  # v2 удаляется
            index_map[old_idx] = old_idx if old_idx < v2 else old_idx - 1

    # Обрабатываем каждую вершину (кроме v2)
        for old_i in range(self.size):
            if old_i == v2:
                continue

            new_i = index_map[old_i]
            neighbors = []

        for old_neighbor in self.adj_list[old_i]:
            # Пропускаем ссылки на v2 (они будут заменены на v1)
            if old_neighbor == v2:
                mapped = index_map[v1]  # v1 в новой нумерации
            else:
                # Пересчитываем индекс соседа
                if old_neighbor not in index_map:
                    continue  # Пропускаем удалённые вершины
                mapped = index_map[old_neighbor]

            neighbors.append(mapped)

        # Убираем дубликаты, сортируем, сохраняем
        new_adj_list[new_i] = sorted(list(set(neighbors)))

    # Объединяем соседей v1 и v2
        v1_new = index_map[v1]
        v1_neighbors = set(new_adj_list[v1_new])  # Теперь безопасно: new_adj_list[v1_new] — список

        for old_neighbor in self.adj_list[v2]:
            if old_neighbor == v2 or old_neighbor == v1:
                continue

            if old_neighbor not in index_map:
                continue  # Пропускаем удалённые

            mapped = index_map[old_neighbor]
            v1_neighbors.add(mapped)

        new_adj_list[v1_new] = sorted(list(v1_neighbors))

        return AdjacencyGraph(new_adj_list)



    
    def split_vertex(self, v):
        """Расщепление вершины v"""
        if v >= self.size:
            print("Ошибка: неверный номер вершины")
            return None
        
        new_adj_list = [neighbors.copy() for neighbors in self.adj_list]
        
        # Добавляем новую вершину
        new_vertex = self.size
        new_adj_list.append([])
        
        # Связываем новую вершину с исходной
        new_adj_list[v].append(new_vertex)
        new_adj_list[new_vertex].append(v)
        
        # Переносим часть связей на новую вершину
        connections_to_move = self.adj_list[v][:len(self.adj_list[v]) // 2]
        
        for neighbor in connections_to_move:
            if neighbor != v:
                # Убираем связь у исходной вершины
                if neighbor in new_adj_list[v]:
                    new_adj_list[v].remove(neighbor)
                if v in new_adj_list[neighbor]:
                    new_adj_list[neighbor].remove(v)
                
                # Добавляем связь к новой вершине
                new_adj_list[new_vertex].append(neighbor)
                new_adj_list[neighbor].append(new_vertex)
        
        # Сортируем все списки
        for i in range(len(new_adj_list)):
            new_adj_list[i] = sorted(new_adj_list[i])
        
        return AdjacencyGraph(new_adj_list)