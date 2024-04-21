"""
Программа спрашивает у пользователя бюджет отпуска. Затем она спрашивает его продолжительность. 
Далее программа спрашивает предпочитаемый климат: «холодный», «умеренный» или «жаркий».

На основании введенных данных программа предлагает направление и тип отдыха (городская экскурсия, пляжный отдых, поход в горы и т.д.), 
учитывая следующие условия:

Если бюджет составляет менее 500 долларов и желаемая продолжительность отдыха менее 5 дней,
то программа предлагает посетить местную достопримечательность независимо от климатических предпочтений.

Если бюджет составляет от 500 до 1000 долларов, и желаемая продолжительность отдыха вновь менее 5 дней то:
Для холодного климата, программа предлагает поход в горы;
Для умеренного климата программа предлагает городскую экскурсию;
Для жаркого климата программа предлагает пляжный отдых.

Если бюджет превышает 1000 долларов и отдых длится более 7 дней, то:
Для жаркого климата программа предлогает заграничный пляжный отдых;
Для умеренного или холодного климата программа предлогает международный культурный тур.

Если ни один вариант не подходит, то программа предлагает никуда не ехать и сэкономить деньги.
"""

# Программа спрашивает пользователя о его предпочтениях в отпуске
budget = int(input("Какой у вас бюджет на отпуск в долларах? "))
days = int(input("Сколько дней вы планируете провести в отпуске? "))
climate = input("Какой климат вы предпочитаете (холодный, умеренный, жаркий)? ")

# Программа предлагает вид отдыха исходя из предпочтений и вохможностей пользователя
if budget < 500 and days < 5:
    print("Рассмотрите возможность изучения местных достопримечательностей!")
elif 500 <= budget <= 1000:
    if climate == "холодный":
        print("Горный поход идеально подойдет вам!")
    elif climate == "умеренный":
        print("Вам подойдет экскурсия по историческому центру города!")
    elif climate == "теплый":
        print("Как насчет пляжного отдыха на побережье?")
elif budget > 1000 and days > 7:
    if climate in ["умеренный", "холодный"]:
        print("Международный культурный тур станет незабываемым событием!")
    elif climate == "жаркий":
        print("Подумайте о пляжном отдыхе за границей!")
else:
    print("Возможно, было бы неплохо сэкономить немного больше на отпуск своей мечты или скорректировать свои предпочтения.")