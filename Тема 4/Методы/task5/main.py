def get_sentences_list(str_):
    text_ = []
    for i in str_.split("."):
        if i:
            text_.append(i.strip())
    return text_

print(get_sentences_list("Здесь много разных слов. Возможно и много повторений..."))
