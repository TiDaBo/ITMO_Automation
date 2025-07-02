a: int = 5
b: str = 'строка'
c: list = [1, 2]


def indent(s: str, width: int) -> str:
    return ' ' * (max(0, width - len(s))) + s

print(indent('123', 123))


# Задачи:

def str_len(s: str = '') -> int:
    return len(s)

print(str_len)


# def two_lists(a: list = [1, 2, 3], b: list = [5, 6]) -> int:
#    return max(len(a, b))
#
# print(two_lists)

def two_lists(a: list, b: list) -> int:
  return max(len(a), len(b))

print(two_lists)


# def random_list(a: list, b: int) -> list:
#     return a add[b]
#
# print(random_list)


def int_list[a: int, b: int, c: int, d: int] -> int:
    return a + b + c + d

print int_list[1, 2, 3, 4]