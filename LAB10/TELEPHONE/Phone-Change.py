import sqlite3

# Функция для обновления номера телефона или имени пользователя в базе данных
def update_contact(contact_id, new_name=None, new_phone=None):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    if new_name:
        cursor.execute('UPDATE PhoneBook SET name = ? WHERE id = ?', (new_name, contact_id))
    if new_phone:
        cursor.execute('UPDATE PhoneBook SET phone = ? WHERE id = ?', (new_phone, contact_id))
    conn.commit()
    conn.close()

# Главная функция
def main():
    contact_id = int(input("Введите ID контакта, которого вы хотите изменить: "))
    new_name = input("Введите новое имя пользователя (если не хотите менять, оставьте пустым): ")
    new_phone = input("Введите новый номер телефона (если не хотите менять, оставьте пустым): ")
    update_contact(contact_id, new_name, new_phone)
    print(f"Контакт с ID {contact_id} успешно обновлен.")

if __name__ == "__main__":
    main()
