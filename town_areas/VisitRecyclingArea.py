import Button
import BlitText
import pygame
import random
import TownView
from pygame import mixer

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


def play_game_recycling_area(screen, text_button, score, mistakes, result):
    font1 = pygame.font.SysFont('arial', 40)

    text3 = " Drag the object to the right recycle bin\n            and click on the bin!"
    font2 = pygame.font.SysFont('arial', 20)

    text_button.draw(screen, 13, (0, 0, 0))  # mayor textbox

    # print score
    score = font1.render("SCORE: " + str(score), True, (0, 255, 0))
    screen.blit(score, (803, 50))

    # print mistakes
    score = font1.render("MISTAKES: " + str(mistakes), True, (255, 0, 0))
    screen.blit(score, (803, 100))

    # print instructions
    BlitText.blit_text(screen, text3, (803, 170), font2)

    if result == 'Correct':
        BlitText.blit_text(screen, 'Correct!', (890, 250), font1, (0, 255, 0))
    elif result == 'Wrong':
        BlitText.blit_text(screen, 'Wrong!', (890, 250), font1, (255, 0, 0))


def visit_recycling_area():
    screen = pygame.display.set_mode((1200, 550))

    # texts
    text = "Let's test your knowledge in recycling!\n1.Pick up the garbage that appears on the grass." \
           "\n2.Put it in the right recycle bin.\n\nIf you're right, your number of recycled materials will\nincrease" \
           " and these materials will be used at the\nrecycling factory so you have to visit that afterwards." \
           "\n\nIf you don't recycle correctly, you will lose the material.\nTHE GAME ENDS AFTER 3 MISTAKES.\nGood luck!"

    # fonts
    font = pygame.font.SysFont('arial', 15)

    # "image" buttons description box town view
    text_button = Button.button((255, 255, 255), 800, 50, 300, 300, ' ')
    play_button = Button.button((150, 240, 0), 900, 300, 100, 35, 'PLAY')

    score, mistakes, oldmx, oldmy, x = 0, 0, 0, 0, 1000
    play, running = False, True
    while running:
        recycling_area_music.play(-1)
        screen.blit(mayor_recycling_area_background, (790, 0))
        screen.blit(recycling_area, (0, 0))

        # for mayor movement
        if x > 700:
            x -= 2
        else:

            if play == False:
                pos = pygame.mouse.get_pos()
                text_button.draw(screen, 13, (0, 0, 0))  # the message of the mayor
                play_button.draw(screen, 35, (0, 0, 0))
                BlitText.blit_text(screen, text, (803, 50), font)

                if event.type == pygame.MOUSEMOTION:
                    if play_button.is_over(pos):
                        play_button.color = (0, 160, 0)
                    else:
                        play_button.color = (150, 240, 0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.is_over(pos):
                        play = True
                        mistakes = 0

            elif play == True:  # if the player pressed play button already

                # select a random trash item from folder "trash"
                i = random.randint(1, 72)
                trash_image = pygame.image.load("design/trash/trash" + str(i) + ".png")

                correct = True  # correct = true, if recycled properly, correct = false, otherwise
                while correct == True:

                    if mistakes < 3:
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
                                correct = -2  # interrupt the game
                                running = False  # also return to the town view

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if 40 <= my <= 210:
                                    if 35 <= mx <= 130:
                                        if material == 'metal':
                                            score += 1
                                            TownView.score_metal += 1
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
                                                TownView.score_organic += 1
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
                                                    TownView.score_paper += 1
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
                                                        TownView.score_plastic += 1
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
                                                            TownView.score_glass += 1
                                                            result = 'Correct'

                                                            # recycle another piece of trash
                                                            i = random.randint(1, 72)
                                                            trash_image = pygame.image.load(
                                                                "design/trash/trash" + str(i) + ".png")

                                                        else:
                                                            mistakes += 1
                                                            result = 'Wrong'

                        # rebuilding background
                        screen.fill((0, 0, 0))
                        screen.blit(mayor_recycling_area_background, (790, 0))
                        screen.blit(recycling_area, (0, 0))
                        screen.blit(mayor_normal_poseBig, (x, 60))
                        play_game_recycling_area(screen, text_button, score, mistakes,
                                                 result)  # printing on screen the text box with the score -->mayor textbox

                        # so the object would not exit the collecting screen and go where the mayor is
                        if 0 <= mx <= 730:
                            screen.blit(trash_image, (mx - 60, my - 60))
                            oldmx = mx
                            oldmy = my
                        else:
                            screen.blit(trash_image, (oldmx, oldmy))
                        pygame.display.flip()

                    else:
                        # the end of the game--->mistakes = 3

                        text = 'Congratulations! You recycled ' + str(score) + ' objects!\n\nClose the window' \
                                                                               ' if you want to leave\nthe area or play again!'
                        font = pygame.font.SysFont('arial', 20)
                        text_button = Button.button((255, 255, 255), 800, 50, 312, 260, ' ')
                        play_button = Button.button((150, 240, 0), 900, 200, 100, 35, 'PLAY')

                        score = 0
                        correct = False
                        play = False
        # end of checking if play button is pressed or not

        # displaying mayor on the screen
        if mistakes == 3:
            # displaying mayor on the screen
            screen.blit(mayor_superhero_pose, (-200, 40))
        else:
            screen.blit(mayor_normal_poseBig, (x, 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    recycling_area_music.stop()
    pygame.display.set_mode((1300, 700))
