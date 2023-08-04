import pygame

class Enemy:
    def __init__(self, x, y, s):
        self.img = pygame.image.load(".\\테스트_적.png")
        self.x=x
        self.y=y
        self.rect = self.img.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y
        self.s = s
        self.size = self.img.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.move = True
        self.damage = 10
        self.attack = True
        self.attack_time = 0
        self.attack_ready_time = 1.5
        self.hp = 10
        self.is_hp_boss = False
        self.is_xp_boss = False

    # def attack(self, damage):
    #     self.damage = damage
