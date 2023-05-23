import pygame
from Settings import Settings
import os

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.surface.Surface((1, 1))
        #self.image.fill("green")
        self.image = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Image/background.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, Settings.WINDOW.size)
        self.rect = self.image.get_rect()