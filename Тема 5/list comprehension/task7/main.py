def task(num: int) -> bool:
    num_list = [int(i) for i in str(abs(num))]
    return 10 <= sum(num_list) <= 99

print(task(12))
print(task(555))
print(task(-12))
print(task(-149))
