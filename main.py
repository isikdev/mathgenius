def main():
    # Запрашиваем у пользователя действие
    action = input("Выберите действие:\n1. Корень числа\n2. Куб числа\n3. Квадрат числа\n: ")

    # Проверяем, какое действие выбрал пользователь
    if action == "1":
        # Запрашиваем у пользователя число
        number = float(input("Введите число: "))

        # Находим корень числа
        root = math.sqrt(number)

        # Выводим результат
        print("Корень числа:", root)
    elif action == "2":
        # Запрашиваем у пользователя число
        number = float(input("Введите число: "))

        # Находим куб числа
        cube = number ** 3

        # Выводим результат
        print("Куб числа:", cube)
    elif action == "3":
        # Запрашиваем у пользователя число
        number = float(input("Введите число: "))

        # Находим квадрат числа
        square = number ** 2

        # Выводим результат
        print("Квадрат числа:", square)
    else:
        print("Недопустимое действие")

if __name__ == "__main__":
    main()
