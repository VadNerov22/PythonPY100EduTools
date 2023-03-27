list_ = [4, -1, 10, -1, 3, 3, -1, 8, 6, 9]

# предположим, что первый элемент в нашем списке минимальный
min_value_index = 0
min_value = 0

# заменить на enumerate
for i, value_ in enumerate(list_):
    if value_ == min(list_):
        min_value = value_
        min_value_index = i
print("Минимальный элемент =", min_value, "находится по индексу", min_value_index)
