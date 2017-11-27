def ask_user(): 
    while True:
        user_say = input('Как дела?')
        print(get_answer(user_say))
        if user_say.lower() == 'пока':
            break




def get_answer(question):
    answer = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    question = question.lower()
    return answer.get(question, 'Не понимаю')

ask_user()
