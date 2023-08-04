import pygame

class Attack:
    def __init__(self):
        self.img = pygame.image.load(".\\테스트_attack_2.png")
        self.learn = False
        self.x = 0
        self.y = 0
        self.rect = self.img.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y
        self.size = self.img.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.damage = 10
        self.attack = True
        self.attack_time = 0
        self.attack_ready_time = 2.5
        self.attack_motion = False
        self.attack_motion_remain_time = 0.15
        # self.attack_direction = 2     # 0: 좌 / 1: 우 / 2: 양쪽
        self.attack_direction_check = False
        self.level = 1

    # def damage(self):
    #     if self.level == 2:
    #         self.damage = 15
    #     elif self.level == 3:
    #         self.damage = 20