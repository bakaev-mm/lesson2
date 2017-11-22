def find_person(name):
    while True:
       if  find_name == name_list.pop():
            print('{} нашелся'.format(find_name))
            break
print('Введите имя, которое ищите:')        


find_name = input()
name_list = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
find_person(find_name)
