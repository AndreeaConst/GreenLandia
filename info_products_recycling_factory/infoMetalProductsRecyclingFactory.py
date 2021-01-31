import pygame

# backgrounds
import BUTTON
import blitText
import drawButton
import townView

recycling_factory = pygame.image.load('design/backgrounds/recycling_factory.jpg')

# descriptions
descriptionMetalBench = pygame.image.load('design/recycled items/metal/description metal bench.jpg')
descriptionMetalChair = pygame.image.load('design/recycled items/metal/description metal chair.png')
descriptionMetalCoffeeMaker = pygame.image.load('design/recycled items/metal/description metal coffeemaker.png')
descriptionCar = pygame.image.load('design/recycled items/metal/description car.png')
descriptionPlane = pygame.image.load('design/recycled items/metal/description plane.png')
descriptionMetalLamp = pygame.image.load('design/recycled items/metal/description metal lamp.png')
descriptionFridge = pygame.image.load('design/recycled items/metal/description fridge.png')
descriptionMetalUtensils = pygame.image.load('design/recycled items/metal/description metal utensils.png')
descriptionMicrowave = pygame.image.load('design/recycled items/metal/description microwave.png')
descriptionOven = pygame.image.load('design/recycled items/metal/description oven.png')
descriptionToaster = pygame.image.load('design/recycled items/metal/description toaster.png')

def info_metalBench(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 60 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this metal bench here!" \

    textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionMetalBench, (560, 240))

        blitText.blit_text(screen, "METAL BENCH", (240, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scoreMetal >= 60:
                        townView.scoreMetal -= 60
                        textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!\n\n" \
                                                                         "You just created a metal bench! Congrats!\n" \
                                                                         "      I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough metal waste\n" \
                                     "     to create a metal bench!\n" \
                                     "Recycle more in order to create it"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (50, 0, 200)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_metalChair(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 40 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this metal chair here!" \

    textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionMetalChair, (560, 240))

        blitText.blit_text(screen, "METAL CHAIR", (240, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scoreMetal >= 40:
                        townView.scoreMetal -= 40
                        textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!\n\n" \
                                                                         "You just created a metal chair! Congrats!\n" \
                                                                         "      I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough metal waste\n" \
                                     "     to create a metal chair!\n" \
                                     "Recycle more in order to create it"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (50, 0, 200)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_metalCoffeemaker(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 50 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this metal coffeemaker here!" \

    textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionMetalCoffeeMaker, (560, 200))

        blitText.blit_text(screen, "METAL COFFEEMAKER", (240, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scoreMetal >= 50:
                        townView.scoreMetal -= 50
                        textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!\n\n" \
                                                                         "You just created a metal coffeemaker! Congrats!\n" \
                                                                         "          I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough metal waste\n" \
                                     "  to create a metal coffeemaker!\n" \
                                     "Recycle more in order to create it"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (50, 0, 200)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_car(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 200 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this car here!" \

    textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionCar, (560, 260))

        blitText.blit_text(screen, "CAR", (280, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scoreMetal >= 200:
                        townView.scoreMetal -= 200
                        textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!\n\n" \
                                                                         "You just created a car! Congrats!\n" \
                                                                         "    I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough metal waste\n" \
                                     "        to create a car!\n" \
                                     "Recycle more in order to create it"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (50, 0, 200)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_plane(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 300 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this plane here!" \

    textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionPlane, (560, 240))

        blitText.blit_text(screen, "PLANE", (240, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scoreMetal >= 300:
                        townView.scoreMetal -= 300
                        textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!\n\n" \
                                                                         "You just created a plane! Congrats!\n" \
                                                                         "     I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough metal waste\n" \
                                     "       to create a plane!\n" \
                                     "Recycle more in order to create it"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (50, 0, 200)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_metalLamp(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 20 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this metal lamp here!" \

    textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionMetalLamp, (630, 220))

        blitText.blit_text(screen, "METAL LAMP", (240, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scoreMetal >= 20:
                        townView.scoreMetal -= 20
                        textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!\n\n" \
                                                                         "You just created a metal lamp! Congrats!\n" \
                                                                         "      I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough metal waste\n" \
                                     "     to create a metal lamp!\n" \
                                     "Recycle more in order to create it"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (50, 0, 200)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()


def info_fridge(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 90 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this fridge here!" \

    textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionFridge, (560, 240))

        blitText.blit_text(screen, "FRIDGE", (240, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scoreMetal >= 90:
                        townView.scoreMetal -= 90
                        textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!\n\n" \
                                                                         "You just created a fridge! Congrats!\n" \
                                                                         "     I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough metal waste\n" \
                                     "       to create a fridge!\n" \
                                     "Recycle more in order to create it"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (50, 0, 200)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_metalUtensils(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 20 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made these metal utensils here!" \

    textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionMetalUtensils, (560, 240))

        blitText.blit_text(screen, "METAL UTENSILS", (240, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scoreMetal >= 20:
                        townView.scoreMetal -= 20
                        textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!\n\n" \
                                                                         "You just created metal utensils! Congrats!\n" \
                                                                         "        I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough metal waste\n" \
                                     "     to create metal utensils!\n" \
                                     "Recycle more in order to create them!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (50, 0, 200)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_microwave(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 70 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this microwave here!" \

    textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionMicrowave, (560, 240))

        blitText.blit_text(screen, "MICROWAVE", (240, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scoreMetal >= 70:
                        townView.scoreMetal -= 70
                        textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!\n\n" \
                                                                         "You just created a microwave! Congrats!\n" \
                                                                         "      I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough metal waste\n" \
                                     "     to create a microwave!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (50, 0, 200)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_oven(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 90 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this oven here!" \

    textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionOven, (560, 240))

        blitText.blit_text(screen, "OVEN", (240, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scoreMetal >= 90:
                        townView.scoreMetal -= 90
                        textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!\n\n" \
                                                                         "You just created an oven! Congrats!\n" \
                                                                         "     I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough metal waste\n" \
                                     "     to create an oven!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (50, 0, 200)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_toaster(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 40 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this toaster here!" \

    textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionToaster, (560, 240))

        blitText.blit_text(screen, "TOASTER", (230, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if townView.scoreMetal >= 40:
                        townView.scoreMetal -= 40
                        textWorker = "You have now " + str(townView.scoreMetal) + " METAL WASTE!\n\n" \
                                                                         "You just created a toaster! Congrats!\n" \
                                                                         "      I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough metal waste\n" \
                                     "       to create a toaster!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (50, 0, 200)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()
