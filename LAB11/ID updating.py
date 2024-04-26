import sqlite3

# Функция для обновления ID пользователя
def update_user_id(old_id, new_id):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()

    # Проверяем, существует ли контакт с указанным старым ID
    cursor.execute('SELECT * FROM PhoneBook WHERE id = ?', (old_id,))
    existing_user = cursor.fetchone()

    if existing_user:
        # Обновляем ID контакта на новый ID
        cursor.execute('UPDATE PhoneBook SET id = ? WHERE id = ?', (new_id, old_id))
        print("ID пользователя успешно обновлен.")
    else:
        print("Контакт с указанным старым ID не найден.")

    conn.commit()
    conn.close()

# Главная функция
def main():
    old_id = int(input("Введите старый ID контакта: "))
    new_id = int(input("Введите новый ID контакта: "))
    update_user_id(old_id, new_id)

if __name__ == "__main__":
    main()
