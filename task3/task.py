# -*- coding: windows-1251 -*
import csv
import math


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


def func(x, n):
    if x == 0:
        return 0
    ans = (x / (n - 1)) * math.log((x / (n - 1)), 2)
    return ans


def counting(table):
    summa = 0
    for i in table:
        for j in i:
            summa += func(x=int(j), n=len(table))

    return -summa


def task(csv_str):
    table = read_csv(csv_str=csv_str)
    return counting(table=table)


path = 'data/task3.csv'

task(path)