from functions import deikstra, end, matrix_to_adj_dict, start  
from chooses import choose_1, choose_3 

import filework as fw

def main():
    G = choose_1(int(input("Выберите случайную генерацию графа(ввод 1) или ввод с файла(ввод 2)")))
    try:
        G_1 = G.copy()
    except:
        print("Заполните файл")
        return None

    vari = int(input("Записать матрицу графа в файл?(1-да, 2-нет)"))
    choose_3(vari, G)

    G = matrix_to_adj_dict(G)
    for vertex, neighbors in G.items():
        print(vertex, neighbors)

    st = start()
    ed = end()
        
    rasstoyanie, put = deikstra(G, st, ed)

    print(f"\nпройденное расстояние {rasstoyanie}\n\nпройденный путь {put}\n")
    fw.matrix_and_path_to_file(G_1, put, rasstoyanie, st, ed)

if __name__ == "__main__":
    print("\n\nРЕАЛИЗАЦИЯ АЛГОРИТМА ДЕЙКСТРЫ\n\n")
    
    while True:
        v = input("Начать работу? (Y/N): ")
        
        if v == "Y" or v == "y":
            main()
            # Спросить, хочет ли пользователь повторить
            repeat = input("\nХотите выполнить еще один расчет? (Y/N): ")
            if repeat == "N" or repeat == "n":
                print("Программа завершена.")
                break
        elif v == "N" or v == "n":
            print("Программа завершена.")
            break
        else:
            print("Введите 'Y' или 'N'\n")
