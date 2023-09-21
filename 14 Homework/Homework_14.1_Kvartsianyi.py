# У прикладеному файлі знаходиться реальний лог веб сервера nginx за добу. Завдання обчислити сумарну кількість надісланих
#  та прийнятих байтів. Оскільки такий протокол може бути дуже великим слід застосувати способи що не потребують завантаження
# в память усього вмісту, наприклад генераторні вирази.

import os
import sys


def calculate_bytes(log_for_count):
    counter = 0
    for line in log_for_count.read().split("\n"):
        text_list = line.split(" \"", 1)
        text = "".join(text_list[0])
        # print(text)
        counter += len(text)

    return counter/8


with open(os.path.join(sys.path[0], "2017_05_07_nginx.txt"), "r", encoding='utf-8') as log_for_check:
    print("сумарну кількість надісланих та прийнятих байтів дорівнює: ", calculate_bytes(log_for_check))
