def print_bord(bord):
    """Function return string-board to print"""
    import os
# Clearing the Screen
    os.system('cls')

    for i in bord:
        # if bord[i] in [0, 9] and bord[i + 1] in [0, 9] and bord[i + 2] in [0, 9]:
        return \
        '        -------------------------\n\
        | {:>3} | {:>3} | {:>3} | {:>3} |\n\
        -------------------------\n\
        | {:>3} | {:>3} | {:>3} | {:>3} |\n\
        -------------------------\n\
        | {:>3} | {:>3} | {:>3} | {:>3} |\n\
        -------------------------\n\
        | {:>3} | {:>3} | {:>3} | {:>3} |\n\
        -------------------------'.format(*bord)
    # TODO
    # return f'{bord[0:4]}\n{bord[4:8]}\n{bord[8:12]}\n{bord[12:16]}'
    #"15 14 13 12\n11 10  9  8\n 7  6  5  4\n 3  1  2  _"

def try_to_move(bord, choise):
    """Function check is _choise_-int is possible to change
    position with 0-int in the bord. If movement is possible do it.
    """
    x = bord.index(choise)

# Перевірка числа з комірки 0
    if x == 0 and bord[x + 1] == 0:
        bord[x + 1] = bord[x]
        bord[x] = 0
    elif x == 0 and bord[x + 4] == 0:
        bord[x + 4] = bord[x]
        bord[x] = 0

# Перевірка числа з комірок 1, 2
    elif (x == 1 or x == 2) and bord[x - 1] == 0:
        bord[x - 1] = bord[x]
        bord[x] = 0
    elif (x == 1 or x == 2) and bord[x + 1] == 0:
        bord[x + 1] = bord[x]
        bord[x] = 0
    elif (x == 1 or x == 2) and bord[x + 4] == 0:
        bord[x + 4] = bord[x]
        bord[x] = 0

# Перевірка числа з комірки 3
    elif x == 3 and bord[x - 1] == 0:
        bord[x - 1] = bord[x]
        bord[x] = 0
    elif x == 3 and bord[x + 4] == 0:
        bord[x + 4] = bord[x]
        bord[x] = 0

# Перевірка числа з комірок 4, 8
    elif (x == 4 or x == 8) and bord[x - 4] == 0:
        bord[x - 4] = bord[x]
        bord[x] = 0
    elif (x == 4 or x == 8) and bord[x + 1] == 0:
        bord[x + 1] = bord[x]
        bord[x] = 0
    elif (x == 4 or x == 8) and bord[x + 4] == 0:
        bord[x + 4] = bord[x]
        bord[x] = 0

# Перевірка числа з комірок 5, 6, 9, 10
    elif (x == 5 or x == 6 or x == 9 or x == 10) and bord[x - 4] == 0:
        bord[x - 4] = bord[x]
        bord[x] = 0
    elif (x == 5 or x == 6 or x == 9 or x == 10) and bord[x + 1] == 0:
        bord[x + 1] = bord[x]
        bord[x] = 0
    elif (x == 5 or x == 6 or x == 9 or x == 10) and bord[x + 4] == 0:
        bord[x + 4] = bord[x]
        bord[x] = 0
    elif (x == 5 or x == 6 or x == 9 or x == 10) and bord[x - 1] == 0:
        bord[x - 1] = bord[x]
        bord[x] = 0

# Перевірка числа з комірок 7, 11
    elif (x == 7 or x == 11) and bord[x - 4] == 0:
        bord[x - 4] = bord[x]
        bord[x] = 0
    elif (x == 7 or x == 11) and bord[x - 1] == 0:
        bord[x - 1] = bord[x]
        bord[x] = 0
    elif (x == 7 or x == 11) and bord[x + 4] == 0:
        bord[x + 4] = bord[x]
        bord[x] = 0

# Перевірка числа з комірки 12
    elif x == 12 and bord[x - 4] == 0:
        bord[x - 4] = bord[x]
        bord[x] = 0
    elif x == 12 and bord[x + 1] == 0:
        bord[x + 1] = bord[x]
        bord[x] = 0

# Перевірка числа з комірки 13, 14
    elif (x == 13 or x == 14) and bord[x - 1] == 0:
        bord[x - 1] = bord[x]
        bord[x] = 0
    elif (x == 13 or x == 14) and bord[x - 4] == 0:
        bord[x - 4] = bord[x]
        bord[x] = 0
    elif (x == 13 or x == 14) and bord[x + 1] == 0:
        bord[x + 1] = bord[x]
        bord[x] = 0

# Перевірка числа з комірки 15
    elif x == 15 and bord[x - 4] == 0:
        bord[x - 4] = bord[x]
        bord[x] = 0
    elif x == 15 and bord[x - 1] == 0:
        bord[x - 1] = bord[x]
        bord[x] = 0
  
    # TODO
    return bord

def is_board_completed(bord):
    """Function return True if the numbers in the board are ordered
    with zero at the finish, otherwise False"""
    if bord != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]:
    # TODO
        return False
    else: return True


if __name__ == "__main__":
    assert print_bord(
        [15,14,13,12,11,10,9,8,7,6,5,4,3,1,0,2]) == "15 14 13 12\n11 10  9  8\n 7  6  5  4\n 3  1  _  2"
    assert try_to_move([15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 1, 2, 0], 2) == [15, 14, 13, 12, 11, 10, 9, 8, 7,
                                                                                      6, 5, 4, 3, 1, 0, 2]
    assert is_board_completed([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]) == True
