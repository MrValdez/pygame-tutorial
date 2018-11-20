# main.py
import os
import pygame
import random
from gameobject import Shot, Hero, Enemy

os.environ["SDL_VIDEO_WINDOW_POS"] = "0,20"
resolution = (1280, 768)
isRunning = True

pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Courier New", 18)

hero = Hero([0, 0])
shots = []
enemies = []
world = [[hero], shots, enemies]

def spawn_enemy():
    pos = [random.randint(3000, 10000), random.randint(-10, resolution[1] - 100)]
    enemy = Enemy(pos)
    enemies.append(enemy)

for i in range(50):
    spawn_enemy()

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

    text_str = f"Enemies in game: {len(enemies)}"
    text = font.render(text_str, False, (0, 0, 0))
    screen.blit(text, (200, 200))

    for object_group in world:
        for object in object_group:
            object.update()

    for object_group in world:
        for object in object_group:
            object.draw(screen)

    pygame.display.flip()

pygame.quit()