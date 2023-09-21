from fractions import *

farenheit = float(input("Введіть температуру в градусах Фаренгейта "))

f = Fraction((100-0), (212-32))

celsius = (farenheit - 32) * f

print(round(celsius, 2))
