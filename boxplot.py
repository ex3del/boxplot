from random import *


# создание выборки из n эл-ов и возврат списка с элементами
def sozdanie_viborki(n):
    with open('viborka.txt', 'w', encoding='utf-8') as inpt:
        print(*[int(randint(0, 100)) for _ in range(n)], file=inpt)
    with open('viborka.txt', encoding='utf-8') as inpt:
        return list(map(int, (inpt.read()).split()))


# сортировка списка
def sortirovka(spisok):
    buf = []
    while spisok:
        for _ in range(len(spisok)):
            mini = spisok[0]
            for i in spisok:
                if i <= mini:
                    mini = i
            buf.append(mini)
            spisok.remove(mini)
    return buf


# расчет медианы
def mediana(spisok):
    if len(spisok) % 2 == 1:
        return spisok[len(spisok) // 2]
    else:
        return (spisok[len(spisok) // 2] + spisok[(len(spisok) // 2) - 1])/2


# нижняя граница ящика
def q25(spisok):
    if len(spisok) % 2 == 1:
        return print(f'Q25: {spisok[len(spisok)//4]}')
    else:
        return print(f'Q25: {mediana(spisok[:len(spisok)//2])}')


# верхняя граница ящика
def q75(spisok):
    if len(spisok) % 2 == 1:
        return print(f'Q75: {spisok[-len(spisok)//4]}')
    else:
        return print(f'Q75: {mediana(spisok[len(spisok) // 2:])}')


# данные необходимые для построения ящика с усами
def box_plot():
    razmer_viborki = int(input('Введите размер выборки: '))
    elements = sortirovka(sozdanie_viborki(razmer_viborki))
    print()
    print(f'Медиана: {mediana(elements)}')
    q25(elements)
    q75(elements)
    print(f'Конец нижнего уса: {elements[0]}\nКонец верхнего уса: {elements[-1]}')
    mat_ozhid = round(sum(elements)/len(elements), 3)
    print(f'x̅: {mat_ozhid}')
    print(f'D: {sum([(i - mat_ozhid) ** 2 for i in elements]) / (len(elements) - 1)}')


box_plot()
