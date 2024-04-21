"""
Программа просит пользователя придумать пароль. 
Используя цикл for, программа проверяет каждый символ пароля, чтобы убедиться, что он соответствует некоторым критериям: 
Наличие хотя бы одной цифры;
Наличие хотя бы одной заглавной и одной строчной буквы.

Также проверьте, составляет ли длина пароля не менее 8 символов. 

Если пароль соответствует всем критериям, выведите сообщение о том, что пароль надежный. 
В противном случае выведите сообщение, указывающее, чего не хватает в пароле. 
"""

# Программа спрашивает у пользователя пароль
password = input("Введите свой пароль, пожалуйста: ")

# Программа инициализирует переменные критериев пароля
has_digit = False
has_upper = False
has_lower = False

# Программа проверяет каждый символ в пароле
for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True

# Программа проверяет, соблюдены ли все критерии
if len(password) >= 8 and has_digit and has_upper and has_lower:
    print("Ваш пароль надежный.")
else:
    # Программа указывает, чего не хватает в пароле
    missing_criteria = []
    if not has_digit:
        missing_criteria.append("хотя бы одна цифра")
    if not has_upper:
        missing_criteria.append("хотя бы одна заглавная буква")
    if not has_lower:
        missing_criteria.append("хотя бы одна строчная буква")
    if len(password) < 8:
        missing_criteria.append("длина хотя бы 8 символов")
    
    print("У вашего пароля должна быть " + ", ".join(missing_criteria) + ".")