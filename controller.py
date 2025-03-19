from model import PhoneBook, FileHandler, Contact, FileOperationError, ContactNotFoundError, InvalidContactDataError
from view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.phone_book = PhoneBook()
        self.filename = 'contacts.txt'
        self.menu_items = [
            'Показать все контакты',
            'Найти контакт',
            'Добавить контакт',
            'Удалить контакт',
            'Изменить контакт'
        ]

    def run(self):
        self.show_welcome_message()
        if not self.ask_to_open():
            return

        self.open_phonebook()
        self.main_loop()

    def show_welcome_message(self):
        print('#' * 60)
        print('Здравствуйте! Хотите открыть телефонный справочник?')
        print('#' * 60)

    def ask_to_open(self):
        choice = self.view.get_input("Выберите да или нет: ").lower()
        if choice == 'да':
            print('&' * 60)
            print('Добро пожаловать в телефонный справочник')
            print('&' * 60)
            return True
        print('Всего хорошего')
        return False

    def open_phonebook(self):
        try:
            self.phone_book = FileHandler.load_contacts(self.filename)
            if not self.phone_book.contacts:
                self.view.show_message("Справочник пуст!")
        except FileOperationError as e:
            self.view.show_error(str(e))

    def main_loop(self):
        while True:
            self.view.show_menu(self.menu_items)
            choice = self.view.get_input("Выберите пункт меню: ")

            try:
                if choice == '1':
                    self.show_all_contacts()
                elif choice == '2':
                    self.search_contact()
                elif choice == '3':
                    self.add_contact()
                elif choice == '4':
                    self.delete_contact()
                elif choice == '5':
                    self.update_contact()
                else:
                    self.view.show_message("Спасибо за использование справочника!")
                    break
            except Exception as e:
                self.view.show_error(str(e))

    def show_all_contacts(self):
        self.view.show_contacts(self.phone_book.contacts)

    def search_contact(self):
        name = self.view.get_input("Введите имя для поиска: ")
        found = self.phone_book.find_by_name(name)
        if not found:
            raise ContactNotFoundError("Контакт не найден")
        self.view.show_contacts(found)

    def add_contact(self):
        name = self.view.get_input("Введите имя: ")
        phone = self.view.get_input("Введите телефон: ")
        comment = self.view.get_input("Введите комментарий: ")

        if not name or not phone:
            raise InvalidContactDataError("Имя и телефон обязательны")

        self.phone_book.add_contact(Contact(name, phone, comment))
        FileHandler.save_contacts(self.filename, self.phone_book)
        self.view.show_message("Контакт добавлен")

    def delete_contact(self):
        self.show_all_contacts()
        index = int(self.view.get_input("Номер контакта для удаления: ")) - 1
        if index < 0 or index >= len(self.phone_book.contacts):
            raise ContactNotFoundError("Неверный номер контакта")

        self.phone_book.remove_contact(index)
        FileHandler.save_contacts(self.filename, self.phone_book)
        self.view.show_message("Контакт удален")

    def update_contact(self):
        self.show_all_contacts()
        index = int(self.view.get_input("Номер контакта для изменения: ")) - 1
        if index < 0 or index >= len(self.phone_book.contacts):
            raise ContactNotFoundError("Неверный номер контакта")

        old = self.phone_book.contacts[index]
        name = self.view.get_input(f"Новое имя ({old.name}): ") or old.name
        phone = self.view.get_input(f"Новый телефон ({old.phone}): ") or old.phone
        comment = self.view.get_input(f"Новый комментарий ({old.comment}): ") or old.comment

        self.phone_book.update_contact(index, Contact(name, phone, comment))
        FileHandler.save_contacts(self.filename, self.phone_book)
        self.view.show_message("Контакт обновлен")


if __name__ == "__main__":
    Controller().run()

