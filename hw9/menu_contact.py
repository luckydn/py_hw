

def menu():
    print('''\nГлавное меню
        1. открыть файл
        2. сохранить файл
        3. показать контакты
        4. добавить контакт
        5. найти контакт
        6. изменить контакт
        7. удалить контакт
        8. выход''')
    while True:
        try:
            choise = int(input("Введите пункт меню: "))
            if 0 < choise < 9:
                return choise
            else:
                print("Введите число от 1 до 8")
        except:
            print("Вводите цифры а не буквы")
        # return choise

def show_contacts(pb: list):
    if pb:
        for i, contact in enumerate(pb, 1):
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            print(f'{i}. {name:<20} {phone:<20} {comment:<20}')
    else:
        print("Телефонная книга пуста или файл не открыт")
def new_contact_input():
    name = input("Введите имя и фамилию: ")
    phone = input("Введите номер телефона: ")
    comment = input("Введите комментарий: ")
    new_contact = {'name': name,
                'phone': phone,
                'comment': comment}
    return new_contact

def search_contact():
    search = input("Введите искомый эллемент: ")
    return search

def input_id():
    ind = int(input("Введите индекс: "))
    return ind

def confirm(condition: str, name: str):
    answer = input(f"Вы действительно хотите {condition} контакт {name}? y/n?: ")
    if answer == 'y':
        return True
    else:
        return False

def confirm_changes():
    answer = input("У вас есть не сохраненные изменения, хотите их сохранить? y/n: ")
    return True if answer == 'y' else False