import pygame

resolution = (640, 480)
isRunning = True

pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

hero = pygame.image.load("hero.png").convert()
hero.set_colorkey((255, 128, 128))
hero_pos = [0, 0]

while isRunning:
    screen.fill((255, 255, 255))
    tick = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

        if event.type == pygame.QUIT:
            isRunning  = False

    hero_pos[0] += 10
    hero_pos[1] += 10

    screen.blit(hero, hero_pos)

    pygame.display.flip()

pygame.quit()