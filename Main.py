import Button
import pygame
import TownView
from pygame import mixer

# Initialize the pygame
pygame.init()
# soundtrack
menu_music = mixer.Sound('design/music/menu.wav')
# Backgrounds
background_menu = pygame.image.load('design/backgrounds/menu_background.png')

menu_button = Button.button((255, 255, 255), 300, 180, 300, 70, 'START GAME')


def main_menu():
    while True:

        menu_music.play(-1)
        screen = pygame.display.set_mode((900, 700))
        # background image
        screen.blit(background_menu, (0, 0))

        menu_button.draw(screen, 40, None)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                pygame.quit()

            # menu button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.is_over(pos):
                    menu_music.stop()
                    TownView.town_view()
            if event.type == pygame.MOUSEMOTION:
                if menu_button.is_over(pos):
                    menu_button.color = (0, 160, 0)
                else:
                    menu_button.color = (255, 255, 255)

        pygame.display.update()


# print(pygame.font.get_fonts())
main_menu()
