import pygame

resolution = (640, 480)
isRunning = True

pygame.init()
screen = pygame.display.set_mode(resolution)

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

        if event.type == pygame.QUIT:
            isRunning  = False

    pygame.display.flip()

pygame.quit()