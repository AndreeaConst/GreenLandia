
# backgrounds
import pygame

import BUTTON
import blitText
import drawButton
import townView

recycling_factory = pygame.image.load('design/backgrounds/recycling_factory.jpg')

# descriptions
descriptionPaperStock = pygame.image.load('design/recycled items/paper/description paper stock.jpg')
descriptionNotebooks = pygame.image.load('design/recycled items/paper/description notebooks.png')
descriptionNapkins = pygame.image.load('design/recycled items/paper/description napkins.jpg')
descriptionPencils = pygame.image.load('design/recycled items/paper/description pencils.jpg')
descriptionBook = pygame.image.load('design/recycled items/paper/description book.png')
descriptionCups = pygame.image.load('design/recycled items/paper/description cups.png')

def info_paperStock(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((255, 255, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 50 PAPER WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  The recycling of paper is the process by\n" \
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

    textWorker = "You have now " + str(townView.scorePaper) + " PAPER WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionPaperStock, (540, 230))

        blitText.blit_text(screen, "RECYCLED PAPER STOCK", (260, 142), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (250, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scorePaper >= 50:
                        townView.scorePaper -= 50
                        textWorker = "You have now " + str(townView.scorePaper) + " PAPER WASTE!\n\n" \
                                                                                  "You just created a recycled paper stock! Congrats!\n" \
                                                                                  "          I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough paper waste\n" \
                                     "     to create a paper stock!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (255, 255, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()


def info_notebook(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((255, 255, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 30 PAPER WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  The recycling of paper is the process by\n" \
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

    textWorker = "You have now " + str(townView.scorePaper) + " PAPER WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionNotebooks, (550, 230))

        blitText.blit_text(screen, "RECYCLED PAPER NOTEBOOKS", (220, 142), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (250, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scorePaper >= 30:
                        townView.scorePaper -= 30
                        textWorker = "You have now " + str(townView.scorePaper) + " PAPER WASTE!\n\n" \
                                                                                  "You just created rcycled notebooks! Congrats!\n" \
                                                                                  "          I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough paper waste\n" \
                                     "     to create notebooks!\n" \
                                     "Recycle more in order to create them!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (255, 255, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()


def info_napkins(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((255, 255, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 10 PAPER WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  The recycling of paper is the process by\n" \
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

    textWorker = "You have now " + str(townView.scorePaper) + " PAPER WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionNapkins, (540, 230))

        blitText.blit_text(screen, "RECYCLED PAPER NAPKINS", (260, 142), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (250, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scorePaper >= 10:
                        townView.scorePaper -= 10
                        textWorker = "You have now " + str(townView.scorePaper) + " PAPER WASTE!\n\n" \
                                                                                  "You just created recycled paper napkins! Congrats!\n" \
                                                                                  "          I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough paper waste\n" \
                                     "     to create paper napkins!\n" \
                                     "Recycle more in order to create them!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (255, 255, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()


def info_pencils(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((255, 255, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 30 PAPER WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  The recycling of paper is the process by\n" \
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

    textWorker = "You have now " + str(townView.scorePaper) + " PAPER WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionPencils, (540, 230))

        blitText.blit_text(screen, "RECYCLED PAPER PENCILS", (260, 142), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (250, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scorePaper >= 30:
                        townView.scorePaper -= 30
                        textWorker = "You have now " + str(townView.scorePaper) + " PAPER WASTE!\n\n" \
                                                                                  "You just created recycled paper pencils! Congrats!\n" \
                                                                                  "          I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough paper waste\n" \
                                     "     to create paper pencils!\n" \
                                     "Recycle more in order to create them!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (255, 255, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()


def info_book(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((255, 255, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 80 PAPER WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  The recycling of paper is the process by\n" \
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

    textWorker = "You have now " + str(townView.scorePaper) + " PAPER WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionBook, (540, 230))

        blitText.blit_text(screen, "BOOK", (300, 142), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (250, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scorePaper >= 80:
                        townView.scorePaper -= 80
                        textWorker = "You have now " + str(townView.scorePaper) + " PAPER WASTE!\n\n" \
                                                                                  "You just created a book! Congrats!\n" \
                                                                                  "     I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough paper waste\n" \
                                     "       to create a book!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (255, 255, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()


def info_cups(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((255, 255, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 20 PAPER WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  The recycling of paper is the process by\n" \
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

    textWorker = "You have now " + str(townView.scorePaper) + " PAPER WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionCups, (540, 230))

        blitText.blit_text(screen, "RECYCLED PAPER CUPS", (260, 142), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (250, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scorePaper >= 20:
                        townView.scorePaper -= 20
                        textWorker = "You have now " + str(townView.scorePaper) + " PAPER WASTE!\n\n" \
                                                                                  "You just created recycled paper cups! Congrats!\n" \
                                                                                  "          I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough paper waste\n" \
                                     "     to create paper cups!\n" \
                                     "Recycle more in order to create them!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (255, 255, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()
