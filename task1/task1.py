# -*- coding: windows-1251 -*
import csv
import json

print("������� x, y:", end=' ')
st = input()
st = st.split()
x = int(st[0])
y = int(st[1])
path = '../data/example.csv'
path_2 = '../data/example.json'

# ������� ��� �������� �� csv � ������
def csv_to_array(filename):
    array_of_arrays = []
    count = 0

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)

        # # ���������� ���������
        # next(csv_reader)

        for row in csv_reader:
            array = []
            for i in row:
                array.append(i)

            array_of_arrays.append(array)

    return array_of_arrays

def json_to_array(filename):
    array_of_arrays = []

    with open(filename, 'r') as file:
        array_of_arrays = file.read()

    return array_of_arrays

print("�� csv �����:")
mas = csv_to_array(path)
print(mas[x - 1][y - 1])

print("�� json �����:")
mas = json_to_array(path)
print(mas[x - 1][y - 1])