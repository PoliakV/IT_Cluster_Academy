# Написати функцію, що здійснює елементарне шифрування повідомлення -
# рядка шляхом заміни кожної літери сусідньою справа за абеткою. а міняється на b, q на r, і так далі.
# Слово 'vasia' буде зашифроване як 'wbtjb'


def encrypt(word="vasia"):
    word_list = list(word)
    for char in range(0, int(len(word))):
        if ord(word[char]) == 90:
            word_list[char] = chr(65)
        elif ord(word[char]) == 122:
            word_list[char] = chr(97)
        else:
            word_list[char] = chr(ord(word[char]) + 1)
    return ''.join(word_list)


if __name__ == "__main__":
    word = input("Please enter a word: ")
    print(encrypt(word))
