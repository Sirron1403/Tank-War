import pygame 
from Settings import Settings
import os
from Shoot import Shoot



class Tank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),"Image/Tank1.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.bullets = []
        self.leben = 100
        self.leben_ak = self.leben
        self.lebt = True
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings.WINDOW.centerx
        self.rect.bottom = Settings.WINDOW.height - 1
    
    def draw(self,screen):
        screen.blit(self.image, self.rect)
        screen.fill((255, 0, 0, 255), pygame.Rect(self.rect.x - 6, self.rect.y + 90, self.leben_ak / self.leben * 100, 15))



    def update(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Settings.WINDOW.width:
            self.rect.right = Settings.WINDOW.width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > Settings.WINDOW.height:
            self.rect.bottom = Settings.WINDOW.height


        return super().update()

    def shoot(self):
      shoot = Shoot()
      shoot.rect.x = self.rect.x + 35
      shoot.rect.y = self.rect.y
      self.bullets.append(shoot)


    def move(self, direction: str):
        if direction == "WEST":
            self.rect.x -= 5
        elif direction == "EAST":
            self.rect.x += 5
        elif direction == "NORTH":
            self.rect.y -= 5
        elif direction == "SOUTH":
            self.rect.y += 5