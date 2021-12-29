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
    pass

def on_key_down(key):
    if key == keys.F:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    elif key == keys.ESCAPE:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))



pgzrun.go()