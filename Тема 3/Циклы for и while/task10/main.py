list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]

count_ch = 0 # четные
count_n = 0 # нечетные

for i in list_:
    if i % 2 == 0:
        count_ch += 1
    else:
        count_n += 1

if count_ch > count_n:
    print("Четных чисел больше")
elif count_n > count_ch:
    print("Нечетных чисел больше")
else:
    print("Четных и нечетных одинаковое количество")
