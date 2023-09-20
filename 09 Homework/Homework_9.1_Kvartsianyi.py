# Гра Blackjack має дуже прості правила: гравці беруть карти по одній намагаючись зібрати більше ніж опонент, але
# не перевищуючи 21. Набір карт містить карти від 2 до 10 включно, які рахуються за іх номіналом, також Король, Дама, Валет,
# що коштують по 10 кожна а також Туз, який може бути 1 або 11 в залежності від того що краще. Вхід програми декілька карт
# представлені символами: 2, 3, 4, 5, 6, 7, 8, 9;  T, J, Q, K для 10, Валет, Дама, Король; А - для Туза. Результат роботи
# кількість очок що не перевищує 21, або слово 'Bust' якщо сума більша за 21 (цей гравець відразу програє).

import random


def score(hand):
    score = 0
    ace = False
    for card in hand:
        if card.isdigit():
            score += int(card)
        elif card in "TJQK":
            score += 10
        else:
            ace = True
            score += 1
            if ace and score <= 11:
                score += 10
    return score


def random_card():
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    return random.choice(cards)


def play():
    player_hand = []
    dealer_hand = []
    player_hand.append(random_card())
    player_hand.append(random_card())
    dealer_hand.append(random_card())
    dealer_hand.append(random_card())
    print("Ваші карти:", player_hand, "Очки:", score(player_hand))
    print("Карти дилера: ['", dealer_hand[0], "', '?']")

    while True:
        choice = input(
            "Ви хочете продовжити чи зупинитись? (Продовжити: 1, зупинитись: 2) ")
        if choice == "1":
            player_hand.append(random_card())
            print("Ваші карти:", player_hand, "Очки:", score(player_hand))
            if score(player_hand) > 21:
                print("Ви розорені! Ви програли!")
                break
        elif choice == "2":
            break
        else:
            print("Ви ввели неправильне значення. Будь ласка введіть 1 або 2.")

    if score(player_hand) <= 21:
        print("Карти дилера:", dealer_hand, "Очки:", score(dealer_hand))
        while True:
            if score(dealer_hand) <= 16:
                dealer_hand.append(random_card())
                print("Карти дилера:", dealer_hand,
                      "Очки:", score(dealer_hand))
            if score(dealer_hand) > 21:
                print("Дилер розорився! Ви виграли!")
                break
            else:
                break

    if score(player_hand) <= 21 and score(dealer_hand) <= 21:
        if score(player_hand) > score(dealer_hand):
            print("Ви виграли!")
        elif score(player_hand) < score(dealer_hand):
            print("Ви програли!")
        else:
            print("Це нічия!")


play()
