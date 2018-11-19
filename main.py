import pygame

resolution = (640, 480)
isRunning = True

pygame.init()
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

hero = pygame.image.load("hero.png").convert()
hero.set_colorkey((255, 128, 128))
hero_pos = [0, 0]

shot = pygame.image.load("shot.png").convert()
shot.set_colorkey((255, 128, 128))
shot_pos = [-100, -100]

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
        shot_pos = hero_pos[:]
        shot_pos[0] += 200
        shot_pos[1] += 50

    screen.blit(hero, hero_pos)
    screen.blit(shot, shot_pos)

    pygame.display.flip()

pygame.quit()