import random


def sort(list_):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(list_)-1):
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
                is_sorted = False
    return list_


if __name__ == '__main__':
    my_list = [random.randint(0, 100) for _ in range(100)]
    print(sort(my_list))
