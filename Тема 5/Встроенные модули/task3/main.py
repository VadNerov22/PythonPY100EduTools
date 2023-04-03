from random import randint

random_list = [randint(-100, 100) for _ in range(50)]
count_otr = [i for i in random_list if i < 0]

print(len(count_otr))
