import random
import time

game_total = 0
user_wins = 0
computer_wins = 0
zero_wins = 0

choices = ["камень", "ножницы", "бумага"]

welcome = ['Добро пожаловать в игру "Камень, ножницы, бумага"!',
            'Чтобы начать играть, следуйте инструкциям на экране.',
            'Для выхода введите "Выход".',
            'Удачи!']

for w in welcome:
    print(w)
    time.sleep(2)


while True:
    user_input = input("Сделайте свой выбор: 'Камень' / 'Ножницы' / 'Бумага' или введите 'Выход', чтобы завершить игру: ").lower()

    if user_input == "выход":
        if game_total == 0:
            print('Приходите к нам еще! Пока!')
            break
        else:
            print("ИТОГИ ИГРЫ:", f"Итоговый счет: ваших побед - {user_wins}, побед компьютера - {computer_wins}, ничьих - {zero_wins}.", sep='\n')
            break

    if user_input not in choices:
        print("Выберите камень, ножницы, бумагу или выход.")
        continue

    computer_pick = random.choice(choices)
    time.sleep(1)
    print(f"У компьютера {computer_pick}.")
    time.sleep(1)

    if user_input == "камень":
        game_total += 1
        if computer_pick == "камень":
            print("Ничья!")
            zero_wins += 1
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
        game_total += 1
        if computer_pick == "камень":
            print("Компьютер победил!")
            computer_wins += 1
            continue
        elif computer_pick == "ножницы":
            print("Ничья!")
            zero_wins += 1
            continue
        elif computer_pick == "бумага":
            print("Вы победили!")
            user_wins += 1
            continue

    if user_input == "бумага":
        game_total += 1
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
            zero_wins += 1
            continue
