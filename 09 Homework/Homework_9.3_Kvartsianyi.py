# Завдання написати просту програмку, що конвертує текстовий рядок у послідовність сигналів азбуки Морзе.
# Тест-кейс 'SOS' -> '... --- ...'

morze = {" ": "|", "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "А": ".-", "Я": ".-.-", "Б": "-...", "Ц": "-.-.", "Х": "----", "Д": "-..", "Є": "..-..", "Е": ".", "Ф": "..-.",
         "Ґ": "--.", "Г": "....", "І": "..", "Й": ".---", "Ї": ".---.", "К": "-.-", "Л": ".-..", "М": "--", "Н": "-.", "Щ": "--.--", "О": "---", "Ч": "---.", "П": ".--.", "Ш": "--.-", "Р": ".-.", "С": "...", "Т": "-", "У": "..-", "Ю": "..--", "Ж": "...-", "В": ".--", "Ь": "-..-", "И": "-.--", "З": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----"}


def tekst_to_morze(tekst):

    tekst = str(tekst)

    tekst_list = []

    rezultat = ""

    n = 0

    for i in tekst:
        tekst_list.append(i)
        rezultat = rezultat + " " + morze.get(tekst_list[n])
        n += 1
    return rezultat


tekst = input("Введіть текст: ").upper()

print(tekst_to_morze(tekst))
