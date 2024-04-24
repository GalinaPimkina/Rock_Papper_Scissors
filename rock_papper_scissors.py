import random
import time

user_wins = 0
computer_wins = 0
game_draw = 0

choices = ["камень", "ножницы", "бумага"]

while True:
    user_input = input("Сделайте свой выбор: 'Камень' / 'Ножницы' / 'Бумага' или 'Выход' для выхода: ").lower()
    if user_input == "выход":
        print(f"Итоговый счет: ваших побед - {user_wins}, побед компьютера - {computer_wins}, ничьих - {game_draw}.")
        quit()

    if user_input not in choices:
        print("Выберите камень, ножницы или бумагу или выход.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = choices[random_number]
    time.sleep(1)
    print(f"У компьютера {computer_pick}.")
    time.sleep(1)

    if user_input == "камень":
        if computer_pick == "камень":
            print("Ничья!")
            game_draw += 1
            continue
        elif computer_pick == "ножницы":
            print("Вы победили!")
            user_wins += 1
            continue
        elif computer_pick == "бумага":
            print("Компьютер победил!")
            computer_wins += 1
            continue

    if user_input == "ножницы":
        if computer_pick == "камень":
            print("Компьютер победил!")
            computer_wins += 1
            continue
        elif computer_pick == "ножницы":
            print("Ничья!")
            game_draw += 1
            continue
        elif computer_pick == "бумага":
            print("Вы победили!")
            user_wins += 1
            continue

    if user_input == "бумага":
        if computer_pick == "камень":
            print("Вы победили!")
            user_wins += 1
            continue
        elif computer_pick == "ножницы":
            print("Компьютер победил!")
            computer_wins += 1
            continue
        elif computer_pick == "бумага":
            print("Ничья!")
            game_draw += 1
            continue
