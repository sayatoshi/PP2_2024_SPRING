import pygame
import random

# Инициализация Pygame
pygame.init()

# Установка размера экрана
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Snake")

# Функция рисования змейки
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

# Функция рисования яблока
def draw_apple(apple):
    pygame.draw.rect(screen, RED, (apple[0] * GRID_SIZE, apple[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def show_game_over():
    font = pygame.font.SysFont(None, 100)
    text = font.render("GAME OVER", True, (255, 0, 0))
    text_rect = text.get_rect(center=(RES // 2, RES // 2))
    screen.blit(text, text_rect)

# Генерация случайного положения для яблока
def generate_apple():
    return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Инициализация змейки
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
dx, dy = 0, 0

# Инициализация яблока
apple = generate_apple()

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

    # Обновление положения змейки
    new_head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, new_head)

    if (
        snake[0][0] < 0 or snake[0][0] >= GRID_WIDTH or
        snake[0][1] < 0 or snake[0][1] >= GRID_HEIGHT
    ):
        
        running = False

    # Проверка на столкновение с яблоком
    if snake[0] == apple:
        apple = generate_apple()
    else:
        snake.pop()

    # Рисование змейки и яблока
    draw_snake(snake)
    draw_apple(apple)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение скорости кадров
    clock.tick(10)

# Выход из игры
pygame.quit()