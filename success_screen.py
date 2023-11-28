# success_screen.py
import pygame
from start_button import StartButton

class SuccessScreen:
    def __init__(self, width, height):
        self.rect = pygame.Rect(0, 0, width, height)
        self.color = (200, 200, 200)
        self.restart_button = StartButton(width // 2 - 50, height // 2 - 25, 100, 50, (50, 150, 50), "Restart", (255, 255, 255), 30)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        self.restart_button.draw(screen)

    def is_restart_clicked(self, mouse_pos):
        return self.restart_button.is_clicked(mouse_pos)
