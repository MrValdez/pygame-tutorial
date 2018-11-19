# main.py
import pygame

class Shot:
    def __init__(self, pos):
        self.image = pygame.image.load("shot.png").convert()
        self.image.set_colorkey((255, 128, 128))

        pos = pos[:]
        pos[0] += 200
        pos[1] += 50

        self.pos = pos

    def draw(self, screen):
        screen.blit(self.image, self.pos)

resolution = (640, 480)
isRunning = True

pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

hero = pygame.image.load("hero.png").convert()
hero.set_colorkey((255, 128, 128))
hero_pos = [0, 0]

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
    if keystate[pygame.K_LEFT]:
        hero_pos[0] -= 10
    if keystate[pygame.K_RIGHT]:
        hero_pos[0] += 10
    if keystate[pygame.K_UP]:
        hero_pos[1] -= 10
    if keystate[pygame.K_DOWN]:
        hero_pos[1] += 10
    if keystate[pygame.K_SPACE]:
        new_shot = Shot(hero_pos)
        shots.append(new_shot)

    screen.blit(hero, hero_pos)
    
    for shot in shots:
        shot.draw(screen)

    pygame.display.flip()

pygame.quit()