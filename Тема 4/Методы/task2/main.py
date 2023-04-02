def is_palindrome(str_):
    str_ = str_.lower()
    str_ = "".join(str_.split())

    if str_ == str_[::-1]:
        print("Строка палиндром")
    else:
        print("Строка не палиндром")


is_palindrome("Кит на море не романтик")
is_palindrome("Прочая строка")
