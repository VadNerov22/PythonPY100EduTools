def get_unique_words(str_):
    text_ = list(set(str_.split()))
    text_.sort()
    return text_

print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
