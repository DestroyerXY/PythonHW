# 1. Открыть файл тел книги
# 2. Сохранить файл телефонной книги
# 3. Показать все контакты
# 4. Найти контакт
# 5. Добавить контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

def menu():
    dict_phnbk = {}
    while True:
        anc = int(input('Введите запрос: 1. Сохранить телефонную книгу, 2. Показать все контакты, 3. Найти контакт,'
        '4.Добавить контакт, 5. Изменить контакт, 6. Удалить контакт, 7. Выход  '))
        if anc == 1:
            safe_dir(dict_phnbk)
            print('Изменения сохранены')
        elif anc == 2:
            if len(dict_phnbk) == 0:
                dict_phnbk = open_read_dir()
            if len(dict_phnbk) == 0:
                print('Справочник пуст')
            else:
                print(dict_phnbk)
        elif anc == 3:
            cont_find(dict_phnbk)
        elif anc == 4:
            dict_phnbk = add_cont(dict_phnbk)
            print('Сохранись!')
        elif anc == 5:
            new_cont = cont_find(dict_phnbk)
            add_cont(dict_phnbk, new_cont)
        elif anc == 6:
            pass
        elif anc == 7:
            print('End')
            break
        else:
            print('Введите еще раз')


def open_read_dir():
    dict_phnbk = {}
    with open('phonebook.txt', 'r', encoding = 'UTF-8') as file:
        for line_cont in file.readlines():
            key, value = line_cont.split(':')
            dict_phnbk[key] = value
        print(dict_phnbk)
        return dict_phnbk

def safe_dir(dict_phnbk):
    str_phnbk = ''
    for key, value in dict_phnbk.items():
        str_phnbk += f'{key}:{value} \n'
    with open('phonebook.txt', 'w', encoding = 'UTF-8') as file:
        file.write(str_phnbk)

def add_cont(dict_phnbk, new_cont_in = [0]):
    if len(new_cont_in) < 2:
        name_cont = input('Введите ФИО контакта')
        phone_cont = input('Введите номер телефона')
        comment_cont = input('Введите комментарий к контакту')
        cont_list = [phone_cont, comment_cont]
    else:
        name_cont, cont_list = tuple(new_cont_in)
    # dict_phnbk[name_cont] = dict_phnbk.setdefault(name_cont, cont_list)
    dict_phnbk.setdefault(name_cont, cont_list)
    print(dict_phnbk[name_cont])
    return dict_phnbk

def cont_find(dict_phnbk):
    name_cont = input('Введите ФИО контакта')
    if name_cont in dict_phnbk:
        print(f'{name_cont}: {dict_phnbk[name_cont]}')
        return [name_cont, dict_phnbk[name_cont]]
    else:
        print('Не найден')

menu()