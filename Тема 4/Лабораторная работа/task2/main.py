def get_count_char(str_):
    count_char = {}

    for char_ in str_.lower():
        if char_.isalpha() == True:
            if char_ in count_char:
                count_char[char_] += 1
            else:
                count_char[char_] = 1
    return count_char

def get_procent_char(str_):
# 5. Функция принимает словарь символов, где количество каждого элемента заменено на процентное отношение ко всем символам.
    count_procent_char = get_count_char(str_)
    all_ = sum(v for v in count_procent_char.values()) / 100
    for v in count_procent_char:
        count_procent_char[v] *= all_
    return count_procent_char

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
#print(get_procent_char(main_str)) # Вывод результатов по п. 5 задания
