# Homework 13
# Завдання: розробити програму speller.py яка буде приймати параметри назви двох файлів. Перший файл містить текст який потрібно перевірити
#  на правопис, другий параметр назва файлу словника dictionary.txt на основі якого проводиться перевірка правопису. Перевірка повинна бути
#  регістр незалежна, приклад: meet, MEET, Meet -- вважається одним і тим самим словом. Не потрібно раховувати присвійний відмінок
#  (мається на увазі відкидати закінчення 's ), приклад her's --> her.
# В результаті роботи програми повинен створюватись файл errors.txt, який містить перелік слів (без повторень) у порядку якому вони
#  зустрічаються в тексті які відсутні в файлі словнику. приклад:

# errots.txt
# ----------------
# appple
# heandds
# ...
# yarderd

import os
import sys


def preparing_text_for_check(text_for_check):
    text = []
    text = text_for_check.read().split()
    for i in range(0, len(text), 1):
        text[i] = text[i].lower()
        t = text[i]
        pos = 0
        while pos < len(t) and t[pos].isalpha():
            pos += 1
        text[i] = t[:pos]

    return text


with open(os.path.join(sys.path[0], "shakepeare.txt"), "r", encoding='utf-8') as text_for_check:
    set_shakepeare = set(preparing_text_for_check(text_for_check))

with open(os.path.join(sys.path[0], "dictionary.txt"), "r", encoding='utf-8') as dictionary:
    set_dictionary = set(preparing_text_for_check(dictionary))

with open(os.path.join(sys.path[0], "errors.txt"), "w", encoding='utf-8') as errors:
    errors_list = list(set_shakepeare.difference(set_dictionary))
    for error in errors_list:
        errors.writelines(error + "; ")
