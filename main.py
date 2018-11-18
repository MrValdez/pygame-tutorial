import pygame

resolution = (640, 480)
isRunning = True

pygame.init()
screen = pygame.display.set_mode(resolution)

hero = pygame.image.load("hero.png")
hero_pos = [0, 0]

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

        if event.type == pygame.QUIT:
            isRunning  = False

    screen.blit(hero, hero_pos)

    pygame.display.flip()

pygame.quit()