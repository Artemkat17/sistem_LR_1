# -*- coding: windows-1251 -*
import csv

print("Введите x, y:", end=' ')
st = input()
x = int(st[0])
y = int(st[2])
path = 'data/example.csv'
# функция для перевода из csv в массив
def csv_to_array(filename):
    array_of_arrays = []
    count = 0

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)

        # # Пропускаем заголовок
        # next(csv_reader)

        for row in csv_reader:
            array = []
            for i in row:
                array.append(i)

            array_of_arrays.append(array)

    return array_of_arrays

mas = csv_to_array(path)

print(mas[x - 1][y - 1])