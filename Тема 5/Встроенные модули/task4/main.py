from random import randint

def random_number() -> int:
    random_list = [randint(0, 9) for _ in range(3)]
    number = "".join([str(i) for i in random_list])
    return int(number)

print(random_number())
