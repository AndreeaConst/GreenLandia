import pygame
from pygame import mixer

import MessageBoxSaveGame
import Button
import TownView
import SaveGame
import LoadGame
import GameTutorial


class MainMenu:
    def __init__(self):
        # initialize game
        pygame.init()
        # soundtrack
        self.menu_music = mixer.Sound('design/music/menu.wav')
        # Backgrounds
        self.background_menu = pygame.image.load('design/backgrounds/menu_background.png')
        # menu buttons
        self.menu_button_start = Button.Button((255, 255, 255), 300, 180, 300, 70, 'START GAME')
        self.menu_button_save = Button.Button((255, 255, 255), 300, 300, 300, 70, 'SAVE GAME')
        self.menu_button_tutorial = Button.Button((255, 255, 255), 300, 420, 300, 70, 'GAME TUTORIAL')
        self.ok_save = False

    def handle_events(self):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                MessageBoxSaveGame.quit_and_save()
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu_button_start.is_over(pos):
                    self.menu_music.stop()
                    LoadGame.load_game()
                    TownView.town_view()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu_button_tutorial.is_over(pos):
                    GameTutorial.run()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu_button_save.is_over(pos):
                    self.ok_save = True
                    SaveGame.save_game()

            if event.type == pygame.MOUSEMOTION:
                if self.menu_button_start.is_over(pos):
                    self.menu_button_start.color = (0, 160, 0)
                else:
                    self.menu_button_start.color = (255, 255, 255)

            if event.type == pygame.MOUSEMOTION:
                if self.menu_button_save.is_over(pos):
                    self.menu_button_save.color = (0, 160, 0)
                else:
                    self.menu_button_save.color = (255, 255, 255)

            if event.type == pygame.MOUSEMOTION:
                if self.menu_button_tutorial.is_over(pos):
                    self.menu_button_tutorial.color = (0, 160, 0)
                else:
                    self.menu_button_tutorial.color = (255, 255, 255)

    def run(self):
        while True:
            self.menu_music.play(-1)
            screen = pygame.display.set_mode((900, 700))

            # display background image
            screen.blit(self.background_menu, (0, 0))
            # display menu buttons
            self.menu_button_start.draw(screen, 40, True)
            self.menu_button_save.draw(screen, 40, True)
            self.menu_button_tutorial.draw(screen, 40, True)

            self.handle_events()

            timer = 70
            while timer > 0:
                if self.ok_save == True:
                    font = pygame.font.Font(None, 64)
                    text = font.render('Game saved', True, pygame.Color('green'))
                    screen.blit(text, (310, 600))
                    pygame.display.update()
                timer -= 1
            self.ok_save = False

            pygame.display.update()


MainMenu().run()
