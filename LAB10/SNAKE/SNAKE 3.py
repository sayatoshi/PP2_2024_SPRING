import pygame
import random
import time
import sqlite3

# Инициализация Pygame
pygame.init()

# Установка размера экрана
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SNAKE")

# Функция рисования змейки
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Функция рисования яблока
def draw_apple(apple, color):
    pygame.draw.rect(screen, color, (apple[0] * GRID_SIZE, apple[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Генерация случайного положения для яблока
def generate_apple():
    return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Функция для ввода имени пользователя
def get_username():
    username = input("Введите ваше имя: ")
    return username

def save_high_score(username, score):
    conn = sqlite3.connect('snake.db')
    cursor = conn.cursor()

    # Проверяем текущий рекорд пользователя
    cursor.execute('SELECT score FROM high_scores WHERE username = ?', (username,))
    current_record = cursor.fetchone()

    if current_record is None or score > current_record[0]:
        # Если рекорда пользователя нет или текущий результат лучше, обновляем его
        cursor.execute('INSERT OR REPLACE INTO high_scores (username, score) VALUES (?, ?)', (username, score))
        conn.commit()
        print("Новый рекорд для пользователя", username, ":", score)
    else:
        print("Рекорд пользователя", username, "не обновлен. Текущий рекорд:", current_record[0])

    conn.close()

# Функция для отображения экрана "Game Over"
def show_game_over_screen(score):
    font = pygame.font.SysFont(None, 36)
    text = font.render("Рекорд: " + str(score), True, RED)
    screen.blit(text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50))
    pygame.display.flip()
    pygame.time.delay(2000)

# Основная функция игры в змейку
def snake_game():
    # Отображение экрана ввода имени пользователя
    username = get_username()

    # Инициализация змейки
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    dx, dy = 0, 0

    # Инициализация еды разных видов
    food_types = [RED, BLUE]  # Цвета для разных видов еды
    food_timers = [5, 7]  # Время жизни каждого вида еды в секундах
    foods = [(generate_apple(), random.choice(food_types), time.time()) for _ in range(len(food_types))]

    # Основной игровой цикл
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(WHITE)

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -1
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, 1
                elif event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -1, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = 1, 0

        # Генерация новой еды по истечении времени
        current_time = time.time()
        for i in range(len(foods)):
            if current_time - foods[i][2] >= food_timers[i]:
                foods[i] = (generate_apple(), random.choice(food_types), current_time)

        # Обновление положения змейки
        new_head = (snake[0][0] + dx, snake[0][1] + dy)
        snake.insert(0, new_head)

        # Проверка на столкновение с едой
        for food in foods:
            if snake[0] == food[0]:
                # Увеличение змейки при поедании еды
                snake.append(snake[-1])
                # Удаление съеденной еды
                foods.remove(food)
                # Добавление новой еды
                foods.append((generate_apple(), random.choice(food_types), current_time))
                break  # Выход из цикла, чтобы не обрабатывать другие съеденные яблоки
        else:
            # Удаление последнего сегмента змеи, если она не съела яблоко
            snake.pop()

        # Проверка на столкновение с краями экрана
        if (
            snake[0][0] < 0 or snake[0][0] >= GRID_WIDTH or
            snake[0][1] < 0 or snake[0][1] >= GRID_HEIGHT
        ):
            # Отображение экрана "Game Over"
            show_game_over_screen(len(snake))
            running = False

        # Рисование змейки и еды
        draw_snake(snake)
        for food in foods:
            draw_apple(food[0], food[1])

        # Обновление экрана
        pygame.display.flip()

        # Ограничение скорости кадров
        clock.tick(10)

    # Сохранение рекорда в базу данных
    save_high_score(username, len(snake))

# Запуск игры
if __name__ == "__main__":
    snake_game()
    pygame.quit()
