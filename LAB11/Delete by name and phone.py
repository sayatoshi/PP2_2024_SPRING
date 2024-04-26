import sqlite3

# Функция для удаления контакта из базы данных по имени и телефону
def delete_contact(name, phone):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM PhoneBook WHERE name = ? AND phone = ?', (name, phone))
    conn.commit()
    if cursor.rowcount == 0:
        print("Контакт не найден.")
    else:
        print("Контакт успешно удален из базы данных.")
    conn.close()

# Главная функция
def main():
    name = input("Введите имя контакта для удаления: ")
    phone = input("Введите номер телефона контакта для удаления: ")
    delete_contact(name, phone)

if __name__ == "__main__":
    main()
