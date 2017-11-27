school_classes = [
    {'school_class': '1a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '1b', 'scores': [3, 3, 5, 5, 5]},
    {'school_class': '4c', 'scores': [4, 4, 4, 4, 2]},
    {'school_class': '4d', 'scores': [2, 2, 1, 2, 3]}
]

school_scores = []

for sc in school_classes:

    class_name = sc['school_class'].upper()
    class_scores = sc['scores']
    school_scores += class_scores
    class_score_average = sum(class_scores) / len(class_scores)

    print('Средний балл класса {}: {}'.format(class_name, class_score_average))

school_score_average = sum(school_scores) / len(school_scores)
print('Средний балл школы: {}'.format(school_score_average))
