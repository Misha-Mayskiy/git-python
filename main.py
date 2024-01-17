import random
from collections import Counter


def create_random_list(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]


def dict_generator(my_list):
    return dict(Counter(my_list))


def main():
    mn = 1
    mx = 10
    ln = 20

    lst = create_random_list(ln, mn, mx)
    dct = dict_generator(lst)
    print(dct)


main()
