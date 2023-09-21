import math

a, b = input("Введіть невід'ємні дійсні числа a і b, b не може дорівнювати 0: ").split()

a = float(a)

b = float(b)

x = math.sqrt(a * b) / (math.exp(a) * b) + a * math.exp(2 * a / b)

print(x)
