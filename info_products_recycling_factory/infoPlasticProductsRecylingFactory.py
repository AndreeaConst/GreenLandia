
# backgrounds
import pygame

import BUTTON
import blitText
import drawButton
import townView

# descriptions
recycling_factory = pygame.image.load('design/backgrounds/recycling_factory.jpg')

# decriptions
plastic_utensils = pygame.image.load('design/recycled items/plastic/plastic_utensils.png')
descriptionUtensils = pygame.image.load('design/recycled items/plastic/description utensils.jpg')
descriptionSchoolbag = pygame.image.load('design/recycled items/plastic/description schoolbag.png')
descriptionPlasticBottle = pygame.image.load('design/recycled items/plastic/description plastic bottle.png')
descriptionCap = pygame.image.load('design/recycled items/plastic/description cap.png')
descriptionShoe = pygame.image.load('design/recycled items/plastic/description shoe.png')

def info_cap(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((200, 10, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 30 PLASTIC WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "    Recycled plastics are plastic made from\n" \
                "recycled plastic materials. In other words,\n" \
                "products that are recycled into something new.\n\n" \
                "  Upon collection, the plastic is then cleaned,\n" \
                "processed into flakes and heated into pellets,\n" \
                "before being stretched into a yarn-like fiber\n" \
                "and woven into a functional fabric. Like a cap!" \

    textWorker = "You have now " + str(townView.scorePlastic) + " PLASTIC WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionCap, (520, 230))

        blitText.blit_text(screen, "RECYCLED PLASTIC CAP", (240, 142), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (250, 240), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scorePlastic >= 30:
                        townView.scorePlastic -= 30
                        textWorker = "You have now " + str(townView.scorePlastic) + " PLASTIC WASTE!\n\n" \
                                                                           "You just created a recycled plastic cap! Congrats!\n" \
                                                                           "          I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough plastic waste\n" \
                                     "        to create a cap!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (200, 10, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_bioUtensils(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((200, 10, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 50 PLASTIC WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 35)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Utensils manufactured with recycled plastic can be recycled again using existing recycling\n" \
                "resources.\n\n" \
                "  Recycled plastics are plastic made from recycled plastic materials. In other words, products\n" \
                "that are recycled into something new.\n\n" \
                "  While this is a great alternative to keeping a product out of the landfill, there are still\n" \
                "resources that go into the process of collecting and recycling an item.\n\n" \
                "  So still, it is better to avoid plastic utensils as much as you can!"

    textWorker = "You have now " + str(townView.scorePlastic) + " PLASTIC WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(plastic_utensils, (650, 65))
        screen.blit(descriptionUtensils, (580, 355))

        blitText.blit_text(screen, "REUSABLE UTENSILS", (210, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (230, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scorePlastic >= 50:
                        townView.scorePlastic -= 50
                        textWorker = "You have now " + str(townView.scorePlastic) + " PLASTIC WASTE!\n\n" \
                                                                           "You just created recycled utensils! Congrats!\n" \
                                                                           "         I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough plastic waste\n" \
                                     "     to create recycled utensils!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (200, 10, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_plasticBackpack(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((200, 10, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 70 PLASTIC WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Recycled plastics are plastic made from recycled plastic\n" \
                "materials. In other words, products that are recycled into\n" \
                "something new.\n\n" \
                "  Upon collection, the plastic is then cleaned, processed into\n" \
                "flakes and heated into pellets, before being stretched into a\n" \
                "yarn-like fiber and woven into a functional fabric. Items from\n" \
                "this collection are shipped in a zero-waste packaging solution:\n" \
                "water-resistant reversible tote bags." \

    textWorker = "You have now " + str(townView.scorePlastic) + " PLASTIC WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionSchoolbag, (550, 250))

        blitText.blit_text(screen, "RECYCLED PLASTIC SCHOOLBAG", (200, 142), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (230, 270), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scorePlastic >= 70:
                        townView.scorePlastic -= 70
                        textWorker = "You have now " + str(townView.scorePlastic) + " PLASTIC WASTE!\n\n" \
                                                                           "You just created a recycled plastic schoolbag! Congrats!\n" \
                                                                           "          I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough plastic waste\n" \
                                     "       to create a schoolbag!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (200, 10, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_plasticBottle(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((200, 10, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 10 PLASTIC WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  After you put your plastic bottle into\n" \
                "the right bin, it is also sorted by the\n" \
                "type of plastic it is made from. Then, the\n" \
                "bottle is cleaned from any food, liquid,\n" \
                "or chemical residue.\n\n" \
                "  Next, all of the bottles are ground up\n" \
                "and shredded into flakes. Finally, they are\n" \
                "melted down and formed into small pellets,\n" \
                "each about the size of a grain of rice.\n" \
                "The pellets are bundled up and sold to\n" \
                "companies that can be melt them and make\n" \
                "them into many different products.\n" \
                "Just like a plastic bottle!" \

    textWorker = "You have now " + str(townView.scorePlastic) + " PLASTIC WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionPlasticBottle, (520, 230))

        blitText.blit_text(screen, "RECYCLED PLASTIC BOTTLE", (240, 142), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (250, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scorePlastic >= 10:
                        townView.scorePlastic -= 10
                        textWorker = "You have now " + str(townView.scorePlastic) + " PLASTIC WASTE!\n\n" \
                                                                           "You just created a recycled plastic bottle! Congrats!\n" \
                                                                           "          I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough plastic waste\n" \
                                     "     to create a plastic bottle!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (200, 10, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_shoe(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((200, 10, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 50 PLASTIC WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "    Recycled plastics are plastic made from\n" \
                "recycled plastic materials. In other words,\n" \
                "products that are recycled into something new.\n\n" \
                "  Upon collection, the plastic is then cleaned,\n" \
                "processed into flakes and heated into pellets,\n" \
                "before being stretched into a yarn-like fiber\n" \
                "and woven into a functional fabric. Like shoes!" \

    textWorker = "You have now " + str(townView.scorePlastic) + " PLASTIC WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionShoe, (520, 230))

        blitText.blit_text(screen, "RECYCLED PLASTIC SHOE", (240, 142), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (250, 260), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scorePlastic >= 50:
                        townView.scorePlastic -= 50
                        textWorker = "You have now " + str(townView.scorePlastic) + " PLASTIC WASTE!\n\n" \
                                                                           "You just created recycled plastic shoes! Congrats!\n" \
                                                                           "          I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough plastic waste\n" \
                                     "        to create shoes!\n" \
                                     "Recycle more in order to create them!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (200, 10, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()