import math

SUM = 0
n = 0
x = float(input("Введите Х = "))
EPS = 1e-4
term = x  # Первый член ряда (n=0: x^(2*0+1) / (2*0+1)! = x/1! = x)

while abs(term) >= EPS:
    SUM += term
    n += 1
    term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)

print("СУММА =", SUM)
print("КОЛИЧЕСТВО СЛАГАЕМЫХ =", n + 1)  # Учитываем начальный член (n=0)
print("Проверка (sin(x)) =", math.sin(x))

