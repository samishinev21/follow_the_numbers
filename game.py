from pgzero.screen import Screen
import pgzrun
from random import randint
import pygame

WIDTH = 800
HEIGHT = 600

dots = []
lines = []

next_dot = 0

def draw():
    screen.clear()
    screen.fill((8, 40, 0))
    number = 1
    for dot in dots:
        dot.draw()
        screen.draw.text(str(number), center=(dot.x, dot.y), color='black')
        number += 1

def create_points():
    for i in range(0, 10):
        x = randint(10, WIDTH - 10)
        y = randint(10, HEIGHT - 10)
        dot = Actor('dot', (x, y))
        dots.append(dot)

def on_mouse_down():
    screen.fill((8, 40, 0))

def on_key_down(key):
    if key == keys.F:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    elif key == keys.ESCAPE:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))

create_points()

pgzrun.go()