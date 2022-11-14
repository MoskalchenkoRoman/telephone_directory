import csv

def get_dict ():
    print('''Введите команду из списка:
    1 просмотр файла
    2 добавить запись''')


    x = int(input('выш выбор: '))
    if x == 1:
        file = 'Phone_dictionary.csv'
        with open (file,  encoding = 'utf-8') as data:
            reader = csv.reader(data)
            for row in reader:
                print(row)

    elif x == 2:
        dict = [] 
        id = input ('Введите порядковый номер: ')
        dict.append(id)
        surname = input('Введите фамилию: ')
        dict.append(surname)
        name = input('Введите имя: ')
        dict.append(name)
        birth_day = input('Введите дату рождения в формате ДДММГГ: ')
        dict.append(birth_day)
        work_pl = input('Введите название организации: ')
        dict.append(work_pl)
        ph_numb1 = input('Введите номера телефона через , : ')
        dict.append(ph_numb1)
       
        return dict