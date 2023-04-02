def get_list_number_divisors(number):
    lis_number = []
    for i in range(1, number + 1):
        if number % i == 0:
            lis_number.append(i)
    return lis_number

print(get_list_number_divisors(23))
print(get_list_number_divisors(2 ** 16))
