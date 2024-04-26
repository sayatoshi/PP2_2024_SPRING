import sqlite3

# Функция для добавления нового пользователя или обновления ID существующего пользователя
def add_or_update_user(user_id, phone):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()

    # Проверяем, существует ли пользователь с заданным ID
    cursor.execute('SELECT * FROM PhoneBook WHERE id = ?', (user_id,))
    existing_user = cursor.fetchone()

    if existing_user:
        # Если пользователь существует, обновляем его ID
        cursor.execute('UPDATE PhoneBook SET phone = ? WHERE id = ?', (phone, user_id))
        print("Номер телефона пользователя успешно обновлен.")
    else:
        # Если пользователь не существует, выводим сообщение об ошибке
        print("Пользователь с указанным ID не найден в базе данных.")

    conn.commit()
    conn.close()

# Главная функция
def main():
    user_id = int(input("Введите ID пользователя: "))
    phone = input("Введите номер телефона пользователя: ")
    add_or_update_user(user_id, phone)

if __name__ == "__main__":
    main()
