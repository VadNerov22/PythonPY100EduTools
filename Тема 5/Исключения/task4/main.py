from typing import Any
def remove(list_: list, x: Any) -> int:
    for index_, val in enumerate(list_):
        if val == x:
            return list_[:index_] + list_[index_ + 1:]
    raise ValueError("В списке нет указанного значения")


print(remove([0, 0, 1, 2], 0))  # [0, 1]
print(remove([0, 1, 1, 2, 3], 1))  # [0, 1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
