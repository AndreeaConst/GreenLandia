import pygame

import Button
import BlitText
import GameGlobalVariables

# Initialize the pygame
from SavingGameFiles import MessageBoxSaveGame

pygame.init()

# backgrounds
recycling_factory = pygame.image.load('design/backgrounds/recycling_factory.jpg')

# descriptions
description_paper_stock = pygame.image.load('design/recycled items/paper/description paper stock.jpg')
description_notebooks = pygame.image.load('design/recycled items/paper/description notebooks.png')
description_napkins = pygame.image.load('design/recycled items/paper/description napkins.jpg')
description_pencils = pygame.image.load('design/recycled items/paper/description pencils.jpg')
description_book = pygame.image.load('design/recycled items/paper/description book.png')
description_cups = pygame.image.load('design/recycled items/paper/description cups.png')

def info_paper_stock(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((255, 255, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 50 PAPER WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  The recycling of paper is the process by\n" \
                "which waste paper is turned into new paper\n" \
                "products. It has a number of important benefits:\n" \
                "it saves waste paper from occupying homes of\n" \
                "people and producing methane as it breaks down.\n\n" \
                "  Because paper fibre contains carbon, recycling\n" \
                "keeps the carbon locked up for longer and out of\n" \
                "the atmosphere.\n\n" \
                "  After repeated processing the fibres become too\n" \
                "short for the production of new paper - this is why\n" \
                "virgin fibre (from sustainably farmed trees) will be\n" \
                "added to the pulp recipe.\n" \
                "  After a long process, here we have new paper that\n" \
                "we can use!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_paper) + " PAPER WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_paper_stock, (540, 230))

        BlitText.blit_text(screen, "RECYCLED PAPER STOCK", (260, 142), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (250, 220), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                MessageBoxSaveGame.quit_and_save()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_paper >= 50:
                        GameGlobalVariables.score_paper -= 50
                        text_worker = "You have now " + str(GameGlobalVariables.score_paper) + " PAPER WASTE!\n\n" \
                                                                                  "You just created a recycled paper stock!\n" \
                                                                                  "             Congrats!"
                    else:
                        text_worker = "You don't have enough paper waste\n" \
                                     "     to create a paper stock!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (255, 255, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()


def info_notebook(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((255, 255, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 30 PAPER WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  The recycling of paper is the process by\n" \
                "which waste paper is turned into new paper\n" \
                "products. It has a number of important benefits:\n" \
                "it saves waste paper from occupying homes of\n" \
                "people and producing methane as it breaks down.\n\n" \
                "  Because paper fibre contains carbon, recycling\n" \
                "keeps the carbon locked up for longer and out of\n" \
                "the atmosphere.\n\n" \
                "  After repeated processing the fibres become too\n" \
                "short for the production of new paper - this is why\n" \
                "virgin fibre (from sustainably farmed trees) will be\n" \
                "added to the pulp recipe.\n" \
                "  After a long process, here we have new notebooks that\n" \
                "we can use!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_paper) + " PAPER WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_notebooks, (550, 230))

        BlitText.blit_text(screen, "RECYCLED PAPER NOTEBOOKS", (220, 142), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (250, 220), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                MessageBoxSaveGame.quit_and_save()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_paper >= 30:
                        GameGlobalVariables.score_paper -= 30
                        text_worker = "You have now " + str(GameGlobalVariables.score_paper) + " PAPER WASTE!\n\n" \
                                                                                  "You just created rcycled notebooks!\n" \
                                                                                  "             Congrats!"
                    else:
                        text_worker = "You don't have enough paper waste\n" \
                                     "     to create notebooks!\n" \
                                     "Recycle more in order to create them!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (255, 255, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()


def info_napkins(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((255, 255, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 10 PAPER WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  The recycling of paper is the process by\n" \
                "which waste paper is turned into new paper\n" \
                "products. It has a number of important benefits:\n" \
                "it saves waste paper from occupying homes of\n" \
                "people and producing methane as it breaks down.\n\n" \
                "  Because paper fibre contains carbon, recycling\n" \
                "keeps the carbon locked up for longer and out of\n" \
                "the atmosphere.\n\n" \
                "  After repeated processing the fibres become too\n" \
                "short for the production of new paper - this is why\n" \
                "virgin fibre (from sustainably farmed trees) will be\n" \
                "added to the pulp recipe.\n" \
                "  After a long process, here we have new napkins that\n" \
                "we can use!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_paper) + " PAPER WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_napkins, (540, 230))

        BlitText.blit_text(screen, "RECYCLED PAPER NAPKINS", (260, 142), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (250, 220), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                MessageBoxSaveGame.quit_and_save()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_paper >= 10:
                        GameGlobalVariables.score_paper -= 10
                        text_worker = "You have now " + str(GameGlobalVariables.score_paper) + " PAPER WASTE!\n\n" \
                                                                                  "You just created recycled paper napkins!\n" \
                                                                                  "               Congrats!"
                    else:
                        text_worker = "You don't have enough paper waste\n" \
                                     "     to create paper napkins!\n" \
                                     "Recycle more in order to create them!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (255, 255, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()


def info_pencils(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((255, 255, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 30 PAPER WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  The recycling of paper is the process by\n" \
                "which waste paper is turned into new paper\n" \
                "products. It has a number of important benefits:\n" \
                "it saves waste paper from occupying homes of\n" \
                "people and producing methane as it breaks down.\n\n" \
                "  Because paper fibre contains carbon, recycling\n" \
                "keeps the carbon locked up for longer and out of\n" \
                "the atmosphere.\n\n" \
                "  After repeated processing the fibres become too\n" \
                "short for the production of new paper - this is why\n" \
                "virgin fibre (from sustainably farmed trees) will be\n" \
                "added to the pulp recipe.\n" \
                "  After a long process, here we have new paper pencils\n" \
                "that we can use!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_paper) + " PAPER WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_pencils, (540, 230))

        BlitText.blit_text(screen, "RECYCLED PAPER PENCILS", (260, 142), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (250, 220), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                MessageBoxSaveGame.quit_and_save()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_paper >= 30:
                        GameGlobalVariables.score_paper -= 30
                        text_worker = "You have now " + str(GameGlobalVariables.score_paper) + " PAPER WASTE!\n\n" \
                                                                                  "You just created recycled paper pencils!\n" \
                                                                                  "             Congrats!"
                    else:
                        text_worker = "You don't have enough paper waste\n" \
                                     "     to create paper pencils!\n" \
                                     "Recycle more in order to create them!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (255, 255, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()


def info_book(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((255, 255, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 80 PAPER WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  The recycling of paper is the process by\n" \
                "which waste paper is turned into new paper\n" \
                "products. It has a number of important benefits:\n" \
                "it saves waste paper from occupying homes of\n" \
                "people and producing methane as it breaks down.\n\n" \
                "  Because paper fibre contains carbon, recycling\n" \
                "keeps the carbon locked up for longer and out of\n" \
                "the atmosphere.\n\n" \
                "  After repeated processing the fibres become too\n" \
                "short for the production of new paper - this is why\n" \
                "virgin fibre (from sustainably farmed trees) will be\n" \
                "added to the pulp recipe.\n" \
                "  After a long process, here we have a new book that\n" \
                "we can use!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_paper) + " PAPER WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_book, (540, 230))

        BlitText.blit_text(screen, "BOOK", (300, 142), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (250, 220), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                MessageBoxSaveGame.quit_and_save()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_paper >= 80:
                        GameGlobalVariables.score_paper -= 80
                        text_worker = "You have now " + str(GameGlobalVariables.score_paper) + " PAPER WASTE!\n\n" \
                                                                                  "You just created a book!\n" \
                                                                                  "         Congrats!"
                    else:
                        text_worker = "You don't have enough paper waste\n" \
                                     "       to create a book!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (255, 255, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()


def info_cups(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((255, 255, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 20 PAPER WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  The recycling of paper is the process by\n" \
                "which waste paper is turned into new paper\n" \
                "products. It has a number of important benefits:\n" \
                "it saves waste paper from occupying homes of\n" \
                "people and producing methane as it breaks down.\n\n" \
                "  Because paper fibre contains carbon, recycling\n" \
                "keeps the carbon locked up for longer and out of\n" \
                "the atmosphere.\n\n" \
                "  After repeated processing the fibres become too\n" \
                "short for the production of new paper - this is why\n" \
                "virgin fibre (from sustainably farmed trees) will be\n" \
                "added to the pulp recipe.\n" \
                "  After a long process, here we have new paper cusp that\n" \
                "we can use instead of plastic ones!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_paper) + " PAPER WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_cups, (540, 230))

        BlitText.blit_text(screen, "RECYCLED PAPER CUPS", (260, 142), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (250, 220), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                MessageBoxSaveGame.quit_and_save()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_paper >= 20:
                        GameGlobalVariables.score_paper -= 20
                        text_worker = "You have now " + str(GameGlobalVariables.score_paper) + " PAPER WASTE!\n\n" \
                                                                                  "You just created recycled paper cups!\n" \
                                                                                  "              Congrats!"
                    else:
                        text_worker = "You don't have enough paper waste\n" \
                                     "     to create paper cups!\n" \
                                     "Recycle more in order to create them!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (255, 255, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()
