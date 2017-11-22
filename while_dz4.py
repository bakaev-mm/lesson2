def ask_user(): 
    while True:
        user_say = input('Как дела?')
        if user_say == 'Хорошо':
            break




def get_answer():
    answer = {"Привет": "И тебе привет!", "Как дела": "Лучше всех", "Пока": "Увидимся"}
    question = input()
    print(answer[question].lower())
