# Задачи:
# 2. Функция на вход получает два произвольных числа.
# Вывести в консоль наибольшее из чисел.

def max_num(a: int, b: int) -> int:
    print(max(a, b))

max_num(156, 13)


# 3. Функция на вход получает два произвольных числа.
# Вывести в консоль “yes”, если они отличаются друг от друга на 135, иначе вывести на экран “No”

def differ_on_135(a: int, b: int):
    if a + 135 == b or b + 135 == a:
        print('Yes')
    else:
        print('No')

differ_on_135(5, 140)
differ_on_135(138, 3)
differ_on_135(-35, 100)
differ_on_135(7, -14)


# 4. Функция на вход получает произвольное число от 1 до 12 (номер месяца).
# Вывести название сезона года в консоль (зима, весна, лето, осень)

def season(a: int):
    if a == 1 or a == 2 or a == 12:
        print('Зима')
    elif a in range (3, 6):
        print('Весна')
    elif 6 <= a <= 8:
        print('Лето')
    elif a in range (9, 12):
        print('Осень')
    else:
        print('Введите число от 1 до 12')

season(3)


# 5. Функция на вход получает три произвольных числа.
# Если все числа больше 10, то вывести на экран “yes”, иначе “no”;

def more_than_ten(a: int, b: int, c: int):
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    else:
        print('No')

more_than_ten(15.5, c = 11, b = -25)


# Доп *
# 6. Функция на вход получает список, состоящий из 5 произвольных чисел.
# Найти количество положительных чисел среди них.

def count_positive(five_num_list: list):
    count = 0
    for item in five_num_list:
        if item>0:
            count += 1
    return count

print(count_positive([1, -5, 3.5, 7, 0]))


# 7. Функция на вход получает 2 переменные. a. Кол-во лет (int) b. Кол-во месяцев (int)
# Вывести в консоль количество дней за это время. Считать, что в каждом месяце 29 дней.

def days(years: int, months: int):
    days = 365 * years + 29 * months
    print(days)

days(15, 8)
