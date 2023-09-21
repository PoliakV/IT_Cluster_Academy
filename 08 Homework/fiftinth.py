from helper import print_bord, try_to_move, is_board_completed

bord = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 1, 2, 0]

while not is_board_completed(bord):
    print(print_bord(bord))
    choice = int(input("Enter number to replace>"))
    bord = try_to_move(bord, choice)

print("YOU WIN!!!")
