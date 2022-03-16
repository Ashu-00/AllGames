import pygame
from classes import *

pygame.init()
pygame.mixer.init()
pygame.font.init()


FPS = 60

WIDTH = 500
HEIGHT = 500

EGG = pygame.transform.scale(pygame.image.load("egg.png"), (EGG_WIDTH, EGG_HEIGHT))
BASKET = pygame.transform.scale(
    pygame.image.load("basket.png"), (BASKET_WIDTH, BASKET_HEIGHT)
)
BACKGROUND = pygame.transform.scale(
    pygame.image.load("background.jpg"), (WIDTH, HEIGHT)
)

EGG_VEL = 5
BASKET_VEL = 7

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("EGG Catcher")

p_sound = pygame.mixer.Sound("point_sound.mp3")
h_sound = pygame.mixer.Sound("egg_sound.mp3")

FONT1 = pygame.font.SysFont("fixedsys", 20)


def check_eggs(eggs, health):
    for egg in eggs:
        if egg.check_egg():
            egg.rec.y += EGG_VEL
        else:
            eggs.remove(egg)
            health -= 1
            h_sound.play()
    return eggs, health


def draw(eggs, basket, health, points):
    WIN.fill((0, 0, 0))
    WIN.blit(BACKGROUND, (0, 0))
    for egg in eggs:
        WIN.blit(EGG, (egg.rec.x, egg.rec.y))
    WIN.blit(BASKET, (basket.rec.x, basket.rec.y))
    text1 = FONT1.render("Health:" + str(health), 1, (255, 0, 0))
    text2 = FONT1.render("Score:" + str(points), 1, (0, 255, 0))
    WIN.blit(text2, (0, 0))
    WIN.blit(text1, (WIDTH - text1.get_width(), 0))


def basket_move(KP, basket):
    if KP[pygame.K_RIGHT]:
        basket.movement("r")
    if KP[pygame.K_LEFT]:
        basket.movement("l")


def check_coll(basket, eggs, points):
    for egg in eggs:
        if egg.check_coll(basket):
            eggs.remove(egg)
            points += 1
            p_sound.play()
        else:
            pass
    return eggs, points


def main():
    global BASKET_VEL

    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.play(-1, 0, 0)

    run = True
    clock = pygame.time.Clock()
    eggs = []
    basket = bask()
    time = pygame.time.get_ticks()
    n = 1
    health = 10
    points = 0

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

                break

        if health == 0:

            pygame.quit()
            import sys

            sys.exit()

        x = pygame.time.get_ticks() - time
        if x > 1000 / n:
            egg1 = egg()
            eggs.append(egg1)
            time = pygame.time.get_ticks()
            n += n / 100
            BASKET_VEL += 0.001 * n / 1000

        KP = pygame.key.get_pressed()

        basket_move(KP, basket)
        eggs, health = check_eggs(eggs, health)
        eggs, points = check_coll(basket, eggs, points)
        draw(eggs, basket, health, points)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
