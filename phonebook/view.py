import text_fields


def main_menu():
    return int(input('''Главное Меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Добавить контакт
    5. Изменить контакт
    6. Найти контакт
    7. Удалить контакт
    8. Выход
Выберите пункт меню:'''))

def show_contacts(book:list , error_message: str):
    if not book:
        print(error_message)
        return False
    else:
        for i, contact in enumerate(book, 1):
                print(f'{i}. {contact.get("name"):<20}'
                    f'{i}. {contact.get("phone"):<20}'
                    f'{i}. {contact.get("comment"):<20}')
        return True

def add_contact():
    name = input('Введите имя:')
    phone = input('Введите номер телефона:')
    comment = input('Введите комментарий:')
    return{'name': name, 'phone': phone, 'comment': comment}

def input_index(message: str):
    return int(input(message))

def input_search(message):
    return input(message)

def change_contact(book: list[dict], index: int):
    print('Введите новые данные или пустое поле, чтобы оставить без изменений')
    contact = add_contact()
    return {'name': contact.get('name') if contact.get('name') else book[index-1].get('name'),
            'phone': contact.get('phone') if contact.get('phone') else book[index-1].get('phone'),
            'comment': contact.get('comment') if contact.get('comment') else book[index-1].get('comment')}

def show_message(message: str):
    print('-' * len(message))
    print(message)
    print('-' * len(message))

def delete_contact(contact: dict, index: int):
    contact = contact[index]
    print(f'Контакт {contact} успешно удален')