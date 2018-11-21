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

hero = Hero([0, 20])
shots = []
enemies = []
world = [[hero], shots, enemies]

def spawn_enemy():
    pos = [random.randint(100, 10000), random.randint(-10, resolution[1] - 100)]
    enemy = Enemy(pos)
    enemies.append(enemy)

for i in range(50):
    spawn_enemy()

def check_collision(box1_pos, box1_size,
                    box2_pos, box2_size):
    return (box1_pos[0] + box1_size[0] > box2_pos[0] and
            box1_pos[0] < box2_pos[0] + box2_size[0] and
            box1_pos[1] + box1_size[1] > box2_pos[1] and
            box1_pos[1] < box2_pos[1] + box2_size[1])

def update_world():
    for shot in shots:
        if shot.pos[0] > resolution[0]:
            shots.remove(shot)
            continue
    
        for enemy in enemies:
            has_collided = check_collision(shot.pos, shot.image.get_size(),
                                           enemy.pos, enemy.image.get_size())
            if has_collided:
               enemies.remove(enemy)
               shots.remove(shot)
               break

class Input():
    def __init__(self):
        self.prev_keydown = self.current_keydown = pygame.key.get_pressed()

    def update(self):
        self.prev_keydown = self.current_keydown
        self.current_keydown = pygame.key.get_pressed()

    def is_hold(self, key):
        return self.current_keydown[key]

    def is_down(self, key):
        return self.current_keydown[key] and not self.prev_keydown[key]

    def is_up(self, key):
        return not self.current_keydown[key] and self.prev_keydown[key]

input = Input()

while isRunning:
    screen.fill((255, 255, 255))
    tick = clock.tick(8)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

        if event.type == pygame.QUIT:
            isRunning  = False

    input.update()
    if input.is_down(pygame.K_SPACE):
        new_shot = Shot(hero.pos)
        shots.append(new_shot)

    text_str = f"Enemies in game: {len(enemies)}"
    text = font.render(text_str, False, (0, 0, 0))
    screen.blit(text, (200, 200))

    for object_group in world:
        for object in object_group:
            object.update()

    update_world()

    for object_group in world:
        for object in object_group:
            object.draw(screen)

    button_hold = "Yes" if input.is_hold(pygame.K_SPACE) else "No "
    button_down = "Yes" if input.is_down(pygame.K_SPACE) else "No "
    button_up = "Yes" if input.is_up(pygame.K_SPACE) else "No "

    text_str = f"Button held: {button_hold}    Button down: {button_down}    Button up: {button_up}"
    text = font.render(text_str, False, (0, 0, 0))
    screen.blit(text, (10, 0))

    pygame.display.flip()

pygame.quit()