# Определить в строке те слова, в которых есть повторение первой буквы слова
s1=str(input("Input str: ")).split()
def find(str):
    result=''
    for word in str:
        firstLetter=word[0]
        for letter in word[1:]:
            if letter==firstLetter:
               result = result+''.join(word)+" "
               break
    return result 
print(find(s1))
print("=======")
# # Переставить в конец строки слова, содержащие заданный символ.
# def replaceStr(str, symbol):
#     wordsWith=[]
#     wordsWithOut=[]
#
#     for word in str:
#         if symbol in word:
#             wordsWith.append(word)
#         else:
#             wordsWithOut.append(word)
#     result=' '.join(wordsWithOut+wordsWith)
#
#     return result
#
# print(replaceStr(s1, "c"))
#
# print("=======")
# #4. Найти в строке те слова, которые являются палиндромами.
# def palindrom(str):
#     palindromList=[]
#     for word in str:
#         found=True
#         for i in range(len(word)//2):
#             if word[i]!=word[-1-i]:
#                 found=False
#                 break
#         if found:
#             palindromList.append(word)
#     result=" ".join(palindromList)
#     return result
# print(palindrom(s1))
#
# print("======")
#
# # 17. В строке поменять местами слова с четными и нечетными номерами.
#
# def func17(str):
#     for i in range(0, len(str)-1, 2):
#         str[i], str[i+1] = str[i+1], str[i]
#
#     result = " ".join(str)
#     return result
#
# print(func17(s1))
# print("============== ")
#
# # 26. Найти в строке те слова, символы которых упорядочены по убыванию.
#
# def func26(str):
#     newStr=[]
#     for word in str:
#         found=True
#         for i in range(len(word)-1):
#             if word[i]<word[i+1]:
#                 found=False
#                 break
#         if found:
#             newStr.append(word)
#     result=" ".join(newStr)
#     return result
#
# print(func26(s1))


