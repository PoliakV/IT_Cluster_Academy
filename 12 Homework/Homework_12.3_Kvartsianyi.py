# Нам дано рядки, що містять дужки 4 видів - круглі (), квадратні [], фігурні {} і кутові <>.
# Задача в тому, щоб перевірити чи є послідовність дужок коректною. Тобто, будь-яка відкриваюча
# дужка повинна мати закриваючу того ж типу десь далі по рядку, і крім того, пари дужок не повинні
# перетинатись, однак вони можуть бути вкладеними:
# (a+[b*c] - {d/3})         - ок
# (a+[b*c) - 17]             не ок, перетинаються
# Написати булеву функцію, що повертає True якщо дужки розставлено вірно або False інакше.
# Тест кейси
# (((a * x) + [b] * y) + c   False
# auf(zlo)men [gy<psy>] four{s}       True


def is_balanced(s):
    brackets = {"(": ")", "{": "}", "[": "]", "<": ">"}
    stack = []
    for char in s:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    return not stack


examples = ["(a+[b*c] - {d/3})", "(a+[b*c) - 17]",
            "(((a * x) + [b] * y) + c", "auf(zlo)men [gy<psy>] four{s}"]
for example in examples:
    print(example, is_balanced(example))
