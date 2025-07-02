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

def append_list(my_list: list):
    my_list.append('test')
    return my_list

print(append_list(['one', 2, 3, 4]))


# def numeral_list([a: int, b: int, c: int]) -> int:
#     for elem in numeral_list:
#         print(a+b+c)
#
# print(numeral_list([1, 2, 3]))

def sum_list(my_list: list) -> int:
    result = 0
    for elem in my_list:
        result = result + elem
    return result

print(sum_list([1, 2, 3]))