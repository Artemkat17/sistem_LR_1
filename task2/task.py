# -*- coding: windows-1251 -*
import csv


def read_csv(csv_str):
    array_of_arrays = []
    count = 0

    with open(csv_str, 'r') as file:
        csv_reader = csv.reader(file)

        # # Пропускаем заголовок
        # next(csv_reader)

        for row in csv_reader:
            array = []
            for i in row:
                array.append(i)

            array_of_arrays.append(array)

    return array_of_arrays


def changing(table1):
    n = int(table1[-1][-1])
    mas = []
    mas2 = []
    mas3 = [0] * n
    for i in range(n):
        mas.append([0, 0, 0, 0, 0])
        mas2.append(set())

    for i in range(len(table1) - 1, -1, -1):
        a = int(table1[i][0])
        b = int(table1[i][1])
        mas[b - 1][1] += 1
        mas[a - 1][0] += 1
        mas2[a - 1].update(mas2[b - 1])
        mas2[a - 1].add(b - 1)

    for i in range(n - 1, -1, -1):
        mas[i][2] = len(mas2[i]) - mas[i][0]
        for j in mas2[i]:
            mas[j][3] += 1

    for i in range(1, n):
        mas[i][3] -= 1

    for i in range(n):
        for j in mas2[i]:
            mas3[j] += 1

    for i in range(1, n):
        mas[i][4] = mas3.count(mas3[i]) - 1

    return mas


def write_csv(mas):
    with open('answer.csv', 'w') as file:
        spamwriter = csv.writer(file, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(len(mas)):
            spamwriter.writerow(mas[i])
        return file


def task(csv_str):
    table1 = read_csv(csv_str=csv_str)
    mas = changing(table1=table1)
    return write_csv(mas=mas)


path = 'data/task2.csv'

task(path)

