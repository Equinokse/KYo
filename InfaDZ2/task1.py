import numpy as np
print('Введите команду: mult, trans, rank')
b = input()

print('Выберите матрицу: 1x2, 2x1, 1x3, 3x1, 2x2, 3x3')
c = input()

print('Введите количество матриц: 1, 2')
k = input()

print('Заполните матрицу через пробел')
a = list(map(int, input().split()))

mat121 = [[0,0]] #Матрица 1х2
mat122 = [[0,0]]


mat211 = [[0],  #Матрица 2х1
[0]]
mat212 = [[0],
[0]]

mat131 = [[0,0,0]] #Матрица 1х3
mat132 = [[0,0,0]]


mat311 = [[0], #Матрица 3х1
[0],
[0]]
mat312 = [[0],
[0],
[0]]


mat221 = [[0,0], #Матрица 2х2
[0,0]]
mat222 = [[0,0], 
[0,0]]


mat331 = [[0,0,0], #Матрица 3х3
[0,0,0],
[0,0,0]]
mat332 = [[0,0,0],
[0,0,0],
[0,0,0]]

if c in '1x2':
    mat121[0][0] = a[0]
    mat121[0][1] = a[1]
    if k in '2':
        mat122[0][0] = a[2]
        mat122[0][1] = a[3]

if c in '2x1':
    mat211[0][0] = a[0]
    mat211[1][0] = a[1]
    if k in '2':
        mat212[0][0] = a[2]
        mat212[1][0] = a[3]

if c in '1x3':
    mat131[0][0] = a[0]
    mat131[0][1] = a[1]
    mat131[0][2] = a[2]
    if k in '2':
        mat132[0][0] = a[3]
        mat132[0][1] = a[4]
        mat132[0][2] = a[5]

if c in '3x1':
    mat311[0][0] = a[0]
    mat311[1][0] = a[1]
    mat311[2][0] = a[2]
    if k in '2':
        mat312[0][0] = a[3]
        mat312[1][0] = a[4]
        mat312[2][0] = a[5]

if c in '2x2':
    mat221[0][0] = a[0]
    mat221[0][1] = a[1]
    mat221[1][0] = a[2]
    mat221[1][1] = a[3]
    if k in '2x2':
        mat222[0][0] = a[4]
        mat222[0][1] = a[5]
        mat222[1][0] = a[6]
        mat222[1][1] = a[7]

if c in '3x3':
    mat331[0][0] = a[0]
    mat331[0][1] = a[1]
    mat331[0][2] = a[2]
    mat331[1][0] = a[3]
    mat331[1][1] = a[4]
    mat331[1][2] = a[5]
    mat331[2][0] = a[6]
    mat331[2][1] = a[7]
    mat331[2][2] = a[8]
    if k in '2':
        mat332[0][0] = a[9]
        mat332[0][1] = a[10]
        mat332[0][2] = a[11]
        mat332[1][0] = a[12]
        mat332[1][1] = a[13]
        mat332[1][2] = a[14]
        mat332[2][0] = a[15]
        mat332[2][1] = a[16]
        mat332[2][2] = a[17]

trans12 = [[0],[0]]
trans21 = [[0,0]]
trans13 = [[0],[0],[0]]
trans31 = [[0,0,0]]
trans22 = [[0,0],[0,0]] 
trans33 = [[0,0,0],[0,0,0],[0,0,0]]

if b in 'trans':
    if c in '1x2':
        trans12[0][0] = mat121[0][0]
        trans12[1][0] = mat121[0][1]
        print(mat121, '=>' ,trans12)
    if c in '2x1':
        trans21[0][0] = mat211[0][0]
        trans21[0][1] = mat211[1][0]
        print(mat211, '=>' ,trans21)
    if c in '1x3':
        trans13[0][0] = mat131[0][0]
        trans13[1][0] = mat131[0][1]
        trans13[2][0] = mat131[0][2]
        print(mat131, '=>' ,trans13)
    if c in '3x1':
        trans31[0][0] = mat311[0][0]
        trans31[0][1] = mat311[1][0]
        trans31[0][2] = mat311[2][0]
        print(mat311, '=>' ,trans31)
    if c in '2x2':
        trans22[0][0] = mat221[0][0]
        trans22[0][1] = mat221[1][0]
        trans22[1][0] = mat221[0][1]
        trans22[1][1] = mat221[1][1]
        print(mat221, '=>' ,trans22)
    if c in '3x3':
        trans33[0][0] = mat331[0][0]
        trans33[0][1] = mat331[1][0]
        trans33[0][2] = mat331[2][0]
        trans33[1][0] = mat331[0][1]
        trans33[1][1] = mat331[1][1]
        trans33[1][2] = mat331[2][1]
        trans33[2][0] = mat331[0][2]
        trans33[2][1] = mat331[1][2]
        trans33[2][2] = mat331[2][2]
        print(mat331, '=>' ,trans33)

if b in 'rank':
    if c in '2x2':
        print('rank 2')
    if c in '3x3':
        print('rank 2')

mult22 = [[0,0], [0, 0]]
mult33 = [[0,0,0], [0,0,0], [0,0,0]]

if b in 'mult':
    if c in '2x2':
        mult22[0][0] = (mat221[0][0]*mat222[0][0])+(mat221[0][1]*mat222[1][0])
        mult22[0][1] = (mat221[0][0]*mat222[0][1])+(mat221[0][1]*mat222[1][1])
        mult22[1][0] = (mat221[1][0]*mat222[0][0])+(mat221[1][1]*mat222[1][0])
        mult22[1][1] = (mat221[1][0]*mat222[0][1])+(mat221[1][1]*mat222[1][1])
        print(mult22)
    if c in '3x3':
        mult33[0][0] = (mat331[0][0]*mat332[0][0])+(mat331[0][1]*mat332[1][0])+(mat331[0][2]*mat332[2][0])
        mult33[0][1] = (mat331[0][0]*mat332[0][1])+(mat331[0][1]*mat332[1][1])+(mat331[0][2]*mat332[2][1])
        mult33[0][2] = (mat331[0][0]*mat332[0][2])+(mat331[0][1]*mat332[1][2])+(mat331[0][2]*mat332[2][2])
        mult33[1][0] = (mat331[1][0]*mat332[0][0])+(mat331[1][1]*mat332[1][0])+(mat331[1][2]*mat332[2][0])
        mult33[1][1] = (mat331[1][0]*mat332[0][1])+(mat331[1][1]*mat332[1][1])+(mat331[1][2]*mat332[2][1])
        mult33[1][2] = (mat331[1][0]*mat332[0][2])+(mat331[1][1]*mat332[1][2])+(mat331[1][2]*mat332[2][2])
        mult33[2][0] = (mat331[2][0]*mat332[0][0])+(mat331[2][1]*mat332[1][0])+(mat331[2][2]*mat332[2][0])
        mult33[2][1] = (mat331[2][0]*mat332[0][1])+(mat331[2][1]*mat332[1][1])+(mat331[2][2]*mat332[2][1])
        mult33[2][2] = (mat331[2][0]*mat332[0][2])+(mat331[2][1]*mat332[1][2])+(mat331[2][2]*mat332[2][2])
        print(mult33)