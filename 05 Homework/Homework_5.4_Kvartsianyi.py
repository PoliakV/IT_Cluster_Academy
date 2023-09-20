#a * x^2 + b * x + c = 0 

a = float(input("Введіть a: "))

b = float(input("Введіть b: "))

c = float(input("Введіть c: "))

d = b ** 2 - 4 * a * c

if d < 0: print("У рівняння немає дійсних коренів")

if d == 0:
    x = (-b + d ** 1/2)/(2 * a)
    print("x = ", x)

if d > 0:
    x1 = (-b + d ** 1/2)/(2 * a)
    x2 = (-b - d ** 1/2)/(2 * a)
    print("x1 = ", x1, " x2 = ", x2)
