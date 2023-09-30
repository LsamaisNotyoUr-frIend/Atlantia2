import pygame
import pygame_gui
import pymunk
import random
from sys import exit

pygame.init()
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
player = pygame.Rect(0, (screen_height / 2 - 35), 5, 70)
opponent = pygame.Rect((screen_width - 5), (screen_height / 2 - 35), 10, 70)
ball = pygame.Rect(screen_width / 2 - 7.5, screen_height / 2 - 7.5, 15, 15)

pygame.display.set_caption('Super pong')
icon = pygame.image.load('Block-a.svg')
pygame.display.set_icon(icon)

clock = pygame.Clock()


class RudementryStuff:
    def __init__(self):
        self.ball_speed_y = 5 * random.choice((-1, 1))
        self.ball_speed_x = 5 * random.choice((-1, 1))

    def ball_animation(self):
        ball.y += self.ball_speed_y
        ball.x += self.ball_speed_x

        if ball.top <= 0 or ball.bottom >= screen_height:
            self.ball_speed_y *= -1
        if ball.left <= -5:
            self.restart()
        if ball.right >= screen_width + 5:
            self.restart()
        if ball.colliderect(player):
            self.ball_speed_x *= -1
        if ball.colliderect(opponent):
            self.ball_speed_x *= -1

    @staticmethod
    def player_animation():
        player.y += player_speed
        if player.top <= 0:
            player.top = 0
        if player.bottom >= screen_height:
            player.bottom = screen_height

    @staticmethod
    def opponent_animation():
        if opponent.top < ball.y:
            opponent.top += opponent_speed + 4.99999999
        if opponent.y > ball.bottom:
            opponent.top -= opponent_speed + 4.99999999
        # opponent.y = ball.y

    def restart(self):
        ball.center = ((screen_width * 0.5), (screen_height * 0.5))
        self.ball_speed_x *= random.choice((1, -1))
        self.ball_speed_y *= random.choice((1, -1))


player_speed = 0
opponent_speed = 0

animations = RudementryStuff()
animations1 = RudementryStuff()
animations2 = RudementryStuff()

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_e:
                player_speed -= 10
            if events.key == pygame.K_d:
                player_speed += 10
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_e:
                player_speed += 10
            if events.key == pygame.K_d:
                player_speed -= 10

    animations.ball_animation()
    animations1.player_animation()
    animations2.opponent_animation()

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), ((screen_width / 2), (screen_height / 2)), 135, 7)
    pygame.draw.aaline(screen, (255, 255, 255), (screen_width / 2, 0), (screen_width / 2, 600), 10)
    pygame.draw.aaline(screen, (255, 255, 255), (screen_width - 401.5, 0), (screen_width - 401.5, 600), 10)
    pygame.draw.aaline(screen, (255, 255, 255), (screen_width - 403, 0), (screen_width - 403, 600), 10)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255, 255, 255), opponent)

    pygame.display.update()
    clock.tick(120)
