import os
import pygame
import pygame_gui
from sys import exit

pygame.init()

wind_width = 1000
wind_height = 600
lindow = pygame.display.set_mode((wind_width, wind_height))
pygame.display.set_caption("my tester")

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, 'my sprite gif.gif')
image = pygame.image.load(image_path)
sage = pygame.image.load('snd.png')

sage = sage.convert_alpha()


font = pygame.font.Font('Kenia-Regular.ttf', 50)
surface = font.render('Tales Of Atlantia', False, (101, 67, 33))

flipped_image = pygame.transform.flip(image, True, False)
otherFlipped_image = pygame.transform.flip(image, False, True)

sprite_pos = image.get_rect()
sprite_pos.x = 100
sprite_pos.y = 100
sprite_speed = 10

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    image = pygame.image.load(image_path)
    colour = (255, 253, 208)
    image = image.convert_alpha()

    # image.set_colorkey(255, 253, 208)
    image.fill((255, 253, 208), special_flags=pygame.BLEND_MULT)
    sage.fill((255, 253, 208), special_flags=pygame.BLEND_MULT)
    # image = image.convert_alpha()
    image = pygame.transform.scale(image, (125, 100))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        sprite_pos.x -= sprite_speed
    elif keys[pygame.K_f]:
        sprite_pos.x += sprite_speed
    elif keys[pygame.K_e]:
        sprite_pos.y -= sprite_speed
    elif keys[pygame.K_d]:
        sprite_pos.y += sprite_speed

#off screen
    if sprite_pos.x <= -30:
        sprite_pos.x = -25
    if sprite_pos.x >= 900:
        sprite_pos.x = 900
    if sprite_pos.y <= -30:
        sprite_pos.y = -25
    if sprite_pos.y >= 500:
        sprite_pos.y = 500

    lindow.fill((155, 255, 255))
    lindow.blit(image, sprite_pos)
    lindow.blit(surface, (320, 100))
    # lindow.blit(sage, sprite_pos)
    # rectangle_colour = (0, 255, 0)
    # rectangle_pos = (500, 400)
    # rectangle_size = (300, 100)
    # pygame.draw.rect(window,rectangle_colour,(rectangle_pos, rectangle_size))

    pygame.display.flip()

    clock.tick(60)


