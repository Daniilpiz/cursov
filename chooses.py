from functions import *
import filework as fw

def choose_1(var):
    if var == 1:
        razm = int(input("Введите количество вершин в графе:\t"))
        vai = int(input("Выберите ориентированный(ввод 1) или неориентированный граф(ввод 2)"))
        return choose_2(razm, vai)
    elif var == 2:
        return fw.matrix_from_file("matrica.txt")
    
    
def choose_2(n, vari):
    if vari ==1:
        return generate_adjacency_matrix_or(n)
    elif vari == 2:
        return generate_adjacency_matrix_neor(n)

def choose_3(vari, G):
    if vari ==1:
        fw.matrix_to_file("graf.txt", G)
    elif vari ==2:
        pass