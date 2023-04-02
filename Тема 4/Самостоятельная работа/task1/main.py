def remove_whitespace(str_):
    text_ = []
    for i in str_.split(" "):
        if i:
            text_.append(i.strip())
    return ' '.join(text_)

str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
