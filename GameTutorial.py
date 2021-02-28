# Initialize the pygame
import os

import pygame

import MessageBoxSaveGame

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'  # for centering the window game

# backgrounds
background = pygame.image.load('design/backgrounds/tutorial_window_background.jpg')

# characters
mayor_pose = pygame.image.load('design/poses/mayor_statistics.png')


def run():
    running = True
    screen = pygame.display.set_mode((1000, 746))

    while running:

        screen.blit(background, (0, 0))
        screen.blit(mayor_pose, (500, -80))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MessageBoxSaveGame.quit_and_save()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()