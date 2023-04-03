from typing import Any

def index(list_: list, x: Any) -> int:
    for index_, val in enumerate(list_):
        if val == x:
            return index_
    raise ValueError("В списке нет указанного значения")

list_items = [1, 2, "3", 1]
print(index(list_items, 1) == list_items.index(1))  # True
