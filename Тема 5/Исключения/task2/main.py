def is_lucky_number(num: int) -> bool:
    if not num > 0:
        raise ValueError("Число должно быть положительным.")
    if num // 1000000 != 0:
        raise ValueError("Число должно быть шестизначным.")

    list_ = [int(i) for i in str(num)]
    return sum(list_[:3]) == sum(list_[3:])


print(is_lucky_number(123321))
print(is_lucky_number(111111))
print(is_lucky_number(123456))
print(is_lucky_number(456243))
