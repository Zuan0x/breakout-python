# start_button.py
import pygame

class StartButton:
    def __init__(self, x, y, width, height, color, text, text_color, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, font_size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_render = self.font.render(self.text, True, self.text_color)
        text_rect = text_render.get_rect(center=self.rect.center)
        screen.blit(text_render, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
