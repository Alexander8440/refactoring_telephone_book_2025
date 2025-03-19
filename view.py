
class View:
    ''' Класс View отвечает за вывод меню, получение ввода от пользователя,
     отображение контактов и сообщений. '''
    @staticmethod
    def show_menu(menu_items: list):
        print("\n".join([f"{ i +1}. {item}" for i, item in enumerate(menu_items)]))

    @staticmethod
    def show_contacts(contacts: list):
        if not contacts:
            print("Справочник пуст!")
        else:
            print("\n".join([f"{ i +1}. {contact}" for i, contact in enumerate(contacts)]))

    @staticmethod
    def get_input(prompt: str) -> str:
        return input(prompt)

    @staticmethod
    def show_message(message: str):
        print(message)

    @staticmethod
    def show_error(error: str):
        print(f"Ошибка: {error}")