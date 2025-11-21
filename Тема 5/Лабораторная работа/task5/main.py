import string
import random


def get_random_password(n: int=8) -> str:
    symbol_parol = string.ascii_letters + string.digits
    return "".join(random.sample(symbol_parol, n))


print(get_random_password())
