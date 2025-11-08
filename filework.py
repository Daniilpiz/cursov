import numpy as np

def matrix_from_file(filename):
    return np.loadtxt(filename).tolist()


def matrix_to_file(filename, G):
    with open(filename, 'a') as filename:
        for i in range(len(G)):
            filename.write(' '.join(str(G[i]) + '\n'))
    # np.savetxt("graf.txt", np.matrix(G, dtype="int32", copy=True), fmt='%d')


def matrix_and_path_to_file(filename, G, path, path_length, t_a, t_b):
    try:
        with open(filename, 'a', encoding='utf-8') as f:

            f.write("\nМатрица смежности:\n")
            for row in G:
                f.write(' '.join(map(str, row)) + '\n')

            f.write(f"\nПуть из вершины {t_a} в вершину {t_b}\n")
                
            
            if path:
                
                f.write(f"\nКратчайший путь: {' -> '.join(map(str, path))}\n")
                f.write(f"Длина пути: {path_length}\n")
            else:
                f.write("\nПуть не найден\n")

        print(f"Матрица и путь сохранены в файл {filename}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")