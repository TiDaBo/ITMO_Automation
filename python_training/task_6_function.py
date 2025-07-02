# определяем функцию
def add(x, y):
    return x + y


# вызываем функцию
add(1, 2)    # или
print(add(1, 2))

print(add('I a', 'm a tester'))


def arg(a, b, c=2, d=3):
    return a + b + c + d


print(arg(1, 1, 1, 1))

print(arg(2, 2))

# print(arg(2, 2, '1', 1))

# print(arg(2, 2, 0.3, 1))


def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d


print(range_arg('1', '2', '3', '4'))

print(range_arg('1', '2', d='3', c='4'))


# Задачи

def task_func(a=(1, 2, 3, 4)):
    return a[0]

print(task_func())


# def square(radius, pi=3.14159):
#    return pi * radius^2

def compute_surface(radius, pi=3.14159):
    return pi * radius * radius

print(compute_surface(2))