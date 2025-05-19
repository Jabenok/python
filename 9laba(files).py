FILENAME = "file.txt"

def write():
    message=input("Input data: ")
    with open(FILENAME, "a") as file:
        file.write(message+"\n")

def read():
    with open(FILENAME, "r") as file:
        for message in file:
            print(message, end="")
        print()

def sort_sim():
    print("По возрастанию: ")
    with open(FILENAME, "r") as file:
        for str in file:
            st=str.split()
            for elem in st:
                flag=True
                for k in range(1,len(elem)):
                    if elem[k-1]>=elem[k]:
                        flag=False
                        break
                if flag:
                    print(elem)


# 22 В каждой строке файла подсчитать количество слов, которые являются записью
# вещественного числа.
def findDigit():
    count=0
    nst=1
    with open(FILENAME, "r") as file:
        for line in file:
            st=line.split()
            for word in st:
                if word.isdigit():
                    count+=1
            print(f"{nst} stroke: {count}")
            nst+=1
            count=0


while(True):
    selection=int(input("1.Запись в файл\t2.Чтение файла\t3.Поиск слов, в которых все символы упорядочены по возрастанию\t0.Выход\nВыберите действие:"))
    match selection:
        case 1:write()
        case 2: read()
        case 3: sort_sim()
        case 22: findDigit()
        case 0:break
        case _:print("error")
print("Over")



