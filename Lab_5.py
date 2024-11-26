import random

print(
    "Добро пожаловать в игру! \n"
    "Правила: В начале игры мы случайным образом определим начальное количество камней в куче.\n"
    "Далее игроки будут по очереди выбирать какое количество камней они хотят убрать из кучи (1 - 3 камня).\n"
    "Победителем считается игрок, после окончания хода которого, в куче остался один камень.\n")


def check(input_data):
    for char in input_data:
        if char not in "012345678":
            return False
        if (int(input_data) < 1) or (int(input_data) > 3):
            return False
        return True


def get_ai_step(num_stones):
    if num_stones <= 4:
        return 1, abs(1 - num_stones)
    user_2 = random.randint(1, 3)
    return num_stones - user_2, user_2


num_stones = random.randint(4, 30)
win = "undefind"

while win == "undefind":
    print(f"\nТекущее значение камней в куче: {num_stones}\n")
    print("Ваш ход\n"
          "Введите число камней, которое хотите убрать из кучи (1 - 3 камня): ")

    input_data = input()

    if check(input_data):
        user_1 = int(input_data)
        num_stones = num_stones - user_1

        if num_stones == 1:
            print("\nВы победили!")
            win = "User_win"
        elif num_stones < 1:
            print("Подумайте еще раз")
        elif num_stones > 1:
            print(f"\nТекущее значение камней в куче: {num_stones}\n")
            print("Ход другого игрока ...")
            num_stones, user_2 = get_ai_step(num_stones)

            if user_2 == 1:
                print(f"Другой игрок убрал {user_2} камень из кучи")
            else:
                print(f"Другой игрок убрал {user_2} камня из кучи")

            if num_stones == 1:
                print(f"\nТекущее значение камней в куче: {num_stones}\n")
                print("Вы проиграли. Желаем удачи в следующий раз!")
                win = "user_2_win"
    else:
        print("Неверные данные, попробуйте еще раз")
