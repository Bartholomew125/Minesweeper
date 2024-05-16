import pygame as pg
import random

class Tile:

    def __init__(self, screen, x, y, w, h, bomb_prop):
        self.screen = screen
        self.color = (255,255,255)
        self.og_color = self.color
        self.size = w

        self.rect = pg.Rect(x, y, w, h)

        self.is_bomb = False

        roll = random.random()
        if roll < bomb_prop:
            self.is_bomb = True
            self.og_color = (255,0,0)
    
    def show(self):
        self.og_color = (0,0,0)

    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)
        pg.draw.rect(self.screen, (0,0,0), self.rect, int(self.size/20))