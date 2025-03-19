import os


class Contact:
    ''' Класс Contact с полями: имя, телефон, комментарий '''

    def __init__(self, name: str, phone: str, comment: str):
        self.name = name
        self.phone = phone
        self.comment = comment

    def __str__(self):
        return f"Имя-{self.name}:Телефон-{self.phone}:Комментарий-{self.comment}"


class PhoneBook:
    '''  Класс телефонная книга содержит список контактов,
     методы для управления контактами '''

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def remove_contact(self, index: int):
        del self.contacts[index]

    def update_contact(self, index: int, new_contact: Contact):
        self.contacts[index] = new_contact

    def find_by_name(self, name: str):
        return [contact for contact in self.contacts if contact.name == name]


class FileHandler:
    ''' Класс для работы с файлами отвечает
    за загрузку и сохранение контактов в файл.
    Обрабатывает исключения, связанные с файлами. '''
    @staticmethod
    def load_contacts(filename: str) -> PhoneBook:
        phone_book = PhoneBook()
        try:
            with open(filename, 'r', encoding='UTF-8') as file:
                if os.stat(filename).st_size == 0:  # Проверка на пустой файл
                    return phone_book

                for line in file:
                    if line.strip():
                        parts = line.strip().split(':')
                        data = {p.split('-')[0]: p.split('-')[1] for p in parts}
                        phone_book.add_contact(Contact(
                            data['Имя'],
                            data['Телефон'],
                            data['Комментарий']
                        ))
        except FileNotFoundError:
            open(filename, 'w', encoding='UTF-8').close()
        except Exception as e:
            raise FileOperationError(f"Ошибка чтения файла: {str(e)}")
        return phone_book
    @staticmethod
    def save_contacts(filename: str, phone_book: PhoneBook):
        try:
            with open(filename, 'w', encoding='UTF-8') as file:
                for contact in phone_book.contacts:
                    file.write(str(contact) + '\n')
        except Exception as e:
            raise FileOperationError(f"Ошибка записи в файл: {str(e)}")
class FileOperationError(Exception):
    ''' Исключения для обработки ошибок '''
    pass


class ContactNotFoundError(Exception):
    ''' Исключения для обработки ошибок.
     Например, при попытке удалить несуществующий контакт '''
    pass


class InvalidContactDataError(Exception):
    ''' Исключения для обработки ошибок.'''
    pass