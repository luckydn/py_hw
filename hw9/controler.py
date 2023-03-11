
import menu_contact
from hw8 import db_manager

pb = db_manager.PhoneBook()


def start():
    while True:
        choise = menu_contact.menu()
        match choise:
            case 1:
                pb.open_file()
            case 2:
                pb.safe_file()
            case 3:
                book = pb.get()
                menu_contact.show_contacts(book)
            case 4:
                new = menu_contact.new_contact_input()
                pb.add(new)
            case 5:
                find = menu_contact.search_contact()
                result = pb.search(find)
                menu_contact.show_contacts(result)
            case 6:
                book = pb.get()
                menu_contact.show_contacts(book)
                ind = menu_contact.input_id()
                contact = menu_contact.new_contact_input()
                pb.change_contact(ind, contact)
            case 7:
                book = pb.get()
                menu_contact.show_contacts(book)
                ind = menu_contact.input_id()
                name = pb.get_name(ind)
                if menu_contact.confirm('Удалить', name):
                    pb.delete_contact(ind)
            case 8:
                if pb.check_changes(pb):
                    if menu_contact.confirm_changes():
                        pb.safe_file()
                print("До свидания")
                break