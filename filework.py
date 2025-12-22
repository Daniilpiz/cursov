def matrix_from_file(filename):
    matrix = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Skip empty lines
                line = line.strip()
                if line:
                    # Split line by spaces and convert to integers (or floats)
                    row = [float(num) for num in line.split()]
                    matrix.append(row)
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден!")
        return None
    
    # Проверяем, не пуста ли матрица
    if not matrix:
        print("Файл пуст. Заполните файл или выберите случайную генерацию.")
        return None
    
    return matrix

def matrix_to_file(filename, G):
    with open(filename, 'a') as filename:
        for i in range(len(G)):
            filename.write(' '.join(str(G[i]) + '\n'))
        filename.write("\n")
    # np.savetxt("graf.txt", np.matrix(G, dtype="int32", copy=True), fmt='%d')


def matrix_and_path_to_file(G, path, path_length, t_a, t_b):
    vari = int(input("Выберите дописать результат в файл(1) или перезаписать в новый(2)"))

    while True:
        if vari == 1:
            try:
                with open("history.txt", 'a', encoding='utf-8') as f:

                    f.write("\nМатрица смежности:\n")
                    for row in G:
                        f.write(' '.join(map(str, row)) + '\n')

                    f.write(f"\nПуть из вершины {t_a} в вершину {t_b}\n")
                
            
                    if path:
                
                        f.write(f"\nКратчайший путь: {' -> '.join(map(str, path))}\n")
                        f.write(f"Длина пути: {path_length}\n")
                    else:
                        f.write("\nПуть не найден\n")

                print("Матрица и путь сохранены в файл history.txt")
            except Exception as e:
                print(f"Ошибка при сохранении файла: {e}")

            break
        elif vari == 2:
            try:
                    with open("last_res.txt", 'w', encoding='utf-8') as f:

                        f.write("\nМатрица смежности:\n")
                        for row in G:
                            f.write(' '.join(map(str, row)) + '\n')

                        f.write(f"\nПуть из вершины {t_a} в вершину {t_b}\n")
                
            
                        if path:
                
                            f.write(f"\nКратчайший путь: {' -> '.join(map(str, path))}\n")
                            f.write(f"Длина пути: {path_length}\n")
                        else:
                            f.write("\nПуть не найден\n")

                    print("Матрица и путь сохранены в файл last_res.txt")
            except Exception as e:
                    print(f"Ошибка при сохранении файла: {e}")
            break
        else: print("Введите 1 или 2!!!")