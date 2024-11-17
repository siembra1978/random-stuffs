# written by siembra

import pygame
import math

WIDTH,HEIGHT = 512,512

pygame.init()
pygame.display.set_caption('render test')
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

class Square:
    def __init__(self, screen, center, radius, thickness):
        self.screen = screen
        self.x,self.y = center[0], center[1]
        self.radius = radius
        self.thickness = thickness
    
    def update(self, angle):
        #print('updating:',id(self))
        self.draw(angle)

    def draw(self, angle):
        angle = math.radians(angle % 360)
        distance = math.sqrt(2*(self.radius**2)) / 2

        p1 = (self.x + distance * math.cos(angle-(math.pi/4)), self.y + distance * math.sin(angle-(math.pi/4)))
        p2 = (self.x + distance * math.cos(angle+(math.pi/4)), self.y + distance * math.sin(angle+(math.pi/4)))
        p3 = (self.x + distance * math.cos(angle+(3*math.pi/4)), self.y + distance * math.sin(angle+(3*math.pi/4)))
        p4 = (self.x + distance * math.cos(angle+(5*math.pi/4)), self.y + distance * math.sin(angle+(5*math.pi/4)))

        pygame.draw.line(screen, (0,0,0), p1, p2, self.thickness)
        pygame.draw.line(screen, (0,0,0), p2, p3, self.thickness)
        pygame.draw.line(screen, (0,0,0), p3, p4, self.thickness)
        pygame.draw.line(screen, (0,0,0), p4, p1, self.thickness)

        #pygame.draw.line(screen,(0,0,255),(self.x,self.y),(self.x + px,self.y + py),self.thickness) # clock hand or whatever lol
        pygame.draw.circle(screen,(255,0,0),p1,5,10) # point
        pygame.draw.circle(screen,(255,0,0),p2,5,10) # point
        pygame.draw.circle(screen,(255,0,0),p3,5,10) # point
        pygame.draw.circle(screen,(255,0,0),p4,5,10) # point

class Cube:
    def __init__(self, screen, center, width):
        self.screen = screen
        self.x,self.y = center[0],center[1]
        self.side = width

        self.vertices = [(1,1,-1),(1,1,1),
                         (-1,1,-1),(-1,1,1),
                         (1,-1,-1),(1,-1,1),
                         (-1,-1,-1),(-1,-1,1)]

    def transform(self):
        pass

    def project(self,vertex):
        pass

    def update(self, angle):
        self.draw(angle)

    def draw(self,angle):
        for vertex in self.vertices:
            pygame.draw.circle(screen,(255,0,0),(self.x + vertex[0]*self.side, self.y + vertex[1]*self.side),5,10)

objects = []

objects.append(Square(screen, (WIDTH/2,HEIGHT/2), 100, 5))
#objects.append(Cube(screen, (WIDTH/2,HEIGHT/2), 50))

d = 0

while True:
    screen.fill('white')

    for object in objects:
        object.update(d)

    pygame.draw.circle(screen,(255,0,0),(WIDTH/2,HEIGHT/2),5,10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        d+=1
    if keys[pygame.K_LEFT]:
        d-=1
    if keys[pygame.K_w]:
        for object in objects:
            object.y -= 1
    if keys[pygame.K_a]:
        for object in objects:
            object.x -= 1
    if keys[pygame.K_s]:
        for object in objects:
            object.y += 1
    if keys[pygame.K_d]:
        for object in objects:
            object.x += 1

    pygame.display.update()
    clock.tick(60)