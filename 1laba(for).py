import math

x = 0.61
a = 0.3
b = 0.9

r = math.sqrt(x**2 + b - b**2) * (math.sin((x + a) / x))**3

print(f"result: {r}")