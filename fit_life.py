import string

# Шаг 1. Знакомство с пользователем (создаём дружелюбный интерфейс)
print("Привет! Давайте познакомимся! :)")

# Запрос имени и сохранение в переменную
user_name = input("Как тебя зовут?: ")

# Запрос возраста и преобразование в число
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

# Вывод данных
print(f"Приятно познакомиться, {user_name}!")

# Шаг 2. Сбор параметров и расчёты (добавляем полезную логику)
print("Теперь давай рассчитаем ИМТ и норму воды! :)")

# Запрос Веса и преобразование в Float
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

# Запрос роста и преобразование: цифры + точка, максимум одна точка
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

# Расчёт ИМТ: вес (кг) / (рост (м) ** 2)
bmi = user_weight / (user_height ** 2)

# Округляем ИМТ
bmi_rounded = round(bmi, 1)

# Константа: норма воды в мл на 1 кг веса
WATER_PER_KG_ML = 30

# Расчёт нормы воды в мл
water_ml = user_weight * WATER_PER_KG_ML

# Перевод в литры
water_l = water_ml / 1000

# Округляем литры
water_l_rounded = round(water_l, 2)

# Вывод
print(
    f"Отчёт для пользователя: {user_name}, {user_age_int} лет",
    f"Твой Индекс Массы Тела: {bmi_rounded}",
    f"Рекомендуемая норма воды: {water_l_rounded} л",
    "Расчёт окончен. Будьте здоровы!",
    sep="\n",
)
