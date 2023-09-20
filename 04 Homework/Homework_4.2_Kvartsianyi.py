import math

x, m, b = input("Введіть дійсні числа x, m, b: ").split()

x = float(x)

m = float(m)

b = float(b)

f = 1 / (b * math.sqrt(2 * math.pi)) * math.exp(- (x-m) ** 2 / (2 * b ** 2))

print(f)
