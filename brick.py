# brick.py
import pygame

class Brick:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.is_visible = True

    def draw(self, screen):
        if self.is_visible:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
