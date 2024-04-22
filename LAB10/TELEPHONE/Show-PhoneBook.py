import sqlite3

# Функция для получения всех контактов из базы данных
def get_contacts():
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM PhoneBook')
    contacts = cursor.fetchall()
    conn.close()
    return contacts

# Главная функция
def main():
    contacts = get_contacts()
    if contacts:
        print("Список контактов:")
        for contact in contacts:
            print("ID:", contact[0])
            print("Имя:", contact[1])
            print("Номер телефона:", contact[2])
            print()
    else:
        print("Список контактов пуст.")

if __name__ == "__main__":
    main()
