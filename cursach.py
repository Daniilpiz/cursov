from functions import *
from chooses import *

#filework - fw

def main():
    G = choose_1(int(input("Выберите случайную генерацию графа(ввод 1) или ввод с файла(ввод 2)")))

    G_1 = G.copy()

    vari = int(input("Записать матрицу графа в файл?(1-да, 2-нет)"))
    choose_3(vari, G)

    G = matrix_to_adj_dict(G)
    for vertex, neighbors in G.items():
        print(vertex, neighbors)

    st = start()
    ed = end()
    
            
    rasstoyanie, put = deikstra(G, st, ed)

    print(f"\nпройденное расстояние {rasstoyanie}\n\nпройденный путь {put}\n")
    fw.matrix_and_path_to_file("result.txt", G_1, put, rasstoyanie, st, ed)

if __name__ == "__main__":
    print("\n\nРЕАЛИЗАЦИЯ АЛГОРИТМА ДЕЙКСТРЫ\n\n")
    v = input("Начать работу?(Y/N)")
    while True:
        if v=="Y" or v=="y":
            main()
        elif v=="N" or v =="n":
            break
        if not(v=="Y" or v=="y") and not(v=="N" or v =="n"):
            print("Введите 'Y' или 'N'\n")
#добавить возможность выхода