import sqlite3

# Функция для удаления контакта из базы данных по номеру телефона
def delete_contact_by_phone(phone):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM PhoneBook WHERE phone = ?', (phone,))
    conn.commit()
    conn.close()

# Главная функция
def main():
    phone = input("Введите номер телефона пользователя, которого вы хотите удалить: ")
    delete_contact_by_phone(phone)
    print(f"Контакт с номером телефона '{phone}' успешно удален из телефонной книги.")

if __name__ == "__main__":
    main()
