from functions import *

def main():
    G = choose_1(int(input("Выберите случайную генерацию графа(ввод 1) или ввод с файла(ввод 2)")))
    G_1 = G.copy()
    vari = int(input("Записать матрицу графа в файл?(1-да, 2-нет)"))
    choose_3(vari, G)

    G = matrix_to_adj_dict(G)
    for vertex, neighbors in G.items():
        print(vertex, neighbors)

    
    
    st = int(input("Введите вершину для старта:\t"))
    ed = int(input("Введите конечную вершину:\t"))

    rasstoyanie, put = deikstra(G, st, ed)

    print(f"\nпройденное расстояние {rasstoyanie}\n\nпройденный путь {put}\n")
    matrix_and_path_to_file("result.txt", G_1, put)


if __name__ == "__main__":
    main()


    """ пользовательский интерфейс
    возможность генереации матрицы
    возможность считывания с файла+
    возможность задания ориентированного и неоринтированного+

    иметь возможность сохранить граф в файл+
    возможность сохранения результата+


    показ графа

    """
