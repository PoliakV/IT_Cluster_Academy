x = input("Введіть невід'ємне ціле число: ")

if x.isdigit() and int(x) > 0:
    for n in range(1, 1000, 1):
        if 2 ** n == int(x):
            print("Введене Вами число є 2 в", n, "степені")
            break

    else:
        print("Введене Вами число не є 2 в будь-якому степені, Ви ввели від'ємне число або число 0. Перезапустіть програму")

else:
    print("Введене Вами число не ціле. Перезапустіть програму")
