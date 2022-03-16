import pygame
import random

WIDTH = 500
HEIGHT = 500

EGG_HEIGHT = 37
EGG_WIDTH = 30

BASKET_HEIGHT = 80
BASKET_WIDTH = 80

BASKET_VEL = 7


class egg:
    def __init__(self):
        self.rec = pygame.Rect(
            random.uniform(0, WIDTH - EGG_WIDTH),
            0 - EGG_HEIGHT,
            EGG_WIDTH,
            EGG_HEIGHT,
        )

    def check_egg(self):
        if self.rec.y > HEIGHT - EGG_HEIGHT:
            return False
        else:
            return True
    
    def check_coll(self,basket):
        if self.rec.colliderect(basket.rec):
            return True
        else:
            return False


class bask:
    def __init__(self):
        self.rec = pygame.Rect(
            (WIDTH - BASKET_HEIGHT) / 2,
            HEIGHT - BASKET_HEIGHT,
            BASKET_WIDTH,
            BASKET_HEIGHT,
        )

    def movement(self, dir):
            if dir == "r" and self.rec.x < (WIDTH - BASKET_WIDTH):
                self.rec.x += BASKET_VEL
            if dir == "l" and self.rec.x > 0 :
                self.rec.x -= BASKET_VEL
