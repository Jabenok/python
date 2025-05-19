import math

a = 4.32
b = 8.13
xn = -3
xk = 4
dx = 0.7
count = 0
z = 0
minZ = 0
maxZ = 0

for x in range(int((xk - xn) / dx) + 1):
    current_x = xn + x * dx
    z = (math.cbrt(pow(a, 2) - 2 * a * b + current_x)) / 5.55 + pow((a + b), 2) + math.exp(current_x)

    if z <= 0 and z < minZ:
        minZ = z
    if z > 0 and z > maxZ:
        maxZ = z

    count += 1
    if count % 2 == 0:
        print(f"{count}  значение {z}")
        print(f"{count}  значение x= {current_x}")
