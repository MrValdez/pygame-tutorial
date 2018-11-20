# gameobject.py
import pygame
import random

class GameObject:
    def __init__(self, filename, pos):
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((255, 128, 128))

        self.pos = pos[:]

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def update(self):
        pass

class Hero(GameObject):
    def __init__(self, pos):
        super().__init__("hero.png", pos)
        self.speed = 10

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.pos[0] -= self.speed
        if keystate[pygame.K_RIGHT]:
            self.pos[0] += self.speed
        if keystate[pygame.K_UP]:
            self.pos[1] -= self.speed
        if keystate[pygame.K_DOWN]:
            self.pos[1] += self.speed

class Shot(GameObject):
    def __init__(self, pos):
        super().__init__("shot.png", pos)
        self.pos[0] += 200
        self.pos[1] += 50

        self.speed = random.randint(1, 20)

    def update(self):
        self.pos[0] += self.speed

class Enemy(GameObject):
    def __init__(self, pos):
        super().__init__("enemy.png", pos)

        self.speed = random.randint(10, 50)

    def update(self):
        self.pos[0] -= self.speed