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
    for d in dots:
        d.draw()

def create_points():
    for i in range(0, 10):
        x = randint(10, WIDTH - 10)
        y = randint(10, HEIGHT - 10)
        dot = Actor('dot', (x, y))
        dots.append(dot)

def on_key_down(key):
    if key == keys.F:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    elif key == keys.ESCAPE:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))

create_points()

pgzrun.go()