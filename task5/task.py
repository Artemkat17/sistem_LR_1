# -*- coding: windows-1251 -*
import json


def json_to_array(filename):
    array_of_arrays = []

    with open(filename, 'r') as file:
        array_of_arrays = json.load(file)

    return array_of_arrays


def build_matrix(mas):
    k = 0

    for i in mas:
        if type(i) == int:
            k = max(k, i)
        else:
            for j in i:
                k = max(k, j)

    ind = [0] * k
    val = 1
    for i in range(len(mas)):
        if type(mas[i]) == int:
            ind[mas[i] - 1] = val
            val += 1
        else:
            for j in range(len(mas[i])):
                ind[mas[i][j] - 1] = val
            val += 1

    ans = []
    for i in range(k):
        ans.append([0]*k)

    for i in range(k):
        for j in range(k):
            if ind[j] >= ind[i]:
                ans[i][j] = 1

    return ans


def AND_matrix(matr_A, matr_B):
    matr = []
    for i in range(len(matr_A)):
        matr.append([0]*len(matr_A[i]))

    for i in range(len(matr_A)):
        for j in range(len(matr_A[i])):
            matr[i][j] = matr_A[i][j] * matr_B[i][j]

    return matr


def transpor(matr):
    matr_new = []
    for _ in range(len(matr)):
        matr_new.append([0] * len(matr))

    for i in range(len(matr)):
        for j in range(len(matr[i])):
            matr_new[i][j] = matr[j][i]

    return matr_new


def OR_matrix(matr_A, matr_B):
    matr = []
    for i in range(len(matr_A)):
        matr.append([0]*len(matr_A[i]))

    for i in range(len(matr_A)):
        for j in range(len(matr_A[i])):
            matr[i][j] = max(matr_A[i][j], matr_B[i][j])

    return matr


def results(matr, matr_A, matr_B):
    num = {}
    mas=[]
    for i in range(len(matr)):
        if i+1 in mas:
            continue
        num[i + 1] = [i + 1]
        for j in range(i+1, len(matr)):
            if matr[i][j] == 0:
                num[i + 1].append(j + 1)
                mas.append(j+1)

    res = []
    for k in num:
        if not res:
            res.append(num[k])
            continue
        for i, elem in enumerate(res):
            if sum(matr_A[elem[0] - 1]) == sum(matr_A[k - 1]) and sum(matr_B[elem[0] - 1]) == sum(matr_B[k - 1]):
                for c in num[k]:
                    res[i].append(c)
                    break

            if sum(matr_A[elem[0] - 1]) < sum(matr_A[k - 1]) or sum(matr_B[elem[0] - 1]) < sum(matr_B[k - 1]):
                res = res[:i] + [num[k]] + res[i:]
                break
        res.append(num[k])

    fin = []
    for r in res:
        if len(r) == 1:
            fin.append(r[0])
        else:
            fin.append(r)
    return str(fin)


def task(A, B):
    mas_A = json_to_array(A)
    mas_B = json_to_array(B)

    matr_A = build_matrix(mas_A)
    matr_B = build_matrix(mas_B)

    matr_AND = AND_matrix(matr_A=matr_A, matr_B=matr_B)
    matr_AND_T = AND_matrix(matr_A=transpor(matr_A), matr_B=transpor(matr_B))

    matr_OR = OR_matrix(matr_A=matr_AND, matr_B=matr_AND_T)


    result = results(matr=matr_OR, matr_A=matr_A, matr_B=matr_B)

    print(result)


path_A = 'data/Range_A.json'
path_B = 'data/Range_B.json'

task(A=path_A, B=path_B)