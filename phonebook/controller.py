import view
import model
# import phone_book

def start():
    while True:
        # pb = phone_book.PhoneBook('phonebook\phone.txt')
        # # pb.new_contact('Иррина Алегрова', '23456789', 'певица')
        # # print(pb)
        # # pb.save()
        pb = model.get_phone_book()
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.show_message('Файл успешно открыт')
            case 2:
                model.save_file()
                view.show_message('Файл успешно сохранен')
            case 3:
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                model.add_contact(view.add_contact())
            case 5:
                if  view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index('Введите номер изменяемого контакта')
                    contact = view.change_contact(pb,index)
                    model.change_contact(contact, index)
            case 6:
                search = view.input_search('Введите искомый элемент:')
                result = model.find_contact(search)
                view.show_contacts(result, 'Контакты не найдены')
            case 7:
                index = view.input_index('Введите номер удаляемого контакта')
                contact = view.delete_contact(pb,index)
                model.delete_contact(index)
            case 8:
                return