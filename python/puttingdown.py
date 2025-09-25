# written by siembra

import pygame
import math

WIDTH,HEIGHT = 900,512

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Courier New', 20)
pygame.display.set_caption('the code pt 2')
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

class Thingy:
    def __init__(self, screen, owner, radius):
        self.owner = owner
        self.screen = screen
        self.radius = radius
        self.center = (WIDTH/2,HEIGHT/2)

    def update(self):
        self.draw()

    def draw(self):
        pygame.draw.circle(self.screen, (255,0,0), self.center, self.radius)

class Person:
    def __init__(self, screen, name, stupid, awesome, pos, color):
        self.screen = screen
        self.name = name
        self.stupid = stupid
        self.awesome = awesome
        self.pos = pos
        self.color = color

    def __str__(self):
        return self.name

    def pick_up(self, thingy):
        thingy.owner = self
        thingy.center = self.pos

    def put_down(self, thingy):
        thingy.owner = None
        thing.center = (WIDTH/2,HEIGHT/2)

    def update(self):
        self.draw()

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, 50)

objects = []

thing = Thingy(screen, None, 25)
siembra = Person(screen, 'siembra', False, True, (WIDTH/3, HEIGHT/3), (0,255,0))
jnosa = Person(screen, "jnosa", True, False, (2*WIDTH/3, HEIGHT/3), (125,125,125))

objects.append(siembra)
objects.append(jnosa)
objects.append(thing)

update = ""

while True:
    screen.fill('white')
    fps_display = font.render(f"FPS: {clock.get_fps():.2f} | Thingy Haver: {thing.owner} | Last Update: {update}", False, (0,0,0))

    for object in objects:
        object.update()

    if thing.owner != jnosa:
        jnosa.pick_up(thing)
        update = "jnosa picked up the thingy"
        print("jnosa picked up the thingy")
    elif thing.owner == jnosa:
        siembra.put_down(thing)
        update = "siembra put down the thingy"
        print("siembra put down the thingy")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(fps_display,(0,0))
    pygame.display.update()
    clock.tick(1)