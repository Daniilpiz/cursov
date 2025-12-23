from functions import deikstra, end, matrix_to_adj_dict, start  
from chooses import choose_1, choose_3 

import filework as fw

def main():
    G = choose_1(int(input("Выберите случайную генерацию графа(ввод 1) или ввод с файла(ввод 2)")))
    G_1 = G.copy()
    # except:
    #     print("Заполните файл")
    #     return None

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
    print("\n" + "="*50)
    print("РЕАЛИЗАЦИЯ АЛГОРИТМА ДЕЙКСТРЫ".center(50))
    print("="*50 + "\n")
    
    while True:
        # Улучшенный ввод с обработкой разных вариантов
        v = input("Начать работу? (Y/Да/N/Нет): ").strip().upper()
        
        if v in ["Y", "ДА", "YES"]:
            try:
                main()
            except Exception as e:
                print(f"\n⚠️  Произошла ошибка: {e}")
                print("Попробуйте снова с другими данными.\n")
            
            # Спросить, хочет ли пользователь повторить
            while True:
                repeat = input("\nХотите выполнить еще один расчет? (Y/Да/N/Нет): ").strip().upper()
                
                if repeat in ["N", "НЕТ", "NO"]:
                    print("\n" + "="*50)
                    print("Программа завершена. Спасибо за использование!".center(50))
                    print("="*50)
                    exit()
                elif repeat in ["Y", "ДА", "YES"]:
                    print("\n" + "-"*50 + "\n")
                    break
                else:
                    print("Пожалуйста, введите 'Y'/'Да' или 'N'/'Нет'")
                    
        elif v in ["N", "НЕТ", "NO"]:
            print("\n" + "="*50)
            print("Программа завершена.".center(50))
            print("="*50)
            break
        else:
            print("❌ Пожалуйста, введите 'Y'/'Да' или 'N'/'Нет'\n")
