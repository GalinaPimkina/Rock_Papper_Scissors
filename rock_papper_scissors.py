import random
import time

user_wins = 0
computer_wins = 0
game_draw = 0

choices = ["камень", "ножницы", "бумага"]

welcome = ['Добро пожаловать в игру "Камень, ножницы, бумага"!',
            'Чтобы начать играть, следуйте инструкциям на экране.',
            'Для выхода введите "Выход".',
            'Удачи!']

for w in welcome:
    print(w)
    time.sleep(2)


game = {
    'total': 0,
    'score': {
        'player_win': 0,
        'computer_win': 0,
        'zero_win': 0
    }
}


while True:
    user_input = input("Сделайте свой выбор: 'Камень' / 'Ножницы' / 'Бумага' или введите 'Выход', чтобы завершить игру: ").lower()

    if user_input == "выход":
        print(f"Итоговый счет: ваших побед - {user_wins}, побед компьютера - {computer_wins}, ничьих - {game_draw}.")
        time.sleep(1)
        print('Приходите к нам еще! Пока!')
        break

    if user_input not in choices:
        print("Выберите камень, ножницы, бумагу или выход.")
        continue

    computer_pick = random.choice(choices)
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
