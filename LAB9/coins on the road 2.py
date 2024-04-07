import random
import sys
import time

import pygame
from pygame.locals import *

# Initialzing 
pygame.init()

# Set up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Defining some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Some main variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN_CENTER = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
SCORE = 0
SCORE_RECT = (SCREEN_WIDTH - 70, 0)
SPEED = 3
N = 25
was_speed_increased = False

# Creating main window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("COINS ON THE ROAD")

# Load background
BACKGROUND = pygame.image.load('c:\\Users\\tumas\\Desktop\\Python\\LAB9\\1.jpg')

# Creating fonts and texts
FONT = pygame.font.Font(None, 70)
FONT_SMALL = pygame.font.Font(None, 20)
GAME_OVER = FONT.render("Game over", True, BLACK)


class Enemy(pygame.sprite.Sprite):
    CAR_WIDTH = 40

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('c:\\Users\\tumas\\Desktop\\Python\\LAB9\\Enemy.png')
        self.rect = self.image.get_rect()
        # Random generating coorinates for enemy car
        self.rect.center = (random.randint(Enemy.CAR_WIDTH, SCREEN_WIDTH - Enemy.CAR_WIDTH), 0)

    def move(self):
        """
        Moving enemy car
        """
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(Enemy.CAR_WIDTH, SCREEN_WIDTH - Enemy.CAR_WIDTH), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Coins(pygame.sprite.Sprite):
    COIN_WIDTH = 20

    def __init__(self, max_weight):
        super().__init__()
        image = pygame.transform.scale(pygame.image.load('c:\\Users\\tumas\\Desktop\\Python\\LAB9\\Coin.png'),
                     (Coins.COIN_WIDTH, Coins.COIN_WIDTH))
        # List of images of differnt sizes
        self.images = [pygame.transform.rotozoom(image, 0, x/max_weight+1) for x in range(max_weight+1)]
        # List of coordinates with weight for every coin on road
        self.coin_list = []
        self.max_weight = max_weight

    def gen(self):
        """
        Generating new coin
        """
        self.coin_list.append((random.randint(Coins.COIN_WIDTH, SCREEN_WIDTH - Coins.COIN_WIDTH), 0, random.randint(1, self.max_weight)))

    def move(self):
        """
        Moving all coins and delete unnecessary
        """
        new_coords = []
        for w,h,c in self.coin_list:
            if h + SPEED <= SCREEN_HEIGHT:
                new_coords.append((w, h + SPEED, c))
        self.coin_list = new_coords

    def check(self, player_rect):
        """
        Calculate sum of coins, getted on the frame, and delete corresponding coins
        """
        new_coords = []
        res = 0
        for w,h,c in self.coin_list:
            if not pygame.Rect.colliderect(player_rect, self.images[c].get_rect(center = (w,h))):
                new_coords.append((w,h, c))
            else:
                res += c
        self.coin_list = new_coords
        return res

    def draw(self, surface):
        """
        Drawing all coins on the screen
        """
        for w,h,c in self.coin_list:
            surface.blit(self.images[c], self.images[c].get_rect(center = (w,h)))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('c:\\Users\\tumas\\Desktop\\Python\\LAB9\\Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH//2, 3*SCREEN_HEIGHT//4)

    def update(self):
        """
        Move player's car left or right if corresponding key was pressed
        """
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        """
        Draw player's car
        """
        surface.blit(self.image, self.rect)
    def get_rect(self):
        
        return self.rect

# Create objects
P1 = Player()
E1 = Enemy()
C = Coins(3)

# Groups of sprites
enemies = pygame.sprite.Group(E1)
sprites = pygame.sprite.Group(P1, enemies, C)

# Some events on timer
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
GEN_COIN = pygame.USEREVENT + 2
pygame.time.set_timer(GEN_COIN, 500)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == INC_SPEED:
            SPEED += 0.3
        if event.type == GEN_COIN:
            C.gen()
    
    # Increasing speed after N coins was reached
    if SCORE == N and not was_speed_increased:
        SPEED += 1
        was_speed_increased = True

    # Add background on screen
    DISPLAYSURF.blit(BACKGROUND, (0, 0))

    # Work with coins
    C.move()
    C.draw(DISPLAYSURF)
    SCORE += C.check(P1.get_rect())

    # Showing score
    scores = FONT_SMALL.render(f"Score {SCORE}", True, BLACK)
    DISPLAYSURF.blit(scores, SCORE_RECT)

    # Work with enemies' cars
    for enemy in enemies:
        enemy.move()
        enemy.draw(DISPLAYSURF)

    # Work with player's car
    P1.update()
    P1.draw(DISPLAYSURF)

    # Game over
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash1.wav').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(GAME_OVER, GAME_OVER.get_rect(center = SCREEN_CENTER))
        pygame.display.update()
        for sprite in sprites: sprite.kill()
        time.sleep(2)
        break
    
    # Show frame
    pygame.display.update()
    FramePerSec.tick(FPS)

# Quitting game
pygame.quit()
sys.exit()