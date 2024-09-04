import pygame
from sprites import *
pygame.init()

class Game(object):
    def __init__(self):
        print("Initializing...")
        # create screen
        self.screen = pygame.display.set_mode(SCREEN.size)
        # create clock
        self.clock = pygame.time.Clock()
        # create sprites groups
        self.sprites()
        # create set_timer
        pygame.time.set_timer(BOOK_EVENT, 1000)
        pygame.time.set_timer(STAR_EVENT, 500)

    def sprites(self):
        b1 = Background()
        b2 = Background(True)
        self.back_group = pygame.sprite.Group(b1, b2)
        self.homework_group = pygame.sprite.Group()
        self.nyusher = NYUSHer()
        self.nyusher_community = pygame.sprite.Group(self.nyusher)

    def start(self):
        print("Initializing...")
        while True:
            self.clock.tick(FRAME)
            self.event()
            self.check()
            self.update()
            pygame.display.update()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.game_over()
            elif event.type == BOOK_EVENT:
                quiz = Quiz()
                essay = Essay()
                due = Due()
                self.homework_group.add(quiz)
                self.homework_group.add(essay)
                self.homework_group.add(due)
            elif event.type == STAR_EVENT:
                self.nyusher.shoot_star()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.nyusher.speed = 15
        elif keys[pygame.K_LEFT]:
            self.nyusher.speed = -15
        else:
            self.nyusher.speed = 0

    def check(self):
        pygame.sprite.groupcollide(self.nyusher.stars, self.homework_group, True, True)
        homework = pygame.sprite.spritecollide(self.nyusher, self.homework_group, True)
        if len(homework) >0:
            self.nyusher.kill()
            Game.game_over()
    def update(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.homework_group.update()
        self.homework_group.draw(self.screen)
        self.nyusher_community.update()
        self.nyusher_community.draw(self.screen)
        self.nyusher.stars.update()
        self.nyusher.stars.draw(self.screen)


    def game_over():
        print("Game Over...")
        pygame.quit()
        exit()
if __name__ == '__main__':
    game = Game()
    game.start()