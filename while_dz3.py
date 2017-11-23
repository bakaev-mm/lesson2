def ask_user(): 
    try:
        while True:
            user_say = input('Как дела?')
            if user_say == 'Хорошо':
                break
    except (KeyboardInterrupt):
        print('Пока!')
    
ask_user()