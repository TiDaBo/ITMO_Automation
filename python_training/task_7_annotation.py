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


def two_lists(a: list, b: list) -> int:
  return max(len(a), len(b))

print(two_lists)


def append_list(my_list: list):
    my_list.append('test')
    return my_list

print(append_list(['one', 2, 3, 4]))


def sum_list(my_list: list) -> int:
    result = 0
    for elem in my_list:
        result = result + elem
    return result

print(sum_list([1, 2, 3]))