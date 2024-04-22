import sqlite3

# Функция для вставки данных пользователя в таблицу
def insert_contact(name, phone):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO PhoneBook (name, phone) VALUES (?, ?)', (name, phone))
    conn.commit()
    conn.close()

# Функция для ввода данных пользователя с клавиатуры
def enter_data():
    name = input("Введите имя пользователя: ")
    phone = input("Введите номер телефона: ")
    return name, phone

# Главная функция
def main():
    name, phone = enter_data()
    insert_contact(name, phone)
    print("Контакт успешно добавлен в телефонную книгу.")

if __name__ == "__main__":
    main()
