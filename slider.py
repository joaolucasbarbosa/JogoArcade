import pygame
import sys

# Classe Slider
class Slider:
    def __init__(self, pos, width, height, min_value, max_value, initial_value, is_enabled=True):
        self.pos = pos
        self.width = width
        self.height = height
        self.rect = pygame.Rect(pos, (width, height))
        self.handle_rect = pygame.Rect((pos[0] + initial_value / (max_value - min_value) * width - height / 2, pos[1]), (height, height))
        self.value = initial_value
        self.min_value = min_value
        self.max_value = max_value
        self.is_dragging = False
        self.is_enabled = is_enabled


    def update(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), self.rect)
        pygame.draw.rect(surface, (100, 100, 100), self.handle_rect)
            
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.handle_rect.collidepoint(event.pos):
                self.is_dragging = True
        elif event.type == pygame.MOUSEMOTION:
            if self.is_dragging:
                self.handle_rect.x = max(self.rect.left, min(self.rect.right - self.handle_rect.width, event.pos[0] - self.handle_rect.width / 2))
                self.value = (self.handle_rect.x - self.rect.left) / (self.rect.width - self.handle_rect.width) * (self.max_value - self.min_value)
                # Convertendo para a escala de 0.0 a 1.0
                pygame.mixer.music.set_volume(self.value)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.is_dragging = False
    
    def is_disabled(self):
        return not self.is_enabled
    
