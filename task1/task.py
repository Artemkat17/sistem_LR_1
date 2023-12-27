# -*- coding: windows-1251 -*
import csv
import json

print("Введите x, y:", end=' ')
st = input()
st = st.split()
x = int(st[0])
y = int(st[1])
path = 'data/example.csv'
path_2 = 'data/example.json'


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


def json_to_array(filename):

    with open(filename, 'r') as file:
        data = json.load(file)

    arr = [data['str'][i] for i in data['str']]

    return arr


print("Из csv файла:")
mas = csv_to_array(path)
print(mas[x - 1][y - 1])

print("Из json файла:")
mas = json_to_array(path_2)
print(mas[x - 1][y - 1])