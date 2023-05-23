import pygame
import pygame_menu
from Settings import Settings

class UI:
        def __init__(self, screen):
                self.screen = screen
                self.font = pygame.font.Font(None, 30)
                self.health = 100
                self.bar_length = 200
                self.bar_height = 20
                self.bar_pos = (Settings.WINDOW.width - self.bar_length // 2, 10)
                self.spielername1 = ""
                self.spielername2 = ""
                        
        def start_menu(self):
                self.menu = pygame_menu.Menu("Start",500, 400, theme=pygame_menu.themes.THEME_DARK)
                self.textbox1 = self.menu.add.text_input("Spielername 1: ", default="Spielername 1", onchange=self.spielername1)
                self.textbox2 = self.menu.add.text_input("Spielername 2: ", default="Spielername 2", onchange=self.spielername2)
                self.menu.add.button("Play", self.menu.disable)
                self.menu.add.button("Exit", pygame_menu.events.EXIT)
                self.menu.mainloop(self.screen)
                self.spielername1 = self.textbox1.get_value()
                self.spielername2 = self.textbox2.get_value()
                print(self.spielername1)
                print(self.spielername2)
        
        def pause_menu(self):
                self.menu = pygame_menu.Menu("Pause", 300, 400, theme=pygame_menu.themes.THEME_DARK)
                self.menu.add.button("Weiter", self.menu.disable)
                self.menu.add.button("Quit", pygame_menu.events.EXIT)
                self.menu.mainloop(self.screen)


