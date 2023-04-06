import string
import random
def get_random_password(n: int=8) -> str:
    symbol_parol = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
    parol = "".join(random.sample(symbol_parol, n))

    return parol

print(get_random_password())
