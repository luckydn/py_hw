import db_manager
import menu_contact


def start():
    while True:
        choise = menu_contact.menu()
        match choise:
            case 1:
                db_manager.open_file()
            case 2:
                db_manager.safe_file()
            case 3:
                pb = db_manager.get()
                menu_contact.show_contacts(pb)
            case 4:
                new = menu_contact.new_contact_input()
                db_manager.add(new)
            case 5:
                find = menu_contact.search_contact()
                result = db_manager.serch(find)
                menu_contact.show_contacts(result)
            case 6:
                pb = db_manager.get()
                menu_contact.show_contacts(pb)
                ind = menu_contact.input_id()
                contact = menu_contact.new_contact_input()
                db_manager.change_contact(ind, contact)
            case 7:
                pb = db_manager.get()
                menu_contact.show_contacts(pb)
                ind = menu_contact.input_id()
                name = db_manager.get_name(ind)
                if menu_contact.confirm('Удалить', name):
                    db_manager.delete_contact(ind)
            case 8:
                if db_manager.check_changes():
                    if menu_contact.confirm_changes():
                        db_manager.safe_file()
                print("До свидания")
                break