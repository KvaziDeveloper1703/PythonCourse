"""
Программа выбирает случайное число от 1 до 100, а затем предлагает пользователю угадать это число. 
Используя цикл while, программа сверяет число пользователя со своим числом:

Если предположенное число больше, программа выведет «Мое число меньше, попробуйте еще раз».
Если предположенное число меньше, программа выведет «Мое число больше, попробуйте еще раз».
Если догадка верна, программа выведет «Поздравляем! Вы угадали число!» и завершится.

Цикл продолжается до тех пор, пока пользователь не угадает правильно.

Используйте функцию random.randint() для генерации случайного числа. Для этого вам нужно будет импортировать модуль random.
Перед сравнением обязательно преобразуйте предположение пользователя в целое число.
"""

import random

# Программа приветствует пользователя
print("Добро пожаловать в программу \"Угадайка\"!")

# Программа создает случайное число от 1 до 100
target_number = random.randint(1, 100)

print("Я выбрала число от 1 до 100. Попробуйте угадать его!")

# Инициализируйте цикл значением, которое не может быть правильным для выхода из него
guess = 0

# Программа запускает цикл угадывания
while guess != target_number:

    # Программа узнает предположение пользователя
    guess = int(input("Введите свое предположение: "))
    
    # Программа дает ответ на основе предположения пользователя
    if guess < target_number:
        print("Мое число меньше, попробуйте еще раз.")
    elif guess > target_number:
        print("Мое число больше, попробуйте еще раз.")
    else:
        print("Поздравляем! Вы угадали число!")