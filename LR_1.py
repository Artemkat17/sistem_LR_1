# -*- coding: windows-1251 -*
import csv

print("������� x, y:")
x = int(input())
y = int(input())
path = 'data/Garpix_data_1 - 1.csv'
# ������� ��� �������� �� csv � ������
def csv_to_array(filename):
    array_of_arrays = []
    count = 0

    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)

        # ���������� ���������
        next(csv_reader)

        for row in csv_reader:
            array = []
            for i in row:
                array.append(i)

            array_of_arrays.append(array)

    return array_of_arrays

mas = csv_to_array(path)

print(mas[x - 1][y - 1])