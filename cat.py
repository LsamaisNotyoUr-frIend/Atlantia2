# write = input(">")
# digits = {
#     '1': "one",
#     '2': 'two',
#     '3': 'three',
#     '4': 'four',
# }
# output = ""
# for keys in write:
#     output += digits.get(keys, '!') + ' '
# print(output)
# class Person:
#
#     def __init__(self, name):
#         self.name = name
#
#     def ment(self):
#         print(f'{self.name} you are mad!')
#
#
# me = Person('george')
# me.ment()
#
#
# class Ment(Person):
#
#     @staticmethod
#     def holders():
#         abomination = 5
#         print(f' you are {abomination} years old')
#
#
# me = Ment
# me.holders()
#
# from hat import rog
# rog()
# from hat import aminu
# nos = [5, 17, 3, 298, 53, 390, 7]
# print(max(nos))
# # man = aminu(nos)
# print(man)
# import random
# for members in range(2):
#     print(random. randint(1,6))
# import random
#
#
# class Items:
#     def roll(self):
#         first_number = random.randint(1, 6)
#         second_number = random.randint(1, 6)
#         return first_number, second_number
#
#
# dice = items()
# print(dice.roll())
# from pathlib import Path
# path = Path()
# for file in path.glob('*'):
#     print(file)

import pygame
import pygame_gui
import pymunk
import random
from sys import exit

pygame.init()
clock = pygame.time.Clock()

tab_with = 1100
tab_height = 650

ball = pygame.Rect(tab_with / 2 - 4, tab_height / 2 - 5, 15, 15)
opponent = pygame.Rect((tab_with - 5), tab_height / 2 - 35, 5, 70)
player = pygame.Rect(0, tab_height / 2 - 35, 5, 70)
tab = pygame.display.set_mode((tab_with, tab_height))
pygame.display.set_caption('Super pong')
icon = pygame.image.load('Block-a.svg')
pygame.display.set_icon(icon)

tab.fill((255, 107, 46))
score = 0
score1 = 0


class BallAnima:
    def __init__(self):
        self.ball_speed_x = 5 * random.choice((-1, 1))
        self.ball_speed_y = 5 * random.choice((-1, 1))

    def update(self):
        ball.x += self.ball_speed_x
        ball.y += self.ball_speed_y

        if ball.top <= 0 or ball.bottom >= tab_height:
            self.ball_speed_y *= -1
        if ball.left <= -4:
            self.ball_restart()
        if ball.right >= tab_with + 5:
            self.ball_restart()
        if ball.colliderect(player):
            self.ball_speed_x *= -1
        if ball.colliderect(player) and ball.left <= 1:
            self.ball_restart()
        if ball.colliderect(opponent):
            self.ball_speed_x *= -1

    @staticmethod
    def player_anima():
        player.y += player_speed
        # player1.y += player1_speed
        if player.top <= 0:
            player.top = 0
        if player.bottom >= tab_height:
            player.bottom = tab_height

    @staticmethod
    def opp_anima():
        if opponent.top < ball.top:
            opponent.top += (opponent_speed + random.choice((4.9, 6, 4.5, 5, 7, 4.1)))
        if opponent.bottom > ball.bottom:
            opponent.top -= (opponent_speed + random.choice((4.9, 6, 4.5, 5, 7, 4.1)))

    def ball_restart(self):
        ball.center = (tab_with / 2, tab_height / 2)
        self.ball_speed_y *= random.choice((1, -1))
        self.ball_speed_x *= random.choice((1, -1))


player_speed = 0
player1_speed = 0
opponent_speed = 0
opponent1_speed = 15
font = pygame.font.Font('Kenia-Regular.ttf', 50)
surface = font.render('Super pong', False, 'Grey')

font1 = pygame.font.Font('Kenia-Regular.ttf', 30)

animation_ball = BallAnima()
animation_player = BallAnima()
animation_opponent = BallAnima()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player_speed += 10
            if event.key == pygame.K_e:
                player_speed -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player_speed -= 10
            if event.key == pygame.K_e:
                player_speed += 10
    animation_ball.update()
    animation_player.player_anima()
    animation_opponent.opp_anima()

    tab.fill((0, 0, 0))
    pygame.draw.circle(tab, (255, 255, 255), ((tab_with / 2), (tab_height / 2)), 150, 5)
    pygame.draw.aaline(tab, (255, 255, 255), (tab_with / 2, 0), (tab_with / 2, tab_height))
    pygame.draw.aaline(tab, (255, 255, 255), (tab_with / 1.995, 0), (tab_with / 1.995, tab_height))
    pygame.draw.aaline(tab, (255, 255, 255), (tab_with / 1.9909, 0), (tab_with / 1.9909, tab_height))
    pygame.draw.ellipse(tab, (200, 200, 200), ball)
    pygame.draw.rect(tab, (200, 200, 200), player,)
    pygame.draw.rect(tab, (200, 200, 200), opponent)
    if ball.left <= 0:
        score1 += 1
    if ball.right >= tab_with + 3:
        score += 1

    score_text1 = font1.render('score:' + str(score), True, 'Green')
    score_text2 = font1.render('score:' + str(score1), True, 'White')

    tab.blit(score_text1, (100, 100))
    tab.blit(score_text2, ((tab_with - 100), 100))
    tab.blit(surface, ((tab_with / 2 - 110), 100))

    pygame.display.update()

    clock.tick(120)




