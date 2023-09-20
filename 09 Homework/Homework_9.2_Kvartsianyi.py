# Написати програму що перетворює числове представлення грошової суми в суму прописом.
# Наприклад Вхід: 1234.56. Вихід: Одна тисяча двісті тридцять чотири гривні 56 копійок.
# Вхідне число не перевищує 999999.99. Така функція застосовується при формуванні платіжних
# доручень, накладних, рахунків і т. д.

units = {0: "", 1: "одна", 2: "дві", 3: "три", 4: "чотири", 5: "п'ять", 6: "шість",
         7: "сім", 8: "вісім", 9: "дев'ять"}
tens = {0: "десять", 1: "одинадцять", 2: "дванадцять", 3: "тринадцять",
        4: "чотирнадцять", 5: "п'ятнадцять", 6: "шістнадцять", 7: "сімнадцять",
        8: "вісімнадцять", 9: "дев'ятнадцять"}
twenties = {0: "", 2: "двадцять", 3: "тридцять", 4: "сорок", 5: "п'ятдесят", 6: "шістдесят",
            7: "сімдесят", 8: "вісімдесят", 9: "дев'яносто"}
hundreds = {0: "", 1: "сто", 2: "двісті", 3: "триста", 4: "чотириста", 5: "п'ятсот",
            6: "шістсот", 7: "сімсот", 8: "вісімсот", 9: "дев'ятсот"}


def nazva_kopiiky(kopiiky):
    kopiiky_list = []
    for i in kopiiky:
        kopiiky_list.append(i)
    if int(kopiiky_list[1]) >= 5 or int(kopiiky_list[1]) == 0 or int(kopiiky) >= 11 and int(kopiiky) <= 14:
        if int(kopiiky) >= 10:
            kopiiky_text = kopiiky + " копійок"
        else:
            kopiiky_text = kopiiky_list[1] + " копійок"
    elif int(kopiiky_list[1]) == 1:
        if int(kopiiky) >= 20:
            kopiiky_text = kopiiky + " копійка"
        else:
            kopiiky_text = kopiiky_list[1] + " копійка"
    elif int(kopiiky_list[1]) >= 2 or int(kopiiky_list[1]) <= 4:
        if int(kopiiky) >= 20:
            kopiiky_text = kopiiky + " копійки"
        else:
            kopiiky_text = kopiiky_list[1] + " копійки"
    return kopiiky_text


def nazva_hryvni(hryvni):
    hryvni_list = []
    for i in hryvni:
        hryvni_list.append(i)

    if len(hryvni) == 1:
        if int(hryvni_list[-1]) >= 5:
            hryvni_text = units.get(int(hryvni_list[-1])) + " гривень"
        elif int(hryvni_list[-1]) == 1:
            hryvni_text = units.get(int(hryvni_list[-1])) + " гривня"
        elif int(hryvni_list[-1]) >= 2 or int(hryvni_list[-1]) <= 4:
            hryvni_text = units.get(int(hryvni_list[-1])) + " гривні"
        elif int(hryvni_list[-1]) == 0:
            hryvni_text = "нуль гривень"

    elif len(hryvni) > 1:
        if int(hryvni_list[-1]) >= 5 or int(hryvni_list[-1]) == 0 or int(hryvni_list[-2]) == 1 and int(hryvni_list[-1]) <= 4 and int(hryvni_list[-1]) >= 1:
            hryvni_text = " гривень"
        elif int(hryvni_list[-1]) == 1:
            hryvni_text = " гривня"
        elif int(hryvni_list[-1]) >= 2 or int(hryvni_list[-1]) <= 4:
            hryvni_text = " гривні"

        if int(hryvni_list[-2]) != 1:
            if int(hryvni_list[-2]) == 0:
                hryvni_text = twenties.get(
                    int(hryvni_list[-2])) + units.get(int(hryvni_list[-1])) + hryvni_text
            else:
                hryvni_text = twenties.get(
                    int(hryvni_list[-2])) + " " + units.get(int(hryvni_list[-1])) + hryvni_text
        else:
            hryvni_text = tens.get(int(hryvni_list[-1])) + hryvni_text

    if len(hryvni) > 2:
        if int(hryvni_list[-3]) == 0:
            hryvni_text = hundreds.get(int(hryvni_list[-3])) + hryvni_text
        else:
            hryvni_text = hundreds.get(
                int(hryvni_list[-3])) + " " + hryvni_text

    if len(hryvni) == 4:
        if int(hryvni_list[-4]) >= 5:
            hryvni_text = units.get(
                int(hryvni_list[-4])) + " тисяч " + hryvni_text
        elif int(hryvni_list[-4]) == 1:
            hryvni_text = units.get(
                int(hryvni_list[-4])) + " тисяча " + hryvni_text
        elif int(hryvni_list[-4]) >= 2 or int(hryvni_list[-4]) <= 4:
            hryvni_text = units.get(
                int(hryvni_list[-4])) + " тисячі " + hryvni_text

    if len(hryvni) > 4:
        if int(hryvni_list[-4]) >= 5 or int(hryvni_list[-4]) == 0 or int(hryvni_list[-5]) == 1 and int(hryvni_list[-4]) <= 4 and int(hryvni_list[-4]) >= 1:
            hryvni_text = " тисяч " + hryvni_text
        elif int(hryvni_list[-4]) == 1:
            hryvni_text = " тисяча " + hryvni_text
        elif int(hryvni_list[-4]) >= 2 or int(hryvni_list[-4]) <= 4:
            hryvni_text = " тисячі " + hryvni_text

        if int(hryvni_list[-5]) != 1:
            if int(hryvni_list[-4]) == 0:
                hryvni_text = twenties.get(
                    int(hryvni_list[-5])) + units.get(int(hryvni_list[-4])) + hryvni_text
            else:
                hryvni_text = twenties.get(
                    int(hryvni_list[-5])) + " " + units.get(int(hryvni_list[-4])) + hryvni_text
        else:
            hryvni_text = tens.get(int(hryvni_list[-4])) + hryvni_text

    if len(hryvni) > 5:
        if int(hryvni_list[-5]) == 0:
            hryvni_text = hundreds.get(int(hryvni_list[-6])) + hryvni_text
        else:
            hryvni_text = hundreds.get(
                int(hryvni_list[-6])) + " " + hryvni_text

    return hryvni_text


if __name__ == '__main__':
    sum = input(
        "Введіть грошову суму з копійками, розділивши їх крапкою. Сума не повинна перевищувати 999999.99: ")
    hryvni, kopiiky = sum.split('.')
    nazva_hryvni_print = nazva_hryvni(hryvni).capitalize()
    print(" ".join(nazva_hryvni_print.split()), nazva_kopiiky(kopiiky))
