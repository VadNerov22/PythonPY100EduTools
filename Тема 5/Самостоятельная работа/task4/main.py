from random import choice
from collections import Counter


EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

for count in counts:
    number = Counter([choice(coin) for _ in range(count)])
    list_freq.append(min(number.values()) / max(number.values()))

print(list_freq)
