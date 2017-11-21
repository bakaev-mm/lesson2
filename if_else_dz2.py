def compare():
    print('Введите первое значение')
    line1 = input()
    print('Введите второе значение')
    line2 = input()
    if line1 == line2:
        print(1)
    elif len(line1) > len(line2):
        print(2)
    elif line1 != line2:
        if line2 == 'learn':
            print(3)
        else:
            print('Введеные данные не соответствуют условиям функции')

compare()