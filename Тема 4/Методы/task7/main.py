students_dict = {
    'Саша': 27,
    'Кирилл': 52, 
    'Маша': 14, 
    'Петя': 36, 
    'Оля': 43, 
}

vozrast = list(students_dict.values())
sr_vozrast = sum(vozrast) / len(vozrast)

print(sr_vozrast)
