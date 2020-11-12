import BUTTON
import drawButton
import pygame
import townView
from pygame import mixer

# Initialize the pygame
pygame.init()
# soundtrack
menu_music = mixer.Sound('music/menu.wav')
# Backgrounds
backgroundMenu = pygame.image.load('images/menu_background.png')

menuButton = BUTTON.button((255, 255, 255), 300, 180, 300, 70, 'START GAME')


def main_menu():
    while True:

        menu_music.play(-1)
        screen = pygame.display.set_mode((900, 700))
        # background image
        screen.blit(backgroundMenu, (0, 0))

        drawButton.drawButton(screen, menuButton, 40, None)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                pygame.quit()

            # menu button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menuButton.isOver(pos):
                    menu_music.stop()
                    townView.townView(screen)
            if event.type == pygame.MOUSEMOTION:
                if menuButton.isOver(pos):
                    menuButton.color = (0, 160, 0)
                else:
                    menuButton.color = (255, 255, 255)

        pygame.display.update()


# print(pygame.font.get_fonts())
main_menu()