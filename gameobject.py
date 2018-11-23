# gameobject.py
import pygame
import random
import math

def magnitude(vector):
    return math.sqrt((vector[0] * vector[0]) + (vector[1] * vector[1]))

def normalize(vector):
    mag = magnitude(vector)
    return [vector[0] / mag, vector[1] / mag]

class GameObject:
    def __init__(self):
        pass

    def draw(self, screen):
        pass

    def update(self):
        pass

    def get_size(self):
        return [0, 0]

class Particle(GameObject):
    def __init__(self):
        pass

class Sprite(GameObject):
    def __init__(self, filename, pos):
        super().__init__()

        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((255, 128, 128))

        self.pos = pos[:]

    def draw(self, screen):
        screen.blit(self.image, self.pos)

    def update(self):
        pass

    def get_size(self):
        return self.image.get_size()

class Hero(Sprite):
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

class Shot(Sprite):
    def __init__(self, pos):
        super().__init__("shot.png", pos)
        self.pos[0] += 200
        self.pos[1] += 50

        self.speed = random.randint(1, 20)

    def update(self):
        self.pos[0] += self.speed

class Enemy(Sprite):
    def __init__(self, pos):
        super().__init__("enemy.png", pos)

        self.speed = random.randint(10, 50)

    def update(self):
        self.pos[0] -= self.speed

class Missile(Particle):
    def __init__(self, pos, target):
        super().__init__()

        self.pos = pos[:]
        self.target = target[:]
        self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        self.radius = random.randint(10, 20)
        self.speed = 10

        self.direction = [self.target[0] - self.pos[0],
                          self.target[1] - self.pos[1]]
        self.direction = normalize(self.direction)

    def draw(self, screen):
        pos = self.pos[:]
        pos[0] -= self.radius / 2
        pos[1] -= self.radius / 2
        pos = [int(pos[0]), int(pos[1])]
        pygame.draw.circle(screen, self.color, pos, self.radius)

    def update(self):
        velocity = [self.direction[0] * self.speed, self.direction[1] * self.speed]
        self.pos[0] += velocity[0]
        self.pos[1] += velocity[1]

    def get_size(self):
        return [self.radius, self.radius]
