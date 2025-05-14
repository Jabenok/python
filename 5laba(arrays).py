# # Числа в массиве имеют значения 0,1,…,9. Отпечатать все пары элементов
# # массива и их индексы, находящиеся рядом и имеющие одинаковые значения, то есть пары
# # =Xi+1 в порядке возрастания.
# arr=[0,1,2,3,3,4,5,6,6,7,8,8,9]
# pairs=[]
# for i in range(len(arr)-1):
#     if arr[i]==arr[i+1]:
#         pairs.append((i, i+1, arr[i]))
#
# pairs.sort()
#
# for pair in pairs:
#     print(f"Индексы: {pair[0]} и {pair[1]}, значения: {pair[2]}")

# arr=[0,1,2,10,4,5,6,7,8,9]
#
#
# for i in range(len(arr)):
#     if arr[i]>arr[i+1]:
#         for j in range(len(arr)):
#             arr[j] *= 2
#         break
#
#
# for i in range(len(arr)):
#     print(f"{arr[i]}")

# arr=[2,3,5,12,56,43,22]
# minValue=arr[0]
# maxValue=arr[0]
#
# for num in arr:
#     if num<minValue:
#         minValue=num
#     if num>maxValue:
#         maxValue=num
#
# if arr[0]>0:
#     multiplier=pow(minValue,2)
# elif arr[0]<0:
#     multiplier=pow(maxValue,2)
#
# for i in range(len(arr)):
#     arr[i]*=multiplier
#
# for i in range(len(arr)):
#     print(f"{arr[i]}")


# Дан массив M(n). Не вводя дополнительного массива, осуществить
# циклический сдвиг на один элемент влево, т.е. новое значение Mi должно быть равно
#старому значению Mi+1, а новое значение Mn должно равняться старому значению M1.

# arr=[1,2,3,4,5,6]
# temp=arr[0]
# for i in range(len(arr)-1):
#     arr[i]= arr[i+1]
# arr[-1]=temp
# for i in range(len(arr)):
#     print(f"{arr[i]}")

#Дан массив В(40). Определить, упорядочены ли в массиве все элементы по
#невозрастанию. Если упорядочены, то найти минимальный элемент. В противном случае
#определить номера первой пары элементов, для которых выполнилось соотношение
#Вi.<Bi+1.
arr=[10,9,8,7,6,10,11,4,3,2,1]
nums=[]
ifSorted=True
for i in range(len(arr)-1):
    if arr[i]<arr[i+1]:
        ifSorted=False
        nums.append((i, i+1))
        break
    if ifSorted:
        if minValue<arr[i]:
            minValue=arr[i]
if ifSorted:
    minValue=arr[-1]
    print(f"{minValue} - minimal value")
else:
    for num in nums:
        print(f"The first pair breaks the rule: {num}")