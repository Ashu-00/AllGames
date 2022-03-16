import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

from player import Player

FPS = 60

FONT1 = pygame.font.SysFont("courier new", 30)
FONT2 = pygame.font.SysFont("Calibri", 50, True)

WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TAG")

BG = pygame.transform.scale(
    pygame.image.load("./assets/background/ocean.jfif"), (WIDTH, HEIGHT)
)

red = Player("red")
green = Player("green")

WASD = pygame.transform.scale(
    (pygame.image.load("./assets/keys_img/wasd-keys.png").convert_alpha()), (100, 100)
)
ULDR = pygame.transform.scale(
    (pygame.image.load("./assets/keys_img/download.png").convert_alpha()), (100, 100)
)

points = 0

BEEP = pygame.mixer.Sound("./assets/sounds/beep.mp3")
ENTER=pygame.mixer.Sound(r".\assets\sounds\enter.mp3")


def draw():
    WIN.blit(BG, (0, 0))
    WIN.blit(red.player, (red.rect.x, red.rect.y))
    WIN.blit(green.player, (green.rect.x, green.rect.y))
    text = FONT1.render("Points:" + str(points), 1, (0, 0, 0))
    WIN.blit(text, (((WIDTH - text.get_width()) / 2), 0))

    pygame.display.update()


def check_coll():
    global points
    if green.rect.colliderect(red.rect):
        points += 1
        BEEP.play()
        red.rect.x, red.rect.y, green.rect.x, green.rect.y = (
            0,
            0,
            WIDTH - green.player.get_width(),
            HEIGHT - green.player.get_height(),
        )
    else:
        pass


def start_screen(run,clock):
    clock.tick(FPS)
    WIN.blit(BG, (0, 0))
    textRed = FONT2.render("RED", 1, (255, 0, 0))
    text = FONT2.render("catches", 1, (0, 0, 0))
    textGreen = FONT2.render("GREEN", 1, (0, 0, 255))

    WIN.blit(textGreen, (200, 0))
    WIN.blit(text, (200, textGreen.get_width() + 5))
    WIN.blit(textRed, (200, textGreen.get_width() + text.get_width() + 10))

    WIN.blit(WASD, (200 + textGreen.get_width() + 10, 0))
    WIN.blit(
        ULDR,
        (
            200 + textGreen.get_width() + 10,
            textGreen.get_width() + text.get_width() + 10,
        ),
    )

    StartText = FONT2.render("START", 1, (0, 0, 0))
    WIN.blit(StartText, (600, textGreen.get_width() + text.get_width() + 10))
    rectangle = pygame.draw.rect(
        WIN,
        (0, 0, 0),
        pygame.Rect(
            595,
            textGreen.get_width() + text.get_width() + 5,
            StartText.get_width() + 10,
            StartText.get_height() + 5,
        ),
        4,
        1,
        1,
        1,
        1,
        1,
    )

    QuitText = FONT2.render("EXIT", 1, (0, 0, 0))
    WIN.blit(
        QuitText,
        (615, textGreen.get_width() + text.get_width() + StartText.get_width() + 20),
    )
    rectangle2 = pygame.draw.rect(
        WIN,
        (0, 0, 0),
        pygame.Rect(
            595,
            textGreen.get_width() + text.get_width() + StartText.get_width() + 15,
            StartText.get_width() + 10,
            StartText.get_height() + 5,
        ),
        4,
        1,
        1,
        1,
        1,
        1,
    )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            import sys

            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if rectangle.collidepoint(pos):
                run = False
                ENTER.play()
            if rectangle2.collidepoint(pos):
                run = False
                ENTER.play()
                pygame.quit()
                import sys
                sys.exit()

    pygame.display.update()
    return run


def main():
    pygame.mixer.music.load("./assets/sounds/bg_song.mp3")
    pygame.mixer.music.play(-1, 0, 0)

    run = True
    clock = pygame.time.Clock()
    while run:
        run = start_screen(run,clock)

    red.rect.x, red.rect.y, green.rect.x, green.rect.y = (
        0,
        0,
        WIDTH - green.player.get_width(),
        HEIGHT - green.player.get_height(),
    )

    global points

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        red.move()
        green.move()

        check_coll()

        draw()

    pygame.quit()


if __name__ == "__main__":
    main()
