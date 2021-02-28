import random
import pygame

import GameGlobalVariables
import Button
from SavingGameFiles import MessageBoxSaveGame
from town_areas.recycling_area import VisitRecyclingArea, PrintTexts

score = 0


def TimedGame(screen):
    global score
    mistakes, oldmx, oldmy = 0, 0, 0

    text_button = Button.Button((255, 255, 255), 800, 50, 300, 430, ' ')

    timer_font = pygame.font.SysFont('arial', 60)
    timer_sec = 30
    timer_min = 1
    timer_text = timer_font.render("01:30", True, (0, 0, 0))
    timer = pygame.USEREVENT + 1
    pygame.time.set_timer(timer, 1000)  # sets timer with USEREVENT and delay in milliseconds

    # select a random trash item from folder "trash"
    i = random.randint(1, 72)
    trash_image = pygame.image.load("design/trash/trash" + str(i) + ".png")

    while (timer_sec != 0 or timer_min != 0) and VisitRecyclingArea.running == True:

        mx, my = pygame.mouse.get_pos()

        # the pixel zone for each trash bin
        if i <= 10:
            material = 'glass'
        elif 11 <= i <= 21:
            material = 'metal'
        elif 22 <= i <= 40:
            material = 'organic'
        elif 41 <= i <= 58:
            material = 'paper'
        else:
            material = 'plastic'

        result = 'None'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MessageBoxSaveGame.quit_and_save()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    VisitRecyclingArea.running = False

            if event.type == timer:  # checks for timer event
                if timer_sec > 0:
                    timer_sec -= 1
                    timer_sec_string = str(timer_sec)
                    if timer_sec < 10:
                        timer_sec_string = "0" + str(timer_sec)
                    timer_text = timer_font.render(str(timer_min) + ":" + timer_sec_string, True, (0, 0, 0))
                elif timer_min >= 0:
                    timer_min -= 1
                    timer_sec = 59
                    timer_text = timer_font.render(str(timer_min) + ":" + str(timer_sec), True, (0, 0, 0))
                else:
                    pygame.time.set_timer(timer, 0)  # turns off timer event

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 40 <= my <= 210:
                    if 35 <= mx <= 130:
                        if material == 'metal':
                            score += 1
                            GameGlobalVariables.score_metal += 1
                            result = 'Correct'

                            # recycle another piece of trash
                            i = random.randint(1, 72)
                            trash_image = pygame.image.load("design/trash/trash" + str(i) + ".png")

                        else:
                            mistakes += 1
                            result = 'Wrong'
                    else:
                        if 180 <= mx <= 270:
                            if material == 'organic':
                                score += 1
                                GameGlobalVariables.score_organic += 1
                                result = 'Correct'

                                # recycle another piece of trash
                                i = random.randint(1, 72)
                                trash_image = pygame.image.load("design/trash/trash" + str(i) + ".png")

                            else:
                                mistakes += 1
                                result = 'Wrong'
                        else:
                            if 340 <= mx <= 415:
                                if material == 'paper':
                                    score += 1
                                    GameGlobalVariables.score_paper += 1
                                    result = 'Correct'

                                    # recycle another piece of trash
                                    i = random.randint(1, 72)
                                    trash_image = pygame.image.load("design/trash/trash" + str(i) + ".png")

                                else:
                                    mistakes += 1
                                    result = 'Wrong'
                            else:
                                if 485 <= mx <= 580:
                                    if material == 'plastic':
                                        score += 1
                                        GameGlobalVariables.score_plastic += 1
                                        result = 'Correct'

                                        # recycle another piece of trash
                                        i = random.randint(1, 72)
                                        trash_image = pygame.image.load("design/trash/trash" + str(i) + ".png")

                                    else:
                                        mistakes += 1
                                        result = 'Wrong'
                                else:
                                    if 640 <= mx <= 720:
                                        if material == 'glass':
                                            score += 1
                                            GameGlobalVariables.score_glass += 1
                                            result = 'Correct'

                                            # recycle another piece of trash
                                            i = random.randint(1, 72)
                                            trash_image = pygame.image.load("design/trash/trash" + str(i) + ".png")

                                        else:

                                            mistakes += 1
                                            result = 'Wrong'

        # rebuilding background
        screen.fill((0, 0, 0))
        screen.blit(VisitRecyclingArea.mayor_recycling_area_background, (790, 0))
        screen.blit(VisitRecyclingArea.recycling_area, (0, 0))
        PrintTexts.print_texts(screen, text_button, score, mistakes,
                               result, "timed")  # printing on screen the text box with the score -->mayor textbox
        screen.blit(VisitRecyclingArea.mayor_normal_poseBig, (700, 60))
        screen.blit(timer_text, (900, 300))

        # so the object would not exit the collecting screen and go where the mayor is
        if 0 <= mx <= 730:
            screen.blit(trash_image, (mx - 60, my - 60))
            oldmx = mx
            oldmy = my
        else:
            screen.blit(trash_image, (oldmx, oldmy))
        pygame.display.flip()
