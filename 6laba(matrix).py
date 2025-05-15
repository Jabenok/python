# A = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]

# B = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20]
# ]
# C=[]
# rows_A=len(A)
# cols_A=len(A[0])

# rows_B=len(B)
# cols_B=len(B[0])

# for i in range(rows_A):
#     C.append([0]*cols_B)

# for i in range(rows_A):
#     for j in range(cols_B):
#         for k in range(cols_A):
#             print(f"C[{i}][{j}]: {C[i][j]} += A[{i}][{k}]: {A[i][k]} * {B[k][j]}: B[{k}][{j}]")
#             C[i][j]+=A[i][k]*B[k][j]
#         print(C[i][j])
#     print("---")

B=[
    [1,2,3,10],
    [4,5,6,11],
    [7,8,9,12],
    [4,4,4,4]
]

# Элементы главной диагонали 
# len(B) - Количество СТРОК, строка (в данной матрице) - [1,2,3] первая строка; [4,5,6] вторая строка
#len(B[0]) - количество СТОЛБЦОВ, т.е. количество элементов в СТРОКЕ, 3 в данном примере: 1 первый столбец; 2 второй столбец.. 4 - первый столбец во второй строке

k=len(B[0])
print("\n Элементы главной диагонали (первым способом): ", end=" ")
for i in range(len(B)):
    for j in range(len(B[0])):
        if i==j:
            print(f"{B[i][j]}", end=" ")

print("\n Элементы главной диагонали (вторым способом): ", end=" ")

#Второй вариант обработки главной диагонали
for i in range(min(len(B), len(B[0]))):
    print(B[i][i], end=" ")

#Элементы побочной диагонали
print("\n Элементы побочной диагонали:", end=" ")
for i in range(len(B)):
    print(B[i][k-i-1], end=" ")

# Элементы над главной диагональю (циклом for):
print("\n Элементы над главной диагональю (циклом for):", end=" ")
for i in range(k):
    for j in range(k):
        if i<j:
            print(f"{B[i][j]}", end=" ")

#Элементы над главной диагональю (циклом while):
print("\n Элементы над главной диагональю (циклом while):", end=" ")
l = 0
while l<k-1:
    j=l+1
    while j<k:
        print(f"{B[l][j]}", end=" ")
        j+=1
    l+=1

#элементы под главной диагональю (циклом for):
print("\n Элементы под главной диагональю (циклом for):", end=" ")
for i in range(k):
    for j in range(k):
        if i>j:
            print(f"{B[i][j]}", end=" ")

#Элементы под главной диагональную циклом while:
print("\n Элементы под главной диагональю (циклом while):", end=" ")
l=1
while l<k:
    j=0
    while j<l:
        print(f"{B[l][j]}", end=" ")
        j+=1
    l+=1



print("\n ======================== \nЗадача 7.3. Cоздать одномерный массив D(n), в который занести количество отрицательных чисел в каждом столбце матрицы A(n,m).")

A=[
    [1, -3, -3, 1],
    [2, 4, 5, 1],
    [5, -3, 6, -7]
]

n= len(A)
m=len(A[0])
d= [0]*m
for i in range(n):
    for j in range(m):
        if A[i][j]<0:
            d[j]+=1
print(f"Ответ: {d}\n")

print("========")
# Найти и отпечатать симметричную строку
# матрицы. Если такой нет, то выдать сообщение
A=[
    [1,2,0],
    [4,8,2],
    [4,5,6]
]
found = False

for row in A:
    is_symmetric=True
    for j in range(len(row) // 2):
        if row[j] != row[-1 - j]:
            is_symmetric = False
            break
        if is_symmetric:
            print(f"Symmetric row: {row}")
            found=True
if not found:
    print("Not found")

print("============")
# Найти и отпечатать строку матрицы, элементы
# которой образуют возрастающую
# последовательность.     
print("Найти и отпечатать строку матрицы, элементы которой образуют возрастающую п оследовательность")
matrix=[
    [1,2,3],
    [4,8,2],
    [4,5,6]
] 
rows=[]

for i in range(len(matrix)):
    found=True
    for j in range(len(matrix[0])-1):
        if matrix[i][j]>matrix[i][j+1]:
            found=False
            break
    if found:
        rows.append(i)

for num in rows:
    print(matrix[num])

print("======== ")

# Записать элементы каждого столбца матрицы в
# обратном порядке

matrix= [
    [9,8,7],
    [6,5,4],
    [3,2,1]
]

for i in range(len(matrix)):
    matrix[i].reverse()

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(f"{matrix[i][j]}", end=" ")
    print()