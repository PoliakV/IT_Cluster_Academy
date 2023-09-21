# Обертання строки на k символів означає операцію зсуву елементів рядка на k позицій.
# Символи, що виходять за межі рядка заходять з іншого боку по колу. Якщо k відємне, зсув здійснюється в інший бік.
# Написати функцію, яка приймає рядок і ціле число на яке здійснюється обертання. k не перевищує половини довжини рядка.
# Тест-кейси:
# 'forwhomthebelltolls', 3       результат         whomthebelltollsfor
# 'verycomplexnumber', -6    результат       numberverycomplex

def letter_shift_left(word, k):
    for i in range(k):
        temporary_list.append(word.pop(0))
    word.extend(temporary_list)
    word_after_shift = ''.join(word)

    return word_after_shift


def letter_shift_right(word, k):
    for i in range(abs(k)):
        temporary_list.insert(0, word.pop())
    temporary_list.extend(word)
    word_after_shift = ''.join(temporary_list)

    return word_after_shift


word = input("Введіть строку без пропусків: ")

k = input("Введіть число k - на скільки буде зміщення символів ")

while k == "0" or "." in k or "," in str(k) or float(k) > len(word) / 2:
    k = input("Ви ввели неправильне значення k.\nВведіть число k - на скільки буде зміщення символів ")

else:
    word = list(word)

    k = int(k)

    temporary_list = []

    print(letter_shift_left(word, k)) if k > 0 else print(letter_shift_right(word, k))
