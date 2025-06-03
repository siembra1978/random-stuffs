# written by siembra

import pygame
import random
import time

interval = 120 # nil for as fast as possible
n = 250
maxh = 100

bars = []
selected_index = 0

for num in range(n):
    bars.append(random.randint(0,maxh))

print(bars)

WIDTH,HEIGHT = 512, 512

pygame.init()
pygame.display.set_caption("siembra's silly sort visualizer")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

def bubble_sort(bars):

    arr = bars.copy()
  
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1): 

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                return arr, i, False
            
    return arr, 0, True

start = time.time()
timed_calculated = False

while True:
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    offset = 0
    distx = WIDTH/len(bars)

    for i, bar in enumerate(bars):
        if i == selected_index:
            pygame.draw.rect(screen, (0,255,0),pygame.Rect(offset,HEIGHT-((bar/maxh)*HEIGHT),distx,(bar/maxh)*HEIGHT))
        else:
            pygame.draw.rect(screen, (255,0,0),pygame.Rect(offset,HEIGHT-((bar/maxh)*HEIGHT),distx,(bar/maxh)*HEIGHT))
        offset+=distx

    bars, selected_index, complete = bubble_sort(bars)

    if complete and not timed_calculated:
        print(time.time() - start)
        timed_calculated = True

    pygame.display.update()
    #clock.tick(interval)