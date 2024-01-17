def create_random_list(length, min_value, max_value):
    import random
    return [random.randint(min_value, max_value) for _ in range(length)]


def dict_generator(my_list):
    from collections import Counter
    return dict(Counter(my_list))


def main():
    mn, mx, ln = 1, 10, 20
    lst = create_random_list(ln, mn, mx)
    dct = dict_generator(lst)
    print(dct)


main()
