import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), "img")

WIDTH = 500
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Practice Game")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -7
        if keystate[pygame.K_RIGHT]:
            self.speedx = 7
        if keystate[pygame.K_UP]:
            self.speedy = -7
        if keystate[pygame.K_DOWN]:
            self.speedy = 7
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Mobup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(mob_img, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(3, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(3, 8)

class Mobleft(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(mob_img, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-50, -20)
        self.rect.y = random.randrange(HEIGHT - self.rect.width)
        self.speedx = random.randrange(3, 8)
    def update(self):
        self.rect.x += self.speedx
        if self.rect.left > WIDTH:
            self.rect.x = random.randrange(-50, -20)
            self.rect.y = random.randrange(HEIGHT - self.rect.width)
            self.speedx = random.randrange(3, 8)

class Mobright(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(mob_img, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(500, 550)
        self.rect.y = random.randrange(HEIGHT - self.rect.width)
        self.speedx = random.randrange(3, 8)
    def update(self):
        self.rect.x -= self.speedx
        if self.rect.right < 0:
            self.rect.x = random.randrange(500, 550)
            self.rect.y = random.randrange(HEIGHT - self.rect.width)
            self.speedx = random.randrange(3, 8)

background = pygame.image.load(path.join(img_dir, "shmuppracbg.jpg"))
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "hud_p1.png"))
mob_img = pygame.image.load(path.join(img_dir, "hud_p2.png"))

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
mobs = pygame.sprite.Group()

for i in range(5):
    mu = Mobup()
    all_sprites.add(mu)
    mobs.add(mu)

for i in range(3):
    ml = Mobleft()
    all_sprites.add(ml)
    mobs.add(ml)

for i in range(3):
    mr = Mobright()
    all_sprites.add(mr)
    mobs.add(mr)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False

    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
