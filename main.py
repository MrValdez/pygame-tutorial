# main.py
import os
import pygame
from gameobject import Shot, Hero

os.environ["SDL_VIDEO_WINDOW_POS"] = "0,20"
resolution = (1280, 768)
isRunning = True

pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Courier New", 18)

hero = Hero([0, 0])
shots = []

while isRunning:
    screen.fill((255, 255, 255))
    tick = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

        if event.type == pygame.QUIT:
            isRunning  = False

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_SPACE]:
        new_shot = Shot(hero.pos)
        shots.append(new_shot)

    hero.update()
    for shot in shots:
        shot.update()

    hero.draw(screen)
    for shot in shots:
        shot.draw(screen)

    text = font.render("Hello world", False, (0, 0, 0))
    screen.blit(text, (0, 0))

    pygame.display.flip()

pygame.quit()