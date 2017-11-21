print('Сколько тебе лет?')
age = input()
age = int(age)
if age < 7:
    print('Дуй в детсад')
elif age < 18:
    print('Вали в школу')
elif age < 23:
    print('Учись в инсте')
elif age < 65:
    print('Работай!') 
elif age < 100:
    print('Вяжи носки!')
else:
    print('Столько не живут!')