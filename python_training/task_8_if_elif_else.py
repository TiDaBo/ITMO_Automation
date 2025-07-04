# Программа проверяет, является число положительным
# или отрицательным и выводит соответствующее сообщение.

num = 0

# Также попробуйте следующие варианты выражения num:
# num = -5
# num = 0

if num >= 0:
    print('Число больше либо равно 0')
else:
    print('Число отрицательное')

# Задача
#
# str_2 содержит в себе str_1?

str_1 = 'test'
str_2 = 'test1'

# if str_1 in str_2:
#     print('Да')
# else:
#     print('Нет')

def task_y_n(str_1, str_2):
    if str_1 in str_2:
        print('ДА')
    else:
        print('НЕТ')
task_y_n('test', 'test1')


num_float = -4.5

# Также попробуйте варианты:
# num_float = 0
# num_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')


num = 5
permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


# Задача:
# student_rank, year_of_study

def status(year: int) -> str:
    if 1 <= year <= 4:
        print('Ваш статус - бакалавр')
    elif year == 5 or year == 6:
        print('Ваш статус - магистр')
    elif year in range (7, 9):
        print('Ваш статус - аспирант')
    else:
        print('Введите корректный год обучения')

status(9)


# Задача:

n = 5

if n > 100 or n < -100:
    print('-')
else:
    print('+')


def num_rank(n: int) -> str:
    if n > 100 or n < -100:
        print('-')
    else:
        print('+')

num_rank(555)