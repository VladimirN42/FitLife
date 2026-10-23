import string

# Шаг 1. Знакомство с пользователем
print("Привет! Давайте познакомимся! :)")

# Запрос имени
user_name = input("Как тебя зовут?: ")

# Запрос возраста с защитой от ошибок
while True:
    user_age = input("Сколько тебе лет?: ")
    try:
        user_age_int = int(user_age)
        if 0 < user_age_int <= 120:
            break
        else:
            print("Пожалуйста, введите возраст от 1 до 120.")
    except ValueError:
        print("Ошибка: введите корректное целое число.")

# Приветствие
print(f"Приятно познакомиться, {user_name}!")

# Шаг 2. Расчёт ИМТ и нормы воды
print("Теперь давай рассчитаем ИМТ и норму воды! :)")

# Ввод веса
while True:
    weight_input = input("Введите ваш вес в килограммах: ")
    allowed_chars = set(string.digits + '.')

    if (
        len(weight_input) > 0
        and all(ch in allowed_chars for ch in weight_input)
        and weight_input.count('.') <= 1
    ):
        try:
            user_weight = float(weight_input)
            if 0 < user_weight <= 300:
                break
            else:
                print(
                    "Вес должен быть больше 0 и не больше 300 кг. "
                    "Попробуйте ещё раз."
                )
        except ValueError:
            print("Ошибка: не удалось распознать число. Попробуйте ещё раз.")
    else:
        print("Ошибка: введите корректное число (например, 70.5).")

# Ввод роста
while True:
    height_input = input(
        "Введите ваш рост в метрах (например, 1.75): "
    ).strip()
    allowed_chars = set(string.digits + '.')

    if (
        len(height_input) > 0
        and all(ch in allowed_chars for ch in height_input)
        and height_input.count('.') <= 1
    ):
        try:
            user_height = float(height_input)
            if 0 < user_height <= 3:
                break
            else:
                print(
                    "Рост должен быть больше 0 и не больше 3 метров. "
                    "Попробуйте ещё раз."
                )
        except ValueError:
            print("Ошибка: не удалось распознать число. Попробуйте ещё раз.")
    else:
        print("Ошибка: введите корректное число (например, 1.75).")

# Расчёт ИМТ
bmi = user_weight / (user_height ** 2)
bmi_rounded = round(bmi, 1)

# Расчёт нормы воды
WATER_PER_KG_ML = 30
water_ml = user_weight * WATER_PER_KG_ML
water_l = water_ml / 1000
water_l_rounded = round(water_l, 2)

# Вывод результатов
print(
    f"Отчёт для пользователя: {user_name}, {user_age_int} лет",
    f"Твой Индекс Массы Тела: {bmi_rounded}",
    f"Рекомендуемая норма воды: {water_l_rounded} л",
    "Расчёт окончен. Будьте здоровы!",
    sep="\n",)
