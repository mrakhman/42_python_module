def count_in_list(lst, key):
    counter = 0
    for el in lst:
        if el == key:
            counter += 1
    return counter
