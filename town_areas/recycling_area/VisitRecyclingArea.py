import Button
import BlitText
import GameGlobalVariables
from SavingGameFiles import MessageBoxSaveGame
from town_areas.recycling_area import TimedGame
from town_areas.recycling_area import NormalGame

import pygame
from pygame import mixer

# GLOBAL VARIABLES--------------------------------------------------------------------------------------
# Initialize the pygame

pygame.init()
# soundtracks
recycling_area_music = mixer.Sound('design/music/recycling_area.wav')
town_music = mixer.Sound('design/music/town.wav')
# backgrounds
mayor_recycling_area_background = pygame.image.load('design/backgrounds/mayor_recycling_area_background.jpg')
recycling_area = pygame.image.load('design/backgrounds/recycling_area.jpg')
#  characters
mayor_normal_poseBig = pygame.image.load('design/poses/mayor_normal_pose(big).png')
mayor_superhero_pose = pygame.image.load('design/poses/mayor_superhero_pose.png')

running = True


def visit_recycling_area():
    global running
    running = True

    screen = pygame.display.set_mode((1200, 550))

    # texts
    text = "Let's test your knowledge in recycling!\n1.Pick up the garbage that appears on the grass." \
           "\n2.Put it in the right recycle bin.\n\nIf you're right, your number of recycled materials will\nincrease" \
           " and these materials will be used at the\nrecycling factory." \
           "\nIf you don't recycle correctly, you will lose the material.\n\nYou can choose to play a game with a timer or a game\n" \
           "with a 3 mistakes limit.\n\n" \
           "You can leave this area by pressing on the 'escape'\nkey on your keyboard."

    # fonts
    font = pygame.font.SysFont('arial', 15)

    # "image" buttons description box town view
    text_button = Button.Button((255, 255, 255), 800, 50, 300, 350, ' ')
    play_timed_button = Button.Button((150, 240, 0), 820, 340, 120, 35, 'PLAY TIMED GAME')
    play_normal_button = Button.Button((150, 240, 0), 950, 340, 130, 35, 'PLAY NORMAL GAME')

    oldmx, oldmy, x = 0, 0, 1000
    play_timed, play_normal = False, False
    while running:
        recycling_area_music.play(-1)
        screen.blit(mayor_recycling_area_background, (790, 0))
        screen.blit(recycling_area, (0, 0))

        # for mayor movement
        if x > 700:
            x -= 2
        else:

            if play_timed == False and play_normal == False:
                pos = pygame.mouse.get_pos()
                text_button.draw(screen, 13, (0, 0, 0))  # the message of the mayor
                play_timed_button.draw(screen, 15, (0, 0, 0))
                play_normal_button.draw(screen, 15, (0, 0, 0))
                BlitText.blit_text(screen, text, (803, 50), font)

                if event.type == pygame.MOUSEMOTION:
                    if play_timed_button.is_over(pos):
                        play_timed_button.color = (0, 160, 0)
                    else:
                        play_timed_button.color = (150, 240, 0)

                    if play_normal_button.is_over(pos):
                        play_normal_button.color = (0, 160, 0)
                    else:
                        play_normal_button.color = (150, 240, 0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_timed_button.is_over(pos):
                        play_timed = True
                    if play_normal_button.is_over(pos):
                        play_normal = True

            elif play_timed == True:  # if the player pressed play button already
                TimedGame.TimedGame(screen)
                text_prize = "unfortunately no price"
                if TimedGame.score > 100:
                    GameGlobalVariables.money += 1000
                    text_prize = "1st prize -> 1000 greenlandions"
                elif 70 <= TimedGame.score <= 100:
                    GameGlobalVariables.money += 800
                    text_prize = "2nd prize -> 800 greenlandions"
                elif 50 <= TimedGame.score <= 69:
                    GameGlobalVariables.money += 400
                    text_prize = "3rd prize -> 400 greenlandions"

                text = 'You recycled ' + str(TimedGame.score) + ' objects and won\n' \
                       + text_prize + '\n\n' \
                       'Press the escape key on your keyboard if\nyou want to leave the area or play again!'

                font = pygame.font.SysFont('arial', 20)
                text_button = Button.Button((255, 255, 255), 800, 50, 312, 230, ' ')
                play_timed_button = Button.Button((150, 240, 0), 820, 220, 120, 35, 'PLAY TIMED GAME')
                play_normal_button = Button.Button((150, 240, 0), 950, 220, 130, 35, 'PLAY NORMAL GAME')

                play_timed = False

            elif play_normal == True:
                NormalGame.NormalGame(screen)

                text = 'Congratulations! You recycled ' + str(NormalGame.score) + ' objects!\n\n' \
                                                                                  'Press the escape key on your keyboard if\nyou want to leave the area or play again!'
                font = pygame.font.SysFont('arial', 20)
                text_button = Button.Button((255, 255, 255), 800, 50, 312, 210, ' ')
                play_timed_button = Button.Button((150, 240, 0), 820, 200, 120, 35, 'PLAY TIMED GAME')
                play_normal_button = Button.Button((150, 240, 0), 950, 200, 130, 35, 'PLAY NORMAL GAME')

                play_normal = False

        # end of checking if play button is pressed or not
        screen.blit(mayor_normal_poseBig, (x, 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MessageBoxSaveGame.quit_and_save()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()

    recycling_area_music.stop()
    pygame.display.set_mode((1300, 700))
