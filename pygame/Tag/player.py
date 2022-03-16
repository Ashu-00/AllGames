import pygame


class Player:
    WIDTH = 800
    HEIGHT = 600
    PLAYER_VEL = 5

    def __init__(self, color):
        self.color = color
        if color == "red":
            self.player = pygame.image.load("./assets/players/red.png").convert_alpha()
            self.player = pygame.transform.scale(self.player, (30, 30))
        else:
            self.player = pygame.image.load(
                "./assets/players/green.png"
            ).convert_alpha()
            self.player = pygame.transform.scale(self.player, (30, 30))
        self.rect = self.player.get_rect()

    def move(self):
        if self.color == "red":
            up = pygame.K_KP8
            down = pygame.K_KP2
            right = pygame.K_KP6
            left = pygame.K_KP4
        else:
            up = pygame.K_w
            down = pygame.K_s
            right = pygame.K_d
            left = pygame.K_a

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[up] and self.rect.y >= 0:
            self.rect.y -= Player.PLAYER_VEL
        if (
            keys_pressed[down]
            and self.rect.y < Player.HEIGHT - self.player.get_height()
        ):
            self.rect.y += Player.PLAYER_VEL
        if keys_pressed[right] and self.rect.x < Player.WIDTH - self.player.get_width():
            self.rect.x += Player.PLAYER_VEL
        if keys_pressed[left] and self.rect.x >= 0:
            self.rect.x -= Player.PLAYER_VEL
