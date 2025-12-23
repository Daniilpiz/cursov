from functions import generate_adjacency_matrix_neor, generate_adjacency_matrix_or  
import filework as fw

def choose_1(var):
    while True:
        if var == 1:
            razm = int(input("Введите количество вершин в графе:\t"))
            vai = int(input("Выберите ориентированный(ввод 1) или неориентированный граф(ввод 2)"))
            return choose_2(razm, vai)
        elif var == 2:
            return fw.matrix_from_file("matrica.txt")
        else:
            print("Введите 1 или 2")
            break
    
    
def choose_2(n, vari):
    if vari ==1:
        return generate_adjacency_matrix_or(n)
    elif vari == 2:
        return generate_adjacency_matrix_neor(n)

def choose_3(vari, G):
    if vari ==1:
        fw.matrix_to_file("graf.txt", G)
        print("Матрица смежности записана в файл graf.txt")
    elif vari ==2:
        pass