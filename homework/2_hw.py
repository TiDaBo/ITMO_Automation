# Задача 1

def task_1(a: int = 1, b: float = 3.14, c: str = 'doh', d: list = [6, 7, 8], e: bool = True) -> list:
    return(type(a), type(b), type(c), type(d), type(e))

print(task_1())


# Задача 2

def task_2(a = [1, 2, 3, 5, 13, 21]) -> list:
    return a[0:3]

print(task_2())

# *срез


# Задача 3

def task_3(a: int) -> int:
    return a * a

print(task_3(3))

