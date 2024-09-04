import random
import pygame

SCREEN = pygame.Rect(0, 0, 724, 900)
FRAME = 60
BOOK_EVENT = pygame.USEREVENT
STAR_EVENT = pygame.USEREVENT + 1

class ALLSprite(pygame.sprite.Sprite):
    def __init__(self, image, speed=1):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed
    def update(self):
        self.rect.y += self.speed

class Background(ALLSprite):
    def __init__(self, is_image2 =False):
        super().__init__("./IMAGES_/Background.jpg")
        if is_image2:
            self.rect.x = -self.rect.width
    def update(self):
        self.rect.x += self.speed
        if self.rect.x >= SCREEN.width:
            self.rect.x = -self.rect.width

class Quiz(ALLSprite):
    def __init__(self):
        super().__init__("./IMAGES_/quiz.png")
        self.speed = random.randint(1, 3)
        max = SCREEN.width - self.rect.width
        self.rect.x = random.randint(0, max)
    def update(self):
        super().update()

class Essay(ALLSprite):
    def __init__(self):
        super().__init__("./IMAGES_/essay.png")
        self.speed = random.randint(1, 3)
        max = SCREEN.width - self.rect.width
        self.rect.x = random.randint(0, max)
    def update(self):
        super().update()

class Due(ALLSprite):
    def __init__(self):
        super().__init__("./IMAGES_/due.png")
        self.speed = random.randint(1, 3)
        max = SCREEN.width - self.rect.width
        self.rect.x = random.randint(0, max)
    def update(self):
        super().update()

class Star(ALLSprite):
    def __init__(self):
        super().__init__("./IMAGES_/star.png", -5)
    def update(self):
        super().update()

class NYUSHer(ALLSprite):
    def __init__(self):
        super().__init__("./IMAGES_/nyusher.png", 0)
        self.rect.x = SCREEN.width/2
        self.rect.bottom = SCREEN.bottom - 20
        self.stars = pygame.sprite.Group()
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > SCREEN.right:
            self.rect.right = SCREEN.right
    def shoot_star(self):
        for i in (0, 1):
            star = Star()
            star.rect.bottom = self.rect.y - i * 50
            star.rect.x = self.rect.x
            self.stars.add(star)

