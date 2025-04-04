from unittest import TestCase
from model import Contact, PhoneBook


class TestContact(TestCase):  # класс для тестирования объекта "Контакт"
    def test_contact_creation(self):
        contact = Contact("Алексей", "555-1234", "семья")  # создание объекта с параметрами
        self.assertEqual(contact.name, "Алексей")  # сравнивает ожидаемое и фактическое значения
        self.assertEqual(contact.phone, "555-1234")  # сравнивает ожидаемое и фактическое значения
        self.assertEqual(contact.comment, "семья")  # сравнивает ожидаемое и фактическое значения


class TestPhoneBook(TestCase):
    def setUp(self):  # выполняется перед каждым тестом, создавая пустую телефонную книгу и два новых контакта
        self.pb = PhoneBook()
        self.pb.add_contact(Contact("Иван", "1234567", "друг"))
        self.pb.add_contact(Contact("Мария", "7654321", "работа"))

    def test_add_contact(self):
        initial_count = len(self.pb.contacts)  # проверяем количество контактов
        self.pb.add_contact(Contact("Новый", "000", "тест"))  # добавляем контакт
        self.assertEqual(len(self.pb.contacts), initial_count + 1)  # проверяем, что количество контактов
        # увеличивается на 1 после добавления

    def test_remove_contact(self):
        initial_count = len(self.pb.contacts)  # проверяем количество контактов
        self.pb.remove_contact(0)  # удаляем контакт
        self.assertEqual(len(self.pb.contacts), initial_count - 1)  # проверяем, что количество контактов
        # уменьшилось на 1 после удаления

    def test_find_by_name(self):
        results = self.pb.find_by_name("Иван")  # поиск по имени
        self.assertEqual(len(results), 1)  # проверяем, найден один контакт
        self.assertEqual(results[0].phone, "1234567")  # у найденного контакта правильный телефон

    def test_update_contact(self):
        new_contact = Contact("Петр", "999", "обновленный") # создаем новый контакт
        self.pb.update_contact(0, new_contact)
        self.assertEqual(self.pb.contacts[0].name, "Петр") # проверяет, что имя первого контакта изменилось после
        # обновления
