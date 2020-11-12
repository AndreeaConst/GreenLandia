import pygame, BUTTON, os, drawButton, visitRecyclingArea, blitText
from pygame import mixer

os.environ['SDL_VIDEO_CENTERED'] = '1' #for centering the window game

#Backgrounds
town_view = pygame.image.load('images/town.png')
townhall = pygame.image.load('images/townhall.png')
recycling_factory = pygame.image.load('images/recycling_factory.jpg')

#Objects
arrow_right = pygame.image.load('arrows/arrow_right.png')
arrow_down = pygame.image.load('arrows/arrow_down.png')
arrow_up = pygame.image.load('arrows/arrow_up.png')
arrow_left = pygame.image.load('arrows/arrow_left.png')

descriptionBioFuel1 = pygame.image.load('recycled items/organic/description bio fuel 1.png')
descriptionBioFuel2 = pygame.image.load('recycled items/organic/description bio fuel 2.png')
descriptionFertilizer1 = pygame.image.load('recycled items/organic/description fertilizer 1.png')
descriptionFertilizer2 = pygame.image.load('recycled items/organic/description fertilizer 2.png')
descriptionUtensils = pygame.image.load('recycled items/plastic/description utensils.jpg')
descriptionSchoolbag = pygame.image.load('recycled items/plastic/description schoolbag.png')
descriptionPlasticBottle = pygame.image.load('recycled items/plastic/description plastic bottle.png')
descriptionPaperStock = pygame.image.load('recycled items/paper/description paper stock.jpg')
descriptionNotebooks = pygame.image.load('recycled items/paper/description notebooks.png')
descriptionNapkins = pygame.image.load('recycled items/paper/description napkins.jpg')
descriptionCap = pygame.image.load('recycled items/plastic/description cap.png')
descriptionShoe = pygame.image.load('recycled items/plastic/description shoe.png')
descriptionPencils = pygame.image.load('recycled items/paper/description pencils.jpg')
descriptionBook = pygame.image.load('recycled items/paper/description book.png')
descriptionCups = pygame.image.load('recycled items/paper/description cups.png')
descriptionGlassBottle = pygame.image.load('recycled items/glass/description glass bottle.png')
descriptionFiberGlass = pygame.image.load('recycled items/glass/description fiber glass.png')
descriptionGlassBricks = pygame.image.load('recycled items/glass/description glass bricks.jpg')
descriptionMetalBench = pygame.image.load('recycled items/metal/description metal bench.jpg')
descriptionMetalChair = pygame.image.load('recycled items/metal/description metal chair.png')
descriptionMetalCoffeeMaker = pygame.image.load('recycled items/metal/description metal coffeemaker.png')
descriptionCar = pygame.image.load('recycled items/metal/description car.png')
descriptionPlane = pygame.image.load('recycled items/metal/description plane.png')
descriptionMetalLamp = pygame.image.load('recycled items/metal/description metal lamp.png')
descriptionGlassphalt1 = pygame.image.load('recycled items/glass/description glassphalt 1.jpg')
descriptionGlassphalt2 = pygame.image.load('recycled items/glass/description glassphalt 2.jpg')
descriptionReflectivePaint = pygame.image.load('recycled items/glass/description reflective paint.png')
descriptionGlassTiles1 = pygame.image.load('recycled items/glass/description glass tiles 1.jpg')
descriptionGlassTiles2 = pygame.image.load('recycled items/glass/description glass tiles 2.jpg')
descriptionGlassTiles3 = pygame.image.load('recycled items/glass/description glass tiles 3.jpg')
descriptionFridge = pygame.image.load('recycled items/metal/description fridge.png')
descriptionMetalUtensils = pygame.image.load('recycled items/metal/description metal utensils.png')
descriptionMicrowave = pygame.image.load('recycled items/metal/description microwave.png')
descriptionOven = pygame.image.load('recycled items/metal/description oven.png')
descriptionToaster = pygame.image.load('recycled items/metal/description toaster.png')

bio_fuel = pygame.image.load('recycled items/organic/biofuel.png')
compost = pygame.image.load('recycled items/organic/fertilizer.png')

plastic_utensils = pygame.image.load('recycled items/plastic/plastic_utensils.png')
bottle = pygame.image.load('recycled items/plastic/bottle.jpg')
cap = pygame.image.load('recycled items/plastic/cap.png')
shoe = pygame.image.load('recycled items/plastic/shoe.png')
schoolbag = pygame.image.load('recycled items/plastic/schoolbag.png')

recycled_paper = pygame.image.load('recycled items/paper/paper.jpg')
notebook = pygame.image.load('recycled items/paper/notebook.jpg')
napkin = pygame.image.load('recycled items/paper/napkin.jpg')
pencils = pygame.image.load('recycled items/paper/pencils.png')
book = pygame.image.load('recycled items/paper/book.jpg')
paper_cups = pygame.image.load('recycled items/paper/paper cups.jpg')

plane = pygame.image.load('recycled items/metal/plane.png')
car = pygame.image.load('recycled items/metal/car.jpg')
lamp = pygame.image.load('recycled items/metal/lamp.jpg')
bench = pygame.image.load('recycled items/metal/bench.jpg')
chair = pygame.image.load('recycled items/metal/chair.jpg')
coffemaker = pygame.image.load('recycled items/metal/coffeemaker.jpg')
fridge = pygame.image.load('recycled items/metal/fridge.jpg')
metal_utensils = pygame.image.load('recycled items/metal/metal utensils.jpg')
microwave = pygame.image.load('recycled items/metal/microwave.jpg')
oven = pygame.image.load('recycled items/metal/oven.jpg')
toaster = pygame.image.load('recycled items/metal/toaster.jpg')

glass_bottle = pygame.image.load('recycled items/glass/glass bottle.png')
fiber_glass = pygame.image.load('recycled items/glass/fiberglass.jpg')
glass_bricks = pygame.image.load('recycled items/glass/glass bricks.jpg')
glassphalt = pygame.image.load('recycled items/glass/glassphalt.jpg')
reflective_paint = pygame.image.load('recycled items/glass/reflective paint.png')
tiles = pygame.image.load('recycled items/glass/tiles.jpg')

#Characters
mayor_normal_pose = pygame.image.load('poses/mayor_normal_pose.png')
worker = pygame.image.load('poses/worker.png')

#soundtrack
town_music = mixer.Sound('music/town.wav')
recycling_factory_music = mixer.Sound('music/recycling_factory.wav')

# Title and Icon
pygame.display.set_caption("Green Landia")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

#Others
menuButton = BUTTON.button((255, 255, 255), 300, 180, 300, 70, 'START GAME')
scorePlastic, scoreOrganic, scoreMetal, scorePaper, scoreGlass = 0, 0, 0, 0, 0


#FUNCTIONS-----------------------------------------------------------------------------

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
    global scoreOrganic
    textWorker = "You have now " +str(scoreOrganic)+ " ORGANIC WASTE!"
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
                    if scoreOrganic >= 300:
                        scoreOrganic -= 300
                        textWorker = "You have now " +str(scoreOrganic)+ " ORGANIC WASTE!\n\n"\
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

    global scoreOrganic
    textWorker = "You have now " + str(scoreOrganic) + " ORGANIC WASTE!"
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
                    if scoreOrganic >= 50:
                        scoreOrganic -= 50
                        textWorker = "You have now " + str(scoreOrganic) + " ORGANIC WASTE!\n\n" \
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

    global scorePlastic
    textWorker = "You have now " + str(scorePlastic) + " PLASTIC WASTE!"
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
                    if scorePlastic >= 50:
                        scorePlastic -= 50
                        textWorker = "You have now " + str(scorePlastic) + " PLASTIC WASTE!\n\n" \
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

    global scorePlastic
    textWorker = "You have now " + str(scorePlastic) + " PLASTIC WASTE!"
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
                    if scorePlastic >= 70:
                        scorePlastic -= 70
                        textWorker = "You have now " + str(scorePlastic) + " PLASTIC WASTE!\n\n" \
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

    global scorePlastic
    textWorker = "You have now " + str(scorePlastic) + " PLASTIC WASTE!"
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
                    if scorePlastic >= 10:
                        scorePlastic -= 10
                        textWorker = "You have now " + str(scorePlastic) + " PLASTIC WASTE!\n\n" \
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

    global scorePaper
    textWorker = "You have now " + str(scorePaper) + " PAPER WASTE!"
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
                    if scorePaper >= 50:
                        scorePaper -= 50
                        textWorker = "You have now " + str(scorePaper) + " PAPER WASTE!\n\n" \
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

    global scorePaper
    textWorker = "You have now " + str(scorePaper) + " PAPER WASTE!"
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
                    if scorePaper >= 30:
                        scorePaper -= 30
                        textWorker = "You have now " + str(scorePaper) + " PAPER WASTE!\n\n" \
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

    global scorePaper
    textWorker = "You have now " + str(scorePaper) + " PAPER WASTE!"
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
                    if scorePaper >= 10:
                        scorePaper -= 10
                        textWorker = "You have now " + str(scorePaper) + " PAPER WASTE!\n\n" \
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

    global scorePlastic
    textWorker = "You have now " + str(scorePlastic) + " PLASTIC WASTE!"
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
                    if scorePlastic >= 30:
                        scorePlastic -= 30
                        textWorker = "You have now " + str(scorePlastic) + " PLASTIC WASTE!\n\n" \
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

    global scorePlastic
    textWorker = "You have now " + str(scorePlastic) + " PLASTIC WASTE!"
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
                    if scorePlastic >= 50:
                        scorePlastic -= 50
                        textWorker = "You have now " + str(scorePlastic) + " PLASTIC WASTE!\n\n" \
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

    global scorePaper
    textWorker = "You have now " + str(scorePaper) + " PAPER WASTE!"
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
                    if scorePaper >= 30:
                        scorePaper -= 30
                        textWorker = "You have now " + str(scorePaper) + " PAPER WASTE!\n\n" \
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

        global scorePaper
        textWorker = "You have now " + str(scorePaper) + " PAPER WASTE!"
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
                        if scorePaper >= 80:
                            scorePaper -= 80
                            textWorker = "You have now " + str(scorePaper) + " PAPER WASTE!\n\n" \
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

        global scorePaper
        textWorker = "You have now " + str(scorePaper) + " PAPER WASTE!"
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
                        if scorePaper >= 20:
                            scorePaper -= 20
                            textWorker = "You have now " + str(scorePaper) + " PAPER WASTE!\n\n" \
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

def info_glassBottle(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((0, 150, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 20 GLASS WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Glass bottles and jars are infinitely recyclable.\n" \
                "Glass recycling is the processing of waste\n" \
                "glass into usable products, like these glass\n" \
                "bottles here.\n\n\n" \
                "  To be recycled, glass waste needs to be\n" \
                "purified and cleaned of contamination. Then,\n" \
                "it might also have to be separated into different\n" \
                "colors. Many recyclers collect different colors of\n" \
                "glass separately since glass retains its color after\n" \
                "recycling." \

    global scoreGlass
    textWorker = "You have now " + str(scoreGlass) + " GLASS WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionGlassBottle, (530, 220))

        blitText.blit_text(screen, "RECYCLED GLASS BOTTLE", (200, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if scoreGlass >= 20:
                        scoreGlass -= 20
                        textWorker = "You have now " + str(scoreGlass) + " GLASS WASTE!\n\n" \
                                                                           "You just created a glass bottle! Congrats!\n" \
                                                                           "      I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough glass waste\n" \
                                     "     to create a glass bottle!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (0, 150, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_fiberGlass(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((0, 150, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 20 GLASS WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Fiberglass is material made from extremely\n" \
                "fine fibers of glass.\n\n\n" \
                "  Fiberglass is used in the telecommunications\n" \
                "industry for shrouding antennas. Other uses include\n" \
                "sheet-form electrical insulators and structural\n" \
                "components commonly found in power-industry products.\n\n" \
                "  Because of fiberglass's light weight and durability,\n" \
                "it is often used in protective equipment such as helmets.\n" \
                "Many sports use fiberglass protective gear, such as\n" \
                "goaltenders' and catchers' masks." \

    global scoreGlass
    textWorker = "You have now " + str(scoreGlass) + " GLASS WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionFiberGlass, (560, 220))

        blitText.blit_text(screen, "FIBER GLASS", (240, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if scoreGlass >= 20:
                        scoreGlass -= 20
                        textWorker = "You have now " + str(scoreGlass) + " GLASS WASTE!\n\n" \
                                                                         "You just created fiber glass! Congrats!\n" \
                                                                         "      I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough glass waste\n" \
                                     "     to create fiber glass!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (0, 150, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_glassBricks(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((0, 150, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 20 GLASS WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Glass brick, also known as glass block,\n" \
                "is an architectural element made from glass.\n\n" \
                "  The appearance of glass blocks can vary in\n" \
                "color, size, texture and form.\n\n" \
                "  Glass bricks provide visual obscuration while\n" \
                "admitting light.\n\n" \
                "  Today glass blocks are used in walls, skylights,\n" \
                "and sidewalk lights." \

    global scoreGlass
    textWorker = "You have now " + str(scoreGlass) + " GLASS WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionGlassBricks, (560, 220))

        blitText.blit_text(screen, "GLASS BRICKS", (240, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if scoreGlass >= 20:
                        scoreGlass -= 20
                        textWorker = "You have now " + str(scoreGlass) + " GLASS WASTE!\n\n" \
                                                                         "You just created glass bricks! Congrats!\n" \
                                                                         "      I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough glass waste\n" \
                                     "     to create glass bricks!\n" \
                                     "Recycle more in order to create them!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (0, 150, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

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

    global scoreMetal
    textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!"
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
                    if scoreMetal >= 60:
                        scoreMetal -= 60
                        textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!\n\n" \
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

    global scoreMetal
    textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!"
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
                    if scoreMetal >= 40:
                        scoreMetal -= 40
                        textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!\n\n" \
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

    global scoreMetal
    textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!"
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
                    if scoreMetal >= 50:
                        scoreMetal -= 50
                        textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!\n\n" \
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

    global scoreMetal
    textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!"
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
                    if scoreMetal >= 200:
                        scoreMetal -= 200
                        textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!\n\n" \
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

    global scoreMetal
    textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!"
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
                    if scoreMetal >= 300:
                        scoreMetal -= 300
                        textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!\n\n" \
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

    global scoreMetal
    textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!"
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
                    if scoreMetal >= 20:
                        scoreMetal -= 20
                        textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!\n\n" \
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

def info_glassphalt(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((0, 150, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 50 GLASS WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  You may not realize it, but you drive over glass\n" \
                "every day.\n" \
                "  Glass is ground and added to other aggregate\n" \
                "materials and to surface parking lots and concrete\n" \
                "pavement.\n\n" \
                "  As a base material, recycled glass enhances the\n" \
                "performance of gravel in an aggregate mix.\n\n" \
                "  Recycled glass is used to make glassphalt,\n" \
                "a material that is applied to roads, highways\n" \
                "and even airport runways to make these surfaces\n" \
                "less slippery and less prone to cracking." \

    global scoreGlass
    textWorker = "You have now " + str(scoreGlass) + " GLASS WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionGlassphalt1, (560, 420))
        screen.blit(descriptionGlassphalt2, (560, 200))


        blitText.blit_text(screen, "GLASSPHALT", (250, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if scoreGlass >= 50:
                        scoreGlass -= 50
                        textWorker = "You have now " + str(scoreGlass) + " GLASS WASTE!\n\n" \
                                                                         "You just created glassphalt! Congrats!\n" \
                                                                         "      I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough glass waste\n" \
                                     "     to create glassphalt!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (0, 150, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_reflectivePaint(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((0, 150, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 20 GLASS WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  Reflective paint is regular paint with a reflective quality.\n" \
                "Reflectivity in paint is made possible by adding tiny spheres\n" \
                "or flakes of material like glass that gives the paint a reflective\n" \
                "quality.\n\n\n" \
                "  Reflectivity happens when light hits and bounces off the\n" \
                "added material.\n\n\n" \
                "  Road signs, road stripes, speed bumps, and reflective\n" \
                "tape are all examples of the use of reflectivity. When a\n" \
                "light source like your car headlights hit a surface that's\n" \
                "painted using a reflective additive, like glass beads, the\n" \
                "additive acts as a prism and reflects the light back in the\n" \
                "direction of its source."


    global scoreGlass
    textWorker = "You have now " + str(scoreGlass) + " GLASS WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionReflectivePaint, (560, 250))

        blitText.blit_text(screen, "REFLECTIVE PAINT", (250, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if scoreGlass >= 20:
                        scoreGlass -= 20
                        textWorker = "You have now " + str(scoreGlass) + " GLASS WASTE!\n\n" \
                                                                         "You just created reflective paint! Congrats!\n" \
                                                                         "      I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough glass waste\n" \
                                     "    to create reflective paint!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (0, 150, 0)
                else:
                    createButton.color = (255, 255, 255)

        pygame.display.update()

def info_glassTiles(screen, worker):
    table1 = BUTTON.button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = BUTTON.button((0, 150, 0), 200, 50, 590, 133, ' ')
    text_button = BUTTON.button((255, 255, 255), 850, 50, 350, 200, ' ')
    createButton = BUTTON.button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 50 GLASS WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    textTable = "  The variety of garden and landscape products made from recycled glass has led to\n" \
                "the term 'greenscaping'. Unlike wood, glass mulch doesn't absorb moisture, which improves\n" \
                "water delivery while reducing the frequency of watering.\n\n" \
                "  It also comes in a wide variety of colors. Manufacturers combine recycled glass with\n" \
                "crushed porcelain embedded in concrete slab to create decorative pathways and patios."

    global scoreGlass
    textWorker = "You have now " + str(scoreGlass) + " GLASS WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        drawButton.drawButton(screen, table1, 13, (0, 0, 0))
        drawButton.drawButton(screen, table2, 13, (0, 0, 0))
        drawButton.drawButton(screen, createButton, 13, (0, 0, 0))
        drawButton.drawButton(screen, text_button, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(descriptionGlassTiles1, (210, 350))
        screen.blit(descriptionGlassTiles3, (405, 400))
        screen.blit(descriptionGlassTiles2, (600, 350))

        blitText.blit_text(screen, "GLASS TILES", (250, 138), font2, (0, 0, 0))
        blitText.blit_text(screen, textTable, (240, 220), font1, (0, 0, 0))
        blitText.blit_text(screen, textWorker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if createButton.isOver(pos):
                    if scoreGlass >= 50:
                        scoreGlass -= 50
                        textWorker = "You have now " + str(scoreGlass) + " GLASS WASTE!\n\n" \
                                                                         "You just created glass tiles! Congrats!\n" \
                                                                         "      I am indeed proud of you!"
                    else:
                        textWorker = "You don't have enough glass waste\n" \
                                     "      to create glass tiles!\n" \
                                     "Recycle more in order to create them!"
            if event.type == pygame.MOUSEMOTION:
                if createButton.isOver(pos):
                    createButton.color = (0, 150, 0)
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

    global scoreMetal
    textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!"
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
                    if scoreMetal >= 90:
                        scoreMetal -= 90
                        textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!\n\n" \
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

    global scoreMetal
    textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!"
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
                    if scoreMetal >= 20:
                        scoreMetal -= 20
                        textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!\n\n" \
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

    global scoreMetal
    textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!"
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
                    if scoreMetal >= 70:
                        scoreMetal -= 70
                        textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!\n\n" \
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

    global scoreMetal
    textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!"
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
                    if scoreMetal >= 90:
                        scoreMetal -= 90
                        textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!\n\n" \
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

    global scoreMetal
    textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!"
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
                    if scoreMetal >= 40:
                        scoreMetal -= 40
                        textWorker = "You have now " + str(scoreMetal) + " METAL WASTE!\n\n" \
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

def tableOfContents_recyclingFactory(screen):
    text = "   Hello! I am Paul, the chef worker here.\n   In the box to the left, you have the " \
           " amount of\nrecycled materials of each kind so far and how much\nmaterial we need to recreate something else." \
           "\n   We will create new products and put them\non the market." \
           " You choose which products\nwe can recreate by clicking on them." \
           "\n\n Go to the market after this process!"
    font = pygame.font.SysFont('arial', 20)
    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 30)

    text_button = BUTTON.button((255, 255, 255), 800, 50, 400, 250, ' ')
    table = BUTTON.button((0, 0, 0), 50, 50, 590, 630, ' ')
    glass_square = BUTTON.button((0, 180, 0), 50, 50, 120, 130, ' ')
    metal_square = BUTTON.button((0, 0, 255), 170, 50, 115, 130, ' ')
    organic_square = BUTTON.button((255, 200, 0), 285, 50, 115, 130, ' ')
    paper_square = BUTTON.button((255, 255, 0), 400, 50, 120, 130, ' ')
    plastic_square = BUTTON.button((255, 0, 0), 520, 50, 120, 130, ' ')

    glass = pygame.image.load('trash/trash1.png')
    metal = pygame.image.load('trash/trash12.png')
    organic = pygame.image.load('trash/trash36.png')
    paper = pygame.image.load('trash/trash42.png')
    plastic = pygame.image.load('trash/trash67.png')

    drawButton.drawButton(screen, text_button, 13, (0, 0, 0))  # the message of the worker
    blitText.blit_text(screen, text, (802, 50), font)
    drawButton.drawButton(screen, table, 13, (0, 0, 0))

    drawButton.drawButton(screen, glass_square, 13, (0, 0, 0))
    drawButton.drawButton(screen, metal_square, 13, (0, 0, 0))
    drawButton.drawButton(screen, organic_square, 13, (0, 0, 0))
    drawButton.drawButton(screen, paper_square, 13, (0, 0, 0))
    drawButton.drawButton(screen, plastic_square, 13, (0, 0, 0))

    screen.blit(glass, (43, 30))
    score = font1.render("Glass: " + str(scoreGlass), True, (0, 0, 0))
    screen.blit(score, (80, 150))

    screen.blit(metal, (190, 50))
    score = font1.render("Metal: " + str(scoreMetal), True, (0, 0, 0))
    screen.blit(score, (195, 150))

    screen.blit(organic, (307, 95))
    score = font1.render("Organic: " + str(scoreOrganic), True, (0, 0, 0))
    screen.blit(score, (315, 150))

    screen.blit(paper, (395, 60))
    score = font1.render("Paper: " + str(scorePaper), True, (0, 0, 0))
    screen.blit(score, (430, 150))

    screen.blit(plastic, (510, 70))
    score = font1.render("Plastic: " + str(scorePlastic), True, (0, 0, 0))
    screen.blit(score, (555, 150))

    blitText.blit_text(screen, "BUILD ITEMS", (223, 180), font2, (255, 255, 255))

def moreProductsRight_recyclingFactory(screen, worker):

    while True:
        font3 = pygame.font.SysFont('arialblack', 12)

        tableOfContents_recyclingFactory(screen)

        screen.blit(arrow_left, (50, 422))
        screen.blit(worker, (700, 0))

        z = 250
        const = 2
        for i in range(0, 3):
            y = 80
            if i == 2:
                const += 1
            for j in range(0, const):
                white_square = BUTTON.button((255, 255, 255), y, z, 175, 130, ' ')
                drawButton.drawButton(screen, white_square, 13, (0, 0, 0))
                y += 175
            z += 130

        screen.blit(bio_fuel, (130, 255))
        blitText.blit_text(screen, "        BIOFUEL\n300 ORGANIC WASTE", (92, 344), font3, (0, 0, 0))

        screen.blit(compost, (300, 247))
        blitText.blit_text(screen, "       COMPOST\n50 ORGANIC WASTE", (270, 344), font3, (0, 0, 0))

        screen.blit(cap, (100, 370))
        blitText.blit_text(screen, "         CAP\n30 PLASTIC WASTE", (100, 475), font3, (0, 0, 0))

        screen.blit(shoe, (280, 370))
        blitText.blit_text(screen, "         SHOE\n50 PLASTIC WASTE", (275, 475), font3, (0, 0, 0))

        screen.blit(pencils, (120, 495))
        blitText.blit_text(screen, "RECYCLED PAPER PENCIL\n     30 PAPER WASTE", (80, 607), font3, (0, 0, 0))

        screen.blit(book, (280, 510))
        blitText.blit_text(screen, "        BOOK\n80 PAPER WASTE", (280, 607), font3, (0, 0, 0))

        screen.blit(paper_cups, (470, 510))
        blitText.blit_text(screen, "   PAPER CUPS\n20 PAPER WASTE", (460, 607), font3, (0, 0, 0))

        mx, my  = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if mx >= 40 and mx <= 70 and my >= 420 and my <= 450:
                running = True
                return running
            if event.type == pygame.QUIT:
                running = False
                return running
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mx >= 130 and mx <= 200 and my >= 255 and my <= 350:
                    info_bioFuel(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 300 and mx <= 360 and my >= 247 and my <= 350:
                    info_compost(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 100 and mx <= 200 and my >= 370 and my <= 470:
                    info_cap(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 280 and mx <= 390 and my >= 370 and my <= 460:
                    info_shoe(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 120 and mx <= 210 and my >= 475 and my <= 570:
                    info_pencils(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 280 and mx <= 390 and my >= 510 and my <= 590:
                    info_book(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 470 and mx <= 570 and my >= 510 and my <= 610:
                    info_cups(screen, worker)
                    screen.blit(recycling_factory, (0, 0))

        pygame.display.update()

def moreProductsRight1_recyclingFactory(screen, worker):

    while True:
        font3 = pygame.font.SysFont('arialblack', 12)

        tableOfContents_recyclingFactory(screen)
        screen.blit(arrow_left, (50, 422))
        screen.blit(worker, (700, 0))

        z = 250
        const = 3
        for i in range(0, 3):
            if i == 2:
                const -= 1
            y = 80
            for j in range(0, const):
                white_square = BUTTON.button((255, 255, 255), y, z, 175, 130, ' ')
                drawButton.drawButton(screen, white_square, 13, (0, 0, 0))
                y += 175
            z += 130

        screen.blit(glassphalt, (123, 250))
        blitText.blit_text(screen, "    GLASSPHALT\n50 GLASS WASTE", (107, 345), font3, (0, 0, 0))

        screen.blit(reflective_paint, (293, 250))
        blitText.blit_text(screen, "REFLECTIVE PAINT\n 20 GLASS WASTE", (280, 345), font3, (0, 0, 0))

        screen.blit(tiles, (467, 250))
        blitText.blit_text(screen, "        TILES\n50 GLASS WASTE", (460, 345), font3, (0, 0, 0))

        screen.blit(fridge, (120, 380))
        blitText.blit_text(screen, "      FRIDGE\n90 METAL WASTE", (110, 474), font3, (0, 0, 0))

        screen.blit(metal_utensils, (277, 380))
        blitText.blit_text(screen, "METAL UTENSILS\n20 METAL WASTE", (280, 474), font3, (0, 0, 0))

        screen.blit(microwave, (465, 380))
        blitText.blit_text(screen, "    MICROWAVE\n70 METAL WASTE", (460, 474), font3, (0, 0, 0))

        screen.blit(oven, (116, 510))
        blitText.blit_text(screen, "        OVEN\n90 METAL WASTE", (105, 605), font3, (0, 0, 0))

        screen.blit(toaster, (283, 510))
        blitText.blit_text(screen, "      TOASTER\n40 METAL WASTE", (280, 605), font3, (0, 0, 0))

        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if mx >= 40 and mx <= 70 and my >= 420 and my <= 450:
                running = True
                return running
            if event.type == pygame.QUIT:
                running = False
                return running
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mx >= 123 and mx <= 223 and my >= 250 and my <= 350:
                    info_glassphalt(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 293 and mx <= 380 and my >= 250 and my <= 350:
                    info_reflectivePaint(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 467 and mx <= 567 and my >= 250 and my <= 350:
                    info_glassTiles(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 120 and mx <= 185 and my >= 380 and my <= 470:
                    info_fridge(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 277 and mx <= 380 and my >= 380 and my <= 465:
                    info_metalUtensils(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 465 and mx <= 570 and my >= 380 and my <= 480:
                    info_microwave(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 116 and mx <= 200 and my >= 510 and my <= 610:
                    info_oven(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 283 and mx <= 380 and my >= 510 and my <= 600:
                    info_toaster(screen, worker)
                    screen.blit(recycling_factory, (0, 0))


        pygame.display.update()


def moreProductsDown_recyclingFactory(screen, worker):

    while True:
        font3 = pygame.font.SysFont('arialblack', 12)

        tableOfContents_recyclingFactory(screen)
        screen.blit(worker, (700, 0))

        z = 250
        for i in range(0, 3):
            y = 80
            for j in range(0, 3):
                white_square = BUTTON.button((255, 255, 255), y, z, 175, 130, ' ')
                drawButton.drawButton(screen, white_square, 13, (0, 0, 0))
                y += 175
            z += 130

        screen.blit(glass_bottle, (120, 247))
        blitText.blit_text(screen, "      BOTTLE \n20 GLASS WASTE", (110, 345), font3, (0, 0, 0))

        screen.blit(fiber_glass, (290, 250))
        blitText.blit_text(screen, "   FIBER GLASS\n20 GLASS WASTE", (280, 345), font3, (0, 0, 0))

        screen.blit(glass_bricks, (470, 250))
        blitText.blit_text(screen, "  GLASS BRICKS\n20 GLASS WASTE", (460, 345), font3, (0, 0, 0))

        screen.blit(bench, (120, 380))
        blitText.blit_text(screen, "       BENCH\n60 METAL WASTE", (100, 474), font3, (0, 0, 0))

        screen.blit(chair, (295, 380))
        blitText.blit_text(screen, "       CHAIR\n40 METAL WASTE", (285, 474), font3, (0, 0, 0))

        screen.blit(coffemaker, (480, 380))
        blitText.blit_text(screen, " COFFEE MAKER\n50 METAL WASTE", (460, 474), font3, (0, 0, 0))

        screen.blit(plane, (100, 525))
        blitText.blit_text(screen, "       PLANE\n300 METAL WASTE", (100, 605), font3, (0, 0, 0))

        screen.blit(car, (280, 510))
        blitText.blit_text(screen, "          CAR\n200 METAL WASTE", (275, 605), font3, (0, 0, 0))

        screen.blit(lamp, (465, 510))
        blitText.blit_text(screen, "         LAMP\n 20 METAL WASTE", (450, 605), font3, (0, 0, 0))


        screen.blit(arrow_up, (320, 220))
        screen.blit(arrow_right, (610, 433))

        mx, my  = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if mx >= 315 and mx <= 340 and my >= 220 and my <= 240:
                running = True
                return running
            if mx >= 605 and mx <= 625 and my >= 433 and my <= 463:
                running = True
                running = moreProductsRight1_recyclingFactory(screen, worker)
                if running == False:
                    return running
            if event.type == pygame.QUIT:
                running = False
                return running
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mx >= 120 and mx <= 190 and my >= 247 and my <= 350:
                    info_glassBottle(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 290 and mx <= 405 and my >= 250 and my <= 350:
                    info_fiberGlass(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 470 and mx <= 570 and my >= 250 and my <= 350:
                    info_glassBricks(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 120 and mx <= 220 and my >= 380 and my <= 480:
                    info_metalBench(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 295 and mx <= 370 and my >= 380 and my <= 480:
                    info_metalChair(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 480 and mx <= 550 and my >= 380 and my <= 480:
                    info_metalCoffeemaker(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 280 and mx <= 390 and my >= 510 and my <= 577:
                    info_car(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 100 and mx <= 200 and my >= 525 and my <= 580:
                    info_plane(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if mx >= 465 and mx <= 565 and my >= 510 and my <= 605:
                    info_metalLamp(screen, worker)
                    screen.blit(recycling_factory, (0, 0))


        pygame.display.update()


def visit_recycling_factory(screen):
    #MAIN WINDOW FOR THE PRODUCTS

    font3 = pygame.font.SysFont('arialblack', 12)

    running = True
    x = 1000
    while running:
        recycling_factory_music.play(-1)
        screen.blit(recycling_factory, (0, 0))

        if(x > 700):
            x -= 3
        else:
            tableOfContents_recyclingFactory(screen)

            z = 250
            const = 2

            for i in range(0, 3):
                y = 80
                if i == 1:
                    const += 1
                for j in range(0, const):
                    white_square = BUTTON.button((255, 255, 255), y, z, 175, 130, ' ')
                    drawButton.drawButton(screen, white_square, 13, (0, 0, 0))
                    y += 175
                z += 130

            screen.blit(bio_fuel, (130, 255))
            blitText.blit_text(screen, "        BIOFUEL\n300 ORGANIC WASTE", (92, 344), font3, (0, 0, 0))

            screen.blit(compost, (300, 247))
            blitText.blit_text(screen, "       COMPOST\n50 ORGANIC WASTE", (270, 344), font3, (0, 0, 0))

            screen.blit(plastic_utensils, (100, 370))
            blitText.blit_text(screen, "REUSABLE UTENSILS\n 50 PLASTIC WASTE", (95, 475), font3, (0, 0, 0))

            screen.blit(schoolbag, (290, 370))
            blitText.blit_text(screen, "      SCHOOLBAG\n 70 PLASTIC WASTE", (275, 475), font3, (0, 0, 0))

            screen.blit(bottle, (485, 380))
            blitText.blit_text(screen, "REUSABLE BOTTLE\n10 PLASTIC WASTE", (450, 475), font3, (0, 0, 0))

            screen.blit(recycled_paper, (125, 520))
            blitText.blit_text(screen, "       PAPER STOCK\n     50 PAPER WASTE", (85, 607), font3, (0, 0, 0))

            screen.blit(notebook, (280, 510))
            blitText.blit_text(screen, "PAPER COVER NOTEBOOK\n     30 PAPER WASTE", (254, 607), font3, (0, 0, 0))

            screen.blit(napkin, (445, 510))
            blitText.blit_text(screen, "        PAPER NAPKIN\n      10 PAPER WASTE", (430, 607), font3, (0, 0, 0))

            screen.blit(arrow_right, (610, 422))
            screen.blit(arrow_down, (320, 645))

            mx, my = pygame.mouse.get_pos()
            if mx >= 600 and mx <= 640 and my >= 422 and my <= 440:
                running = moreProductsRight_recyclingFactory(screen, worker)
            if mx >= 315 and mx <= 345 and my >= 640 and my <= 670:
                running = moreProductsDown_recyclingFactory(screen, worker)

        screen.blit(worker, (x, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mx >= 130 and mx <= 200 and my >= 255 and my <= 350:
                    info_bioFuel(screen, worker)
                if mx >= 300 and mx <= 360 and my >= 247 and my <= 350:
                    info_compost(screen, worker)
                if mx >= 100 and mx <= 230 and my >= 370 and my <= 470:
                    info_bioUtensils(screen, worker)
                if mx >= 290 and mx <= 385 and my >= 370 and my <= 470:
                    info_plasticBackpack(screen, worker)
                if mx >= 485 and mx <= 535 and my >= 380 and my <= 480:
                    info_plasticBottle(screen, worker)
                if mx >= 125 and mx <= 210 and my >= 520 and my <= 610:
                    info_paperStock(screen, worker)
                if mx >= 280 and mx <= 390 and my >= 510 and my <= 600:
                    info_notebook(screen, worker)
                if mx >= 445 and mx <= 575 and my >= 510 and my <= 600:
                    info_napkins(screen, worker)

        pygame.display.update()

    recycling_factory_music.stop()
    town_music.play(-1)

def townBackgrounds_Buttons(screen, recycling_area, supermarket, water_plant, recycling_plant,
                           business_center, touristic_area, eco_events, x):
    screen.blit(townhall, (910, 1))
    screen.blit(town_view, (0, 0))

    # buttons
    drawButton.drawButton(screen, recycling_area, 13, (0, 0, 0))
    drawButton.drawButton(screen, supermarket, 13, (0, 0, 0))
    drawButton.drawButton(screen, water_plant, 13, (0, 0, 0))
    drawButton.drawButton(screen, recycling_plant, 13, (0, 0, 0))
    drawButton.drawButton(screen, business_center, 13, (0, 0, 0))
    drawButton.drawButton(screen, touristic_area, 13, (0, 0, 0))
    drawButton.drawButton(screen, eco_events, 13, (0, 0, 0))

    screen.blit(mayor_normal_pose, (x, 39))

def townView(screen):
    #town background music
    town_music.play(-1)

    #background
    screen = pygame.display.set_mode((1300, 700))

    #texts
    intro_text = "Hello! Welcome to our eco city\ndestined to change the future: \nGREEN LANDIA!\nI am the mayor, Margaret Green." \
                 "\nClick on a button of an area to\ndiscover more or the 'escape' button" \
                 "\non your keyboard to leave the town!"

    #fonts
    font_intro_text = pygame.font.SysFont('arial', 15)
    font_text_before_after_mayor = pygame.font.SysFont('javanesetext', 20)

    #"image" buttons description box town view
    mayor_text_button = BUTTON.button((255, 255, 255), 950, 50, 210, 150, ' ')
    visit_button = BUTTON.button((150, 240, 0), 1030, 600, 120, 50, 'VISIT AREA')

    # "image" buttons town view
    recycling_area = BUTTON.button((255, 255, 0), 500, 650, 90, 30, 'Recycling area')
    supermarket = BUTTON.button((255, 255, 0), 360, 50, 80, 30, 'Supermarket')
    water_plant = BUTTON.button((255, 255, 0), 500, 50, 150, 30, 'Water purification center')
    recycling_plant = BUTTON.button((255, 255, 0), 740, 10, 100, 30, 'Recycling factory')
    business_center = BUTTON.button((255, 255, 0), 100, 350, 100, 30, 'Business center')
    touristic_area = BUTTON.button((255, 255, 0), 700, 450, 100, 30, 'Touristic area')
    eco_events = BUTTON.button((255, 255, 0), 400, 450, 100, 30, 'Eco-events area')


    running = True

    x = 1000
    clickedButton = 0
    while running:

        pos = pygame.mouse.get_pos()  # mouse coordinates
        #backgrounds screening
        townBackgrounds_Buttons(screen, recycling_area, supermarket, water_plant, recycling_plant,
                               business_center, touristic_area, eco_events, x)
        #mayor movement + texts
        text = " "

        if clickedButton == 0:
            if x > 900:
                x -= 2
                text = font_text_before_after_mayor.render("THE MAYOR IS COMING...", True, (255, 255, 255))
                screen.blit(text, (950, 480))
            else:
                # text boxes
                drawButton.drawButton(screen, mayor_text_button, 13, (0, 0, 0)) # the message of the mayor
                blitText.blit_text(screen, intro_text, (952, 50), font_intro_text)

                #cover the old text
                text = font_text_before_after_mayor.render("THE MAYOR IS COMING...", True, (0, 0, 0))
                screen.blit(text, (950, 480))

                #make new text appear in description box
                text = font_text_before_after_mayor.render("THE MAYOR IS SPEAKING NOW...", True, (255, 255, 255))
                screen.blit(text, (915, 480))
        elif clickedButton == 1:
                screen.fill((0, 0, 0))
                townBackgrounds_Buttons(screen, recycling_area, supermarket, water_plant, recycling_plant,
                               business_center, touristic_area, eco_events, x)
                drawButton.drawButton(screen, visit_button, 13, (0, 0, 0))

                #mayor message
                mayor_text_button = BUTTON.button((255, 255, 255), 930, 50, 230, 100, ' ')
                drawButton.drawButton(screen, mayor_text_button, 13, (0, 0, 0))
                mayor_text = "Welcome to the RECYCLING AREA!\nClick on the 'escape' button on your\nkeyboard if you " \
                             "want to leave the town\nor press on another area button!"
                blitText.blit_text(screen, mayor_text, (933, 50), font_intro_text)

                #description box text
                font = pygame.font.SysFont('arial', 15)
                description_text = "THE RECYCLING AREA is the place where you, as a citizen, can sort" \
                                   " your garbage. Paper to paper. Glass to glass. Plastic to plastic. And so on." \
                                   "\n\nIn order to keep the planet alive and help our future generations thrive, " \
                                   "we have to act responsibly.\n\nStep by step, every day, we encourage our citizens" \
                                   " to care and sort their garbage at least. Let me present you the recycling area fully!" \
                                   " Click on 'visit area' and let's go !!!"
                blitText.blit_text(screen, description_text, (915, 370), font, (255, 255, 255))


                if event.type == pygame.MOUSEMOTION:
                    if visit_button.isOver(pos):
                        visit_button.color = (0, 160, 0)
                    else:
                        visit_button.color = (150, 240, 0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if visit_button.isOver(pos):
                        town_music.stop()
                        visitRecyclingArea.visit_recycling_area(screen)


        elif clickedButton == 2:
            screen.fill((0, 0, 0))
            townBackgrounds_Buttons(screen, recycling_area, supermarket, water_plant, recycling_plant,
                                    business_center, touristic_area, eco_events, x)
            drawButton.drawButton(screen, visit_button, 13, (0, 0, 0))

            # mayor message
            mayor_text_button = BUTTON.button((255, 255, 255), 930, 50, 230, 100, ' ')
            drawButton.drawButton(screen, mayor_text_button, 13, (0, 0, 0))
            mayor_text = "Welcome to the SUPERMARKET!\nClick on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            blitText.blit_text(screen, mayor_text, (933, 50), font_intro_text)

            # description box text
            font = pygame.font.SysFont('arial', 15)
            description_text = "Our Supermarkets are completely eco. We have a whole healthy industry" \
                               " and provide our citizens with the best quality food. \n\nHow was it in the prehistorical" \
                               " era? Everyone could live without chocolate, chips and other poisoning foods... " \
                               "And even though humans could not get their food easily, they would at least" \
                               " eat healthy. We want to bring this back." \
                               "\n\nClick on 'visit area' and let's see how our business is going here!"
            blitText.blit_text(screen, description_text, (915, 370), font, (255, 255, 255))

            if event.type == pygame.MOUSEMOTION:
                if visit_button.isOver(pos):
                    visit_button.color = (0, 160, 0)
                else:
                    visit_button.color = (150, 240, 0)

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if visit_button.isOver(pos):
            #         town_music.stop()
            #         visit_supermarket(screen)

        elif clickedButton == 3:
            screen.fill((0, 0, 0))
            townBackgrounds_Buttons(screen, recycling_area, supermarket, water_plant, recycling_plant,
                                    business_center, touristic_area, eco_events, x)
            drawButton.drawButton(screen, visit_button, 13, (0, 0, 0))

            # mayor message
            mayor_text_button = BUTTON.button((255, 255, 255), 930, 50, 230, 100, ' ')
            drawButton.drawButton(screen, mayor_text_button, 13, (0, 0, 0))
            mayor_text = "Welcome to the\nWATER PURIFICATION CENTER!\nClick on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            blitText.blit_text(screen, mayor_text, (933, 50), font_intro_text)

            # description box text
            font = pygame.font.SysFont('arial', 15)
            description_text = "Curious what our water purification center does?\n" \
                               "Well, water purification is the process of removing undesirable chemicals, " \
                               "biological contaminants, suspended solids, and gases from water. The goal is to produce " \
                               "water fit for specific purposes. Most water is purified and disinfected for human" \
                               " consumption (drinking water), but water purification may also be carried out for a" \
                               " variety of other purposes, including medical, pharmacological, chemical, " \
                               "and industrial applications.\nI know, dear, it sounds complicated but with this we make " \
                               "your life better and we think that you should know. " \
                               "\nIf you want to experiment with the process, let's visit the area!"
            blitText.blit_text(screen, description_text, (915, 370), font, (255, 255, 255))

            if event.type == pygame.MOUSEMOTION:
                if visit_button.isOver(pos):
                    visit_button.color = (0, 160, 0)
                else:
                    visit_button.color = (150, 240, 0)

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if visit_button.isOver(pos):
            #         town_music.stop()
            #         visit_water_plant(screen)

        elif clickedButton == 4:
            screen.fill((0, 0, 0))
            townBackgrounds_Buttons(screen, recycling_area, supermarket, water_plant, recycling_plant,
                                    business_center, touristic_area, eco_events, x)
            drawButton.drawButton(screen, visit_button, 13, (0, 0, 0))

            # mayor message
            mayor_text_button = BUTTON.button((255, 255, 255), 930, 50, 230, 100, ' ')
            drawButton.drawButton(screen, mayor_text_button, 13, (0, 0, 0))
            mayor_text = "Welcome to the RECYCLING FACTORY!\nClick on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            blitText.blit_text(screen, mayor_text, (933, 50), font_intro_text)

            # description box text
            font = pygame.font.SysFont('arial', 15)
            description_text = "The RECYCLING FACTORY is the place where the sorted garbage arrives, from the recycling area." \
                               "\n\nAt this facility, items are sorted, compressed, baled, stored, and then shipped out to be " \
                               "made into new products.\n\n Easy said, but believe me: it is a hard thing" \
                               " to do. If you want to see how the business goes here, let's visit the factory! "
            blitText.blit_text(screen, description_text, (915, 370), font, (255, 255, 255))

            if event.type == pygame.MOUSEMOTION:
                if visit_button.isOver(pos):
                    visit_button.color = (0, 160, 0)
                else:
                    visit_button.color = (150, 240, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if visit_button.isOver(pos):
                    town_music.stop()
                    visit_recycling_factory(screen)

        elif clickedButton == 5:
            screen.fill((0, 0, 0))
            townBackgrounds_Buttons(screen, recycling_area, supermarket, water_plant, recycling_plant,
                                    business_center, touristic_area, eco_events, x)
            drawButton.drawButton(screen, visit_button, 13, (0, 0, 0))

            # mayor message
            mayor_text_button = BUTTON.button((255, 255, 255), 930, 50, 230, 100, ' ')
            drawButton.drawButton(screen, mayor_text_button, 13, (0, 0, 0))
            mayor_text = "Welcome to the BUSINESS CENTER!\nClick on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            blitText.blit_text(screen, mayor_text, (933, 50), font_intro_text)

            # description box text
            font = pygame.font.SysFont('arial', 15)
            description_text = "This is the heart of Green Landia. It is the place that conducts all the business, " \
                               "ranging from tourism, to the recycling actions. " \
                               "\n Here we establish the rules for the city and plans for the future, we create" \
                               " associations of people with different purposes and encourage the youth to participate." \
                               "\n\nLet's see how things go in here because I am indeed curious myself!"
            blitText.blit_text(screen, description_text, (915, 370), font, (255, 255, 255))

            if event.type == pygame.MOUSEMOTION:
                if visit_button.isOver(pos):
                    visit_button.color = (0, 160, 0)
                else:
                    visit_button.color = (150, 240, 0)

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if visit_button.isOver(pos):
            #         town_music.stop()
            #         visit_business_area(screen)

        elif clickedButton == 6:
            screen.fill((0, 0, 0))
            townBackgrounds_Buttons(screen, recycling_area, supermarket, water_plant, recycling_plant,
                                    business_center, touristic_area, eco_events, x)
            drawButton.drawButton(screen, visit_button, 13, (0, 0, 0))

            # mayor message
            mayor_text_button = BUTTON.button((255, 255, 255), 930, 50, 230, 100, ' ')
            drawButton.drawButton(screen, mayor_text_button, 13, (0, 0, 0))
            mayor_text = "Welcome to the TOURISTIC AREA!\nClick on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            blitText.blit_text(screen, mayor_text, (933, 50), font_intro_text)

            # description box text
            font = pygame.font.SysFont('arial', 15)
            description_text = "This is one of our touristic areas. As you can see,it is a camping site, but we have so much more." \
                               "\n\nActually, we tend to focus more on getting people outside in the nature and appreciate " \
                               "its role in our lives. We have been born in nature and we evolved in nature. Not in a " \
                               "hospital. Not in our workplace. But among the trees and animals.\n\nLet's play some games " \
                               "in here, dear citizen!"
            blitText.blit_text(screen, description_text, (915, 370), font, (255, 255, 255))

            if event.type == pygame.MOUSEMOTION:
                if visit_button.isOver(pos):
                    visit_button.color = (0, 160, 0)
                else:
                    visit_button.color = (150, 240, 0)

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if visit_button.isOver(pos):
            #         town_music.stop()
            #         visit_touristic_area(screen)

        else:
            screen.fill((0, 0, 0))
            townBackgrounds_Buttons(screen, recycling_area, supermarket, water_plant, recycling_plant,
                                    business_center, touristic_area, eco_events, x)
            drawButton.drawButton(screen, visit_button, 13, (0, 0, 0))

            # mayor message
            mayor_text_button = BUTTON.button((255, 255, 255), 930, 50, 230, 100, ' ')
            drawButton.drawButton(screen, mayor_text_button, 13, (0, 0, 0))
            mayor_text = "Welcome to the EVENTS AREA!\nClick on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            blitText.blit_text(screen, mayor_text, (933, 50), font_intro_text)

            # description box text
            font = pygame.font.SysFont('arial', 15)
            description_text = "Would you guess what happens here?\n" \
                               "With the help of our citizens from the business center, we organize weekly events." \
                               "It is quite fun: concerts, painting contests, sports, meditation sessions and whatnot." \
                               "But all with the purpose of developing our citizens into better human beings. And..." \
                               "perhaps for a bit of fun too!\n\n" \
                               "Here is a rule, though: after you will have established a plan for an event in the " \
                               "business center, come here and make it happen! We are eager to see what is on your " \
                               "entrepreneur mind.\n" \
                               "Shall we see what is happening here now? "
            blitText.blit_text(screen, description_text, (915, 370), font, (255, 255, 255))

            if event.type == pygame.MOUSEMOTION:
                if visit_button.isOver(pos):
                    visit_button.color = (0, 160, 0)
                else:
                    visit_button.color = (150, 240, 0)

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if visit_button.isOver(pos):
            #         town_music.stop()
            #         visit_event_area(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if recycling_area.isOver(pos):
                    clickedButton = 1
                if supermarket.isOver(pos):
                    clickedButton = 2
                if water_plant.isOver(pos):
                    clickedButton = 3
                if recycling_plant.isOver(pos):
                    clickedButton = 4
                if business_center.isOver(pos):
                    clickedButton = 5
                if touristic_area.isOver(pos):
                    clickedButton = 6
                if eco_events.isOver(pos):
                    clickedButton = 7
            if event.type == pygame.MOUSEMOTION:
                if recycling_area.isOver(pos):
                    recycling_area.color = (0, 160, 0)
                else:
                    recycling_area.color = (255, 255, 0)
                if supermarket.isOver(pos):
                    supermarket.color = (0, 160, 0)
                else:
                    supermarket.color = (255, 255, 0)
                if water_plant.isOver(pos):
                    water_plant.color = (0, 160, 0)
                else:
                    water_plant.color = (255, 255, 0)
                if business_center.isOver(pos):
                    business_center.color = (0, 160, 0)
                else:
                    business_center.color = (255, 255, 0)
                if touristic_area.isOver(pos):
                    touristic_area.color = (0, 160, 0)
                else:
                    touristic_area.color = (255, 255, 0)
                if eco_events.isOver(pos):
                    eco_events.color = (0, 160, 0)
                else:
                    eco_events.color = (255, 255, 0)
                if recycling_plant.isOver(pos):
                    recycling_plant.color = (0, 160, 0)
                else:
                    recycling_plant.color = (255, 255, 0)

        pygame.display.update()

    town_music.stop()
