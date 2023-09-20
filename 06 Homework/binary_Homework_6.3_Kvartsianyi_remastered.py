'''
Написати функцію, яка приймає ціле число його двійкове представлення
'''


def binary(number):
    if number == 0:
        bin = "0"
    else:
        bin = ""
        while number > 0:
            bin = str(int(number) % 2) + bin
            number = int(number) // 2
    return bin


cases = [
        ['0', 0],
        ['1', 1],
        ['101', 5],
        ['110', 6],
        ['1011', 11],
        ['1100101', 101],
        ['100100101001', 2345],
]

for i in cases:
    expected, number = i
    result = binary(number)
    assert expected == result, 'Wrong convertation.\nExpected: {}\nActual: {}'.format(
        expected, result)
