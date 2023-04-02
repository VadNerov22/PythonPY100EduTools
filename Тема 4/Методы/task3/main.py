def count(list_, n):
    count_n = 0
    for i in list_:
        if i == n:
            count_n += 1
    return count_n


list_items = [1, 2, "3", 1]
print(count(list_items, 1) == list_items.count(1))  # True
print(count(list_items, 3) == list_items.count(3))  # True
