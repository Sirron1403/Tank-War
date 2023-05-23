import os
import pygame
from Settings import Settings
from Ui import UI
from Background import Background
from Tank1 import Tank
from Tank2 import Tank2
from pygame.constants import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, QUIT

class Game(object):
   def __init__(self):
      os.environ['SDL_VIDEO_WINDOW_POS'] = "10, 50"
      pygame.init()
      self.screen = pygame.display.set_mode(Settings.WINDOW.size)
      pygame.display.set_caption("Tank War")
      self.clock = pygame.time.Clock()
      self.tank_ = Tank()
      self.tank = pygame.sprite.GroupSingle(self.tank_)
      self.tank2_ = Tank2()
      self.tank2 = pygame.sprite.GroupSingle(self.tank2_)
      self.background = pygame.sprite.GroupSingle(Background())
      self.UI = UI(self.screen)
      self.t1 = ""
      self.t11 = "Sie haben den Gegner erfolgreich vernichtet."
      self.font = pygame.font.Font(pygame.font.get_default_font(), 25)
      self.running = True

   def run(self):
      self.UI.start_menu()
      while self.running:
         self.clock.tick(Settings.FPS)
         self.watch_for_events()
         self.update()
         self.draw()
      pygame.quit()

   def watch_for_events(self):
      for event in pygame.event.get():
         if event.type == QUIT:
            self.running = False
         if event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_p:
               self.tank_.shoot()
            if key == pygame.K_r:
               self.tank2_.shoot()
      keys = pygame.key.get_pressed()
      if keys[pygame.K_ESCAPE]:
         self.UI.pause_menu()
      if keys[pygame.K_LEFT]:
         self.tank.sprite.move("WEST")
      if keys[pygame.K_RIGHT]:
         self.tank.sprite.move("EAST")
      if keys[pygame.K_UP]:
         self.tank.sprite.move("NORTH")
      if keys[pygame.K_DOWN]:
         self.tank.sprite.move("SOUTH")
      if keys[pygame.K_a]:
         self.tank2.sprite.move("WEST")
      if keys[pygame.K_d]:
         self.tank2.sprite.move("EAST")
      if keys[pygame.K_w]:
         self.tank2.sprite.move("NORTH")
      if keys[pygame.K_s]:
         self.tank2.sprite.move("SOUTH")
        
   def update(self):
      self.tank.update()
      self.tank2.update()
      for i in self.tank_.bullets:
         i.update()
      for i in self.tank2_.bullets:
         i.update()
      for bullet in self.tank_.bullets:
         if self.tank2_.rect.colliderect(bullet):
            self.tank_.bullets.remove(bullet)

            self.tank2_.leben_ak -= 25
            if self.tank2_.leben_ak <= 0:
               self.tank2_.leben_ak = 0
               self.tank2_.lebt = False
               self.t1 = str(self.UI.spielername2) + " hat gewonnen."
         
      for bullet in self.tank2_.bullets:
         if self.tank_.rect.colliderect(bullet):
            self.tank2_.bullets.remove(bullet)
              
            self.tank_.leben_ak -= 25
            if self.tank_.leben_ak <= 0:
               self.tank_.leben_ak = 0
               self.tank_.lebt = False
               self.t1 = str(self.UI.spielername1) + " hat gewonnen."
          
   def draw(self):
      if self.tank_.lebt and self.tank2_.lebt:
         self.background.draw(self.screen)
         if self.tank_.lebt:
            self.tank.draw(self.screen)
            self.tank_.draw(self.screen)
         for i in self.tank_.bullets:
            i.draw(self.screen)
         if self.tank2_.lebt:
            self.tank2.draw(self.screen)
            self.tank2_.draw(self.screen)
         for i in self.tank2_.bullets:
            i.draw(self.screen)
      else:
         self.screen.fill((0, 0, 0), Settings.WINDOW)
         font_surface = self.font.render(self.t1 + " " + self.t11, True,(255,0,0))
         textrect = font_surface.get_rect()
         textrect.center = Settings.WINDOW.center 
         self.screen.blit(font_surface, textrect)
              
      pygame.display.flip()

if __name__ == '__main__':
   game = Game()
   game.run()