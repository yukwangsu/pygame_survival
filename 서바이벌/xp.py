import pygame

class Xp:
    def __init__(self, x, y):
        self.img = pygame.image.load(".\\테스트_경험치.png")
        self.x = x
        self.y = y
        self.rect = self.img.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y
        self.size = self.img.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]