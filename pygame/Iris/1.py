import pygame
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 500, 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gotta Cathc 'em all!")
YELLOW = (255, 255, 0)

FPS = 60
POKEBAL = pygame.image.load("pok.png")
POKEBALL = pygame.transform.scale(POKEBAL, (40, 40))
BALL_VEL = 5

SPRIT = pygame.image.load("sprite.png")
SPRITE = pygame.transform.scale(SPRIT, (80, 80))

TARGE = pygame.image.load("target.png")
TARGET = pygame.transform.scale(TARGE, (80, 80))

MO = pygame.image.load("axew.png")
MON = pygame.transform.scale(MO, (60, 60))

FONT1 = pygame.font.SysFont("comicsans", 15)
FONT2 = pygame.font.SysFont("comicsans", 50)


def set_sprite():
    pygame.draw.line(WIN, (0, 0, 0), (0, (HEIGHT / 2) - 45), (83, (HEIGHT / 2) - 45), 3)
    pygame.draw.line(WIN, (0, 0, 0), (0, (HEIGHT / 2) + 45), (83, (HEIGHT / 2) + 45), 3)
    pygame.draw.line(
        WIN, (0, 0, 0), (83, (HEIGHT / 2) - 45), (83, (HEIGHT / 2) + 45), 3
    )
    WIN.blit(SPRITE, (0, (HEIGHT / 2) - 40))


def draw(balls, max_balls, score):
    WIN.fill(YELLOW)
    set_sprite()
    text1 = FONT1.render("Balls:" + str(max_balls), 1, (0, 0, 255))
    text2 = FONT1.render("Caught:" + str(score), 1, (0, 0, 255))
    WIN.blit(text1, (0, 0))
    WIN.blit(text2, (text1.get_width() + 10, 0))
    for ball in balls:
        WIN.blit(POKEBALL, (ball.x, ball.y))


def handle_balls(balls, posx, posy):
    for ball in balls:
        if all([ball.x < WIDTH, ball.x < posx, ball.y < HEIGHT, ball.y > 0]):
            ball.x += BALL_VEL
            ball.y += (BALL_VEL * ((posy - HEIGHT / 2) / (posx - 83))) + 1
        else:
            balls.remove(ball)


def handle_target(posx, posy):
    if all([posx, posy]):
        WIN.blit(TARGET, (posx, posy))
    pygame.display.update()


def create_Mon():
    import random

    t = time.time()
    return (
        pygame.Rect(random.uniform(100, 350), random.uniform(0, HEIGHT - 60), 60, 60),
        t,
    )


def handle_Mon(mons, rec):
    if mons:
        WIN.blit(MON, (rec.x, rec.y))


def check_coll(Mrec, balls, score, time):
    for ball in balls:
        if Mrec.colliderect(ball):
            score += 1
            Mons_rec, t = create_Mon()
            axew_sound = pygame.mixer.Sound("axew.mp3")
            axew_sound.play()
            balls.remove(ball)
            return score, Mons_rec, t
    return score, Mrec, time


def endgame(score):
    textB = FONT2.render("Game Ended", 1, (0, 0, 0))
    textA = FONT2.render("Your Score:" + str(score), 1, (0, 0, 0))
    WIN.blit(textB, ((WIDTH - textB.get_width()) / 2, 0))
    WIN.blit(textA, ((WIDTH - textA.get_width()) / 2, textB.get_height() + 5))
    pygame.display.update()

    pygame.time.delay(5000)


def main():
    clock = pygame.time.Clock()
    score = 0
    max_balls = 10
    run = True
    balls = []
    posx = posy = None
    mons = True
    Mons_rec, t = create_Mon()
    pygame.mixer.music.load("theme.mp3")
    pygame.mixer.music.play(-1, 0, 0)

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and posx and posy:
                    rec = pygame.Rect(83, HEIGHT / 2 - 20, 40, 40)
                    balls.append(rec)
                    max_balls -= 1

            if event.type == pygame.MOUSEBUTTONUP:
                posx, posy = pygame.mouse.get_pos()
                posx -= 34
                posy -= 32

        if time.time() - t >= 3:
            Mons_rec, t = create_Mon()

        if max_balls < 0:
            endgame(score)
            break

        while score + max_balls > 10:
            score -= 1

        handle_balls(balls, posx, posy)
        draw(balls, max_balls, score)
        handle_Mon(mons, Mons_rec)
        score, Mons_rec, t = check_coll(Mons_rec, balls, score, t)
        handle_target(posx, posy)

    pygame.quit()


if __name__ == "__main__":
    main()
