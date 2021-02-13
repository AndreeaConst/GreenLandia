import Button
import pygame
import TownView
from pygame import mixer


class MainMenu:
    def __init__(self):
        # initialize game
        pygame.init()
        # soundtrack
        self.menu_music = mixer.Sound('design/music/menu.wav')
        # Backgrounds
        self.background_menu = pygame.image.load('design/backgrounds/menu_background.png')
        # menu buttons
        self.menu_button = Button.Button((255, 255, 255), 300, 180, 300, 70, 'START GAME')

    def handle_events(self):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                pygame.quit()

            # menu button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu_button.is_over(pos):
                    self.menu_music.stop()
                    TownView.town_view()

            if event.type == pygame.MOUSEMOTION:
                if self.menu_button.is_over(pos):
                    self.menu_button.color = (0, 160, 0)
                else:
                    self.menu_button.color = (255, 255, 255)

    def run(self):
        while True:
            self.menu_music.play(-1)
            screen = pygame.display.set_mode((900, 700))

            # display background image
            screen.blit(self.background_menu, (0, 0))
            # display menu buttons
            self.menu_button.draw(screen, 40, None)

            self.handle_events()

            pygame.display.update()


MainMenu().run()
