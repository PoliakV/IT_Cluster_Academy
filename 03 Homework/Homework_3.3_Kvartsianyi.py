from fractions import *

zrist = float(input("Введіть зріст в сантиметрах "))

masa = float(input("Введіть Вашу вагу в кілограмах "))

bmi = masa / (zrist / 100) ** 2

print(round(bmi, 2))
