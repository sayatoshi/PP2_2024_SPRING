import sqlite3

# Функция для поиска контактов по части имени или телефона в базе данных
def find_contacts(search_term):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM PhoneBook WHERE name LIKE ? OR phone LIKE ?", ('%' + search_term + '%', '%' + search_term + '%'))
    contacts = cursor.fetchall()
    conn.close()
    return contacts

# Главная функция
def main():
    search_term = input("Введите часть имени или номера телефона для поиска: ")
    found_contacts = find_contacts(search_term)
    if found_contacts:
        print("Найденные контакты:")
        for contact in found_contacts:
            print(contact)
    else:
        print("Контакты не найдены.")

if __name__ == "__main__":
    main()
