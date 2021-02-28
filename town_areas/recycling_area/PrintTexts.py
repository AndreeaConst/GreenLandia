import pygame

import BlitText


def print_texts(screen, text_button, score, mistakes, result, game_type = "normal"):
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

    if game_type == "timed":
        text4 = "1st prize: more than 100 items recycled\n" \
                "2nd prize: 70-100 items recycled\n" \
                "3rd prize: 50-69 items recycled"
        BlitText.blit_text(screen, text4, (807, 400), font2)

    if result == 'Correct':
        BlitText.blit_text(screen, 'Correct!', (896, 240), font1, (0, 255, 0))

    elif result == 'Wrong':
        BlitText.blit_text(screen, 'Wrong!', (896, 240), font1, (255, 0, 0))
