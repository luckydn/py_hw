

class PhoneBook:
    def __init__(self, path: str = 'contact_bd.txt'):
        self.data = ''
        self.path = path
        self.phone_book = []
        self.new_phone_book = []


    def open_file(self):
        with open(self.path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for contact in data:
                new = contact.strip().split(';')
                new_contact = {}
                new_contact['name'] = new[0]
                new_contact['phone'] = new[1]
                new_contact['comment'] = new[2]
                self.phone_book.append(new_contact)
            self.new_phone_book.append(self.phone_book)
    def get(self):
        return self.phone_book
    def add(self, new_contact):
        self.phone_book.append(new_contact)

    def safe_file(self):
        data = []
        for contact in self.phone_book:
            data.append(';'.join(contact.values()))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def search(self, find_option: str) -> list:
        all_find = []
        for contact in self.phone_book:
            for element in contact.values():
                if find_option in element:
                    all_find.append(contact)
        return all_find

    def change_contact(self, ind, contact):
        self.phone_book.pop(ind-1)
        self.phone_book.insert(ind-1, contact)

    def delete_contact(self, ind):
        self.phone_book.pop(ind-1)

    def get_name(self, ind: int):
        return self.phone_book[ind - 1].get('name')

    def check_changes(self, pb):
        if self.new_phone_book != pb:
            return True
        return False