# Слово або ціла фраза, букви якої ідуть в тому ж порядку якщо їх читати зліва-направо, або справа-наліво, називається паліндромом.
# Ось дескілька прикладів:
# Was it a cat I saw
# No 'x' in Nixon
# А роза упала на лапу Азора
# Три психи пили Пилипихи спирт
# Вор Азаров
# регістр букв не враховується. Пробєли и знаки також.
# Задача цієї вправи, написати функцію, що визначає чи є фраза паліндромом чи ні (повертає bool True/False).


def check_if_palindrome(word_check):
    n = 1
    k = 0
    for i in (range(len(word_check) // 2)):
        if word_check[i] == word_check[-n]:
            k += 1
        n += 1
    if k == len(word_check) // 2:
        return True
    else:
        return False


word = input("Введіть слово або фразу: ")

word = list(word.lower())

word = [word[i] for i in range(0, len(word)) if word[i].isalpha()]

print(check_if_palindrome(word))
