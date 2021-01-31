import pygame

import BUTTON
import blitText
import drawButton
import townView

# backgrounds
recycling_factory = pygame.image.load('design/backgrounds/recycling_factory.jpg')

# descriptions
descriptionBioFuel1 = pygame.image.load('design/recycled items/organic/description bio fuel 1.png')
descriptionBioFuel2 = pygame.image.load('design/recycled items/organic/description bio fuel 2.png')
descriptionFertilizer1 = pygame.image.load('design/recycled items/organic/description fertilizer 1.png')
descriptionFertilizer2 = pygame.image.load('design/recycled items/organic/description fertilizer 2.png')

def info_bioFuel(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((255, 180, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255),850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 300 ORGANIC WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Biofuels are designed to replace gasoline, diesel\n" \
           "fuel and coal, which are called “fossil fuels” \n" \
           "because they are made from animals and plants that\n" \
           "died millions of years ago.\n\n\n" \
           "  Biofuels are made mostly from plants that have\n" \
           "just been harvested.\n\n\n" \
           "  Biofuels are looked at as a means of replacing ALL\n" \
           "of human energy needs from home heating to vehicle\n" \
           "fuel to electricity generation."

    textWorker = "You have now " +str(townView.scoreOrganic)+ " ORGANIC WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionBioFuel1, (530, 50))
        screen.blit(descriptionBioFuel2, (530, 280))

        blitText.blit_text(screen, "BIOFUEL", (280, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scoreOrganic >= 300:
                        townView.scoreOrganic -= 300
                        textWorker = "You have now " +str(townView.scoreOrganic)+ " ORGANIC WASTE!\n\n"\
                                     "You just created biofuel! Congrats!\n" \
                                     "    I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough organic waste\n" \
                                     "        to create biofuel!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (255, 180, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_compost(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((255, 180, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 50 ORGANIC WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  The soil in which a plant grows plays the most important role because\n" \
                "the various minerals and organic nutrients in the soil make sure\n" \
                "that it is healthy.\n\n\n"\
                " Compost is added in order to improve the quality, structure and\n" \
                "texture of the soil, increasing the amount of nutrients for plants.\n\n\n"\
                "  Compost can be made of paper materials as long as there is no\n" \
                "plastic coating, dried out egg-shells, leaves and garden trimmings,\n" \
                "fruits and vegetables, coffee and tea leaves.\n" \
                "  Practically, it uses organic matter that you produce in your\n" \
                "kitchen or around the house."

    textWorker = "You have now " + str(townView.scoreOrganic) + " ORGANIC WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionFertilizer2, (420, 58))
        screen.blit(descriptionFertilizer1, (580, 280))

        blitText.blit_text(screen, "COMPOST", (280, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (230, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scoreOrganic >= 50:
                        townView.scoreOrganic -= 50
                        textWorker = "You have now " + str(townView.scoreOrganic) + " ORGANIC WASTE!\n\n" \
                                                                           "You just created compost! Congrats!\n" \
                                                                           "    I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough organic waste\n" \
                                     "        to create compost!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (255, 180, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()