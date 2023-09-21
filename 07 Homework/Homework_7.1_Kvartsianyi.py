def ostannij(kilk, dead):
    if kilk == 1:
        number = kilk - 1
    else:
        i = 1
        number = 0
        while (i <= kilk):
            number = (number + dead) % i
            i += 1
    return number + 1


kilk = int(input("Введіть кількість солдат "))

dead = int(input("Введіть крок "))

print("Останній солдат: ", ostannij(kilk, dead))
