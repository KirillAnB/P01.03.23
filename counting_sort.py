import random


def sort(container):
    max_item = max(container)
    new_list = [0] * (max_item + 1)
    for item in container:
        new_list[item] += 1
    sorted_list = []
    k = 0
    for item in new_list:
        for _ in range(item):
            sorted_list.append(k)
        k += 1
    return sorted_list


if __name__ == '__main__':
    list_ = [random.randint(0, 100) for _ in range(100)]
    print(list_)
    print(sort(list_))
