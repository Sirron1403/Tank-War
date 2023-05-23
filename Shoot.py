import pygame 
from Settings import Settings
import os



class Shoot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Image/bullet.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = -5
        self.rect.centerx = Settings.WINDOW.centerx
        self.rect.bottom = Settings.WINDOW.height - 1
    
    def draw(self,screen):
        screen.blit(self.image, self.rect)


    def update(self):
       self.rect.y += self.speed

        #return super().update()