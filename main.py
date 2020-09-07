import pygame, BUTTON, random, time
from pygame import mixer

# Initialize the pygame
pygame.init()

#Backgrounds
backgroundMenu = pygame.image.load('images/menu_background.png')
town_view = pygame.image.load('images/town.png')
townhall = pygame.image.load('images/townhall.png')
recycling_area = pygame.image.load('images/recycling_area.jpg')
mayor_recycling_area_background = pygame.image.load('images/mayor_recycling_area_background.jpg')
recycling_factory = pygame.image.load('images/recycling_factory.jpg')

#Objects
arrow_right = pygame.image.load('arrow_right.png')
arrow_down = pygame.image.load('arrow_down.png')
arrow_up = pygame.image.load('arrow_up.png')
arrow_left = pygame.image.load('arrow_left.png')

bio_fuel = pygame.image.load('recycled items/organic/biofuel.png')
compost = pygame.image.load('recycled items/organic/fertilizer.png')

plastic_utensils = pygame.image.load('recycled items/plastic/plastic_utensils.png')
bio_bag = pygame.image.load('recycled items/plastic/bio_bag.png')
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
mayor_normal_poseBig = pygame.image.load('poses/mayor_normal_pose(big).png')
mayor_superhero_pose = pygame.image.load('poses/mayor_superhero_pose.png')
worker = pygame.image.load('poses/worker.png')

#soundtrack
menu_music = mixer.Sound('music/menu.wav')
town_music = mixer.Sound('music/town.wav')
recycling_area_music = mixer.Sound('music/recycling_area.wav')
recycling_factory_music = mixer.Sound('music/recycling_factory.wav')

# Title and Icon
pygame.display.set_caption("Green Landia")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

#Others
menuButton = BUTTON.button((255, 255, 255), 300, 180, 300, 70, 'START GAME')
scorePlastic, scoreOrganic, scoreMetal, scorePaper, scoreGlass = 0, 0, 0, 0, 0

#FUNCTIONS-----------------------------------------------------------------------------
def drawButton(screen, BUTTON, size, outline):
    BUTTON.draw(screen, size, outline)

def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def play_game_recycling_area(screen, text_button, score, mistakes, result):
    font1 = pygame.font.SysFont('arial', 40)

    text3 = " Drag the object to the right recycle bin\n            and click on the bin!"
    font2 = pygame.font.SysFont('arial', 20)

    drawButton(screen, text_button, 13, (0, 0, 0))  # mayor textbox

    #print score
    score = font1.render("SCORE: " + str(score), True, (0, 255, 0))
    screen.blit(score, (803, 50))

    #print mistakes
    score = font1.render("MISTAKES: " + str(mistakes), True, (255, 0, 0))
    screen.blit(score, (803, 100))

    #print instructions
    blit_text(screen, text3, (803, 170), font2)

    if result == 'Correct':
         blit_text(screen, 'Correct!', (890, 250), font1, (0, 255, 0))
    elif result == 'Wrong':
         blit_text(screen, 'Wrong!', (890, 250), font1, (255, 0, 0))

def visit_recycling_area(screen):

    screen = pygame.display.set_mode((1200, 550))

    # texts
    text = "Let's test your knowledge in recycling!\n1.Pick up the garbage that appears on the grass." \
           "\n2.Put it in the right recycle bin.\n\nIf you're right, your number of recycled materials will\nincrease" \
           " and these materials will be used at the\nrecycling factory so you have to visit that afterwards." \
           "\n\nIf you don't recycle correctly, you will lose the material.\nTHE GAME ENDS AFTER 3 MISTAKES.\nGood luck!"

    # fonts
    font = pygame.font.SysFont('arial', 15)

    # "image" buttons description box town view
    text_button = BUTTON.button((255, 255, 255), 800, 50, 300, 300, ' ')
    play_button = BUTTON.button((150, 240, 0), 900, 300, 100, 35, 'PLAY')

    score, mistakes, oldmx, oldmy, x = 0, 0, 0, 0, 1000
    play, running = False, True
    while running:
        recycling_area_music.play(-1)
        screen.blit(mayor_recycling_area_background, (790,0))
        screen.blit(recycling_area, (0, 0))

        # for mayor movement
        if (x > 700):
            x -= 2
        else:

            if play == False:
                pos = pygame.mouse.get_pos()
                drawButton(screen, text_button, 13, (0, 0, 0))  # the message of the mayor
                drawButton(screen, play_button, 35, (0, 0, 0))
                blit_text(screen, text, (803, 50), font)

                if event.type == pygame.MOUSEMOTION:
                    if play_button.isOver(pos):
                        play_button.color = (0, 160, 0)
                    else:
                        play_button.color = (150, 240, 0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.isOver(pos):
                        play = True
                        mistakes = 0

            elif play == True: # if the player pressed play button already

                 #select a random trash item from folder "trash"
                i = random.randint(1, 72)
                trashImg = pygame.image.load("trash/trash" + str(i) + ".png")

                correct = True  #correct = true, if recycled properly, correct = false, otherwise
                while correct == True:

                    if mistakes < 3:
                        mx, my = pygame.mouse.get_pos()

                        #the pixel zone for each trash bin
                        if i <= 10:
                            material = 'glass'
                        elif i >= 11 and i <= 21:
                            material = 'metal'
                        elif i >= 22 and i <= 40:
                            material = 'organic'
                        elif i >= 41 and i <= 58:
                            material = 'paper'
                        else:
                            material = 'plastic'

                        result = 'None'
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                correct = -2 #interrupt the game
                                running = False #also return to the town view

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if my >= 40 and my <= 210:
                                    if mx >= 35 and mx <= 130:
                                        if material == 'metal':
                                            score += 1
                                            global scoreMetal
                                            scoreMetal += 1
                                            result = 'Correct'

                                            # recycle another piece of trash
                                            i = random.randint(1, 72)
                                            trashImg = pygame.image.load("trash/trash" + str(i) + ".png")

                                        else:
                                             mistakes += 1
                                             result = 'Wrong'
                                    else:
                                        if mx >= 180 and mx <= 270:
                                            if material == 'organic':
                                                score += 1
                                                global scoreOrganic
                                                scoreOrganic += 1
                                                result = 'Correct'

                                                # recycle another piece of trash
                                                i = random.randint(1, 72)
                                                trashImg = pygame.image.load("trash/trash" + str(i) + ".png")

                                            else:
                                                mistakes += 1
                                                result = 'Wrong'
                                        else:
                                            if mx >= 340 and mx <= 415:
                                                if material == 'paper':
                                                    score += 1
                                                    global scorePaper
                                                    scorePaper += 1
                                                    result = 'Correct'

                                                    # recycle another piece of trash
                                                    i = random.randint(1, 72)
                                                    trashImg = pygame.image.load("trash/trash" + str(i) + ".png")

                                                else:
                                                    mistakes += 1
                                                    result = 'Wrong'
                                            else:
                                                if mx >= 485 and mx <= 580:
                                                    if material == 'plastic':
                                                        score += 1
                                                        global scorePlastic
                                                        scorePlastic += 1
                                                        result = 'Correct'

                                                        # recycle another piece of trash
                                                        i = random.randint(1, 72)
                                                        trashImg = pygame.image.load("trash/trash" + str(i) + ".png")

                                                    else:
                                                        mistakes += 1
                                                        result = 'Wrong'
                                                else:
                                                    if mx >= 640 and mx <= 720:
                                                        if material == 'glass':
                                                            score += 1
                                                            global scoreGlass
                                                            scoreGlass += 1
                                                            result = 'Correct'

                                                            #recycle another piece of trash
                                                            i = random.randint(1, 72)
                                                            trashImg = pygame.image.load("trash/trash" + str(i) + ".png")

                                                        else:
                                                            mistakes += 1
                                                            result = 'Wrong'

                        #rebuilding background
                        screen.fill((0, 0, 0))
                        screen.blit(mayor_recycling_area_background, (790, 0))
                        screen.blit(recycling_area, (0, 0))
                        screen.blit(mayor_normal_poseBig, (x, 60))
                        play_game_recycling_area(screen, text_button, score, mistakes, result)  # printing on screen the text box with the score -->mayor textbox

                        #so the object would not exit the collecting screen and go where the mayor is
                        if mx >= 0 and mx <= 730:
                            screen.blit(trashImg, (mx - 60, my - 60))
                            oldmx = mx
                            oldmy = my
                        else:
                            screen.blit(trashImg, (oldmx, oldmy))
                        pygame.display.flip()

                    else:
                        # the end of the game--->mistakes = 3

                        text = 'Congratulations! You recycled '+str(score)+' objects!\n\nClose the window' \
                            ' if you want to leave\nthe area or play again!'
                        font = pygame.font.SysFont('arial', 20)
                        text_button = BUTTON.button((255, 255, 255), 800, 50, 312, 260, ' ')
                        play_button = BUTTON.button((150, 240, 0), 900, 200, 100, 35, 'PLAY')

                        score = 0
                        correct = False
                        play = False
        #end of checking if play button is pressed or not

        #displaying mayor on the screen
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
    town_music.play(-1)
    screen = pygame.display.set_mode((1300, 700))


def tableOfContents_recyclingFactory(screen):
    text = "   Hello! I am Paul, the chef worker here.\n   In the box to the left, you have the " \
           " amount of\nrecycled materials of each kind so far and how much\nmaterial we need to recreate something else." \
           "\n   We will create new products and put them\non the market." \
           " You choose which products\nwe can recreate by clicking on them." \
           "\n\n  CONSUME, RECYCLE, REUSE."
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

    drawButton(screen, text_button, 13, (0, 0, 0))  # the message of the worker
    blit_text(screen, text, (802, 50), font)
    drawButton(screen, table, 13, (0, 0, 0))

    drawButton(screen, glass_square, 13, (0, 0, 0))
    drawButton(screen, metal_square, 13, (0, 0, 0))
    drawButton(screen, organic_square, 13, (0, 0, 0))
    drawButton(screen, paper_square, 13, (0, 0, 0))
    drawButton(screen, plastic_square, 13, (0, 0, 0))

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

    blit_text(screen, "BUILD ITEMS", (223, 180), font2, (255, 255, 255))

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
            if i == 1:
                const += 1
            for j in range(0, const):
                white_square = BUTTON.button((255, 255, 255), y, z, 175, 130, ' ')
                drawButton(screen, white_square, 13, (0, 0, 0))
                y += 175
            z += 130

        screen.blit(bio_fuel, (130, 255))
        blit_text(screen, "        BIOFUEL\n300 ORGANIC WASTE", (92, 344), font3, (0, 0, 0))

        screen.blit(compost, (300, 247))
        blit_text(screen, "       COMPOST\n50 ORGANIC WASTE", (270, 344), font3, (0, 0, 0))

        screen.blit(cap, (100, 370))
        blit_text(screen, "         CAP\n30 PLASTIC WASTE", (100, 475), font3, (0, 0, 0))

        screen.blit(shoe, (280, 370))
        blit_text(screen, "         SHOE\n50 PLASTIC WASTE", (275, 475), font3, (0, 0, 0))

        screen.blit(schoolbag, (465, 375))
        blit_text(screen, "      SCHOOLBAG\n 70 PLASTIC WASTE", (447, 475), font3, (0, 0, 0))

        screen.blit(pencils, (120, 495))
        blit_text(screen, "RECYCLED PAPER PENCIL\n     30 PAPER WASTE", (80, 607), font3, (0, 0, 0))

        screen.blit(book, (280, 510))
        blit_text(screen, "        BOOK\n80 PAPER WASTE", (280, 607), font3, (0, 0, 0))

        screen.blit(paper_cups, (470, 510))
        blit_text(screen, "   PAPER CUPS\n20 PAPER WASTE", (460, 607), font3, (0, 0, 0))

        mx, my  = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if mx >= 40 and mx <= 70 and my >= 420 and my <= 450:
                running = True
                return running
            if event.type == pygame.QUIT:
                running = False
                return running

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
                drawButton(screen, white_square, 13, (0, 0, 0))
                y += 175
            z += 130

        screen.blit(glassphalt, (123, 250))
        blit_text(screen, "    GLASSPHALT\n50 GLASS WASTE", (107, 345), font3, (0, 0, 0))

        screen.blit(reflective_paint, (293, 250))
        blit_text(screen, "REFLECTIVE PAINT\n 20 GLASS WASTE", (280, 345), font3, (0, 0, 0))

        screen.blit(tiles, (467, 250))
        blit_text(screen, "        TILES\n50 GLASS WASTE", (460, 345), font3, (0, 0, 0))

        screen.blit(fridge, (120, 380))
        blit_text(screen, "      FRIDGE\n90 METAL WASTE", (110, 474), font3, (0, 0, 0))

        screen.blit(metal_utensils, (277, 380))
        blit_text(screen, "METAL UTENSILS\n20 METAL WASTE", (280, 474), font3, (0, 0, 0))

        screen.blit(microwave, (465, 380))
        blit_text(screen, "    MICROWAVE\n70 METAL WASTE", (460, 474), font3, (0, 0, 0))

        screen.blit(oven, (116, 510))
        blit_text(screen, "        OVEN\n90 METAL WASTE", (105, 605), font3, (0, 0, 0))

        screen.blit(toaster, (283, 510))
        blit_text(screen, "      TOASTER\n40 METAL WASTE", (280, 605), font3, (0, 0, 0))

        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if mx >= 40 and mx <= 70 and my >= 420 and my <= 450:
                running = True
                return running
            if event.type == pygame.QUIT:
                running = False
                return running

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
                drawButton(screen, white_square, 13, (0, 0, 0))
                y += 175
            z += 130

        screen.blit(glass_bottle, (120, 247))
        blit_text(screen, "      BOTTLE \n20 GLASS WASTE", (110, 345), font3, (0, 0, 0))

        screen.blit(fiber_glass, (290, 250))
        blit_text(screen, "   FIBER GLASS\n20 GLASS WASTE", (280, 345), font3, (0, 0, 0))

        screen.blit(glass_bricks, (470, 250))
        blit_text(screen, "  GLASS BRICKS\n20 GLASS WASTE", (460, 345), font3, (0, 0, 0))

        screen.blit(bench, (120, 380))
        blit_text(screen, "       BENCH\n60 METAL WASTE", (100, 474), font3, (0, 0, 0))

        screen.blit(chair, (295, 380))
        blit_text(screen, "       CHAIR\n40 METAL WASTE", (285, 474), font3, (0, 0, 0))

        screen.blit(coffemaker, (480, 380))
        blit_text(screen, " COFFEE MAKER\n50 METAL WASTE", (460, 474), font3, (0, 0, 0))

        screen.blit(plane, (100, 525))
        blit_text(screen, "       PLANE\n300 METAL WASTE", (100, 605), font3, (0, 0, 0))

        screen.blit(car, (280, 510))
        blit_text(screen, "          CAR\n200 METAL WASTE", (275, 605), font3, (0, 0, 0))

        screen.blit(lamp, (465, 510))
        blit_text(screen, "         LAMP\n 20 METAL WASTE", (450, 605), font3, (0, 0, 0))


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

        pygame.display.update()


def visit_recycling_factory(screen):
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
                    drawButton(screen, white_square, 13, (0, 0, 0))
                    y += 175
                z += 130

            screen.blit(bio_fuel, (130, 255))
            blit_text(screen, "        BIOFUEL\n300 ORGANIC WASTE", (92, 344), font3, (0, 0, 0))

            screen.blit(compost, (300, 247))
            blit_text(screen, "       COMPOST\n50 ORGANIC WASTE", (270, 344), font3, (0, 0, 0))

            screen.blit(plastic_utensils, (100, 370))
            blit_text(screen, "    BIO UTENSILS\n50 PLASTIC WASTE", (100, 475), font3, (0, 0, 0))

            screen.blit(bio_bag, (280, 370))
            blit_text(screen, "       BIO BAG\n20 PLASTIC WASTE", (275, 475), font3, (0, 0, 0))

            screen.blit(bottle, (485, 380))
            blit_text(screen, "BIO PLASTIC BOTTLE\n 10 PLASTIC WASTE", (447, 475), font3, (0, 0, 0))

            screen.blit(recycled_paper, (125, 520))
            blit_text(screen, "       PAPER STOCK\n     50 PAPER WASTE", (85, 607), font3, (0, 0, 0))

            screen.blit(notebook, (280, 510))
            blit_text(screen, "PAPER COVER NOTEBOOK\n     30 PAPER WASTE", (254, 607), font3, (0, 0, 0))

            screen.blit(napkin, (445, 510))
            blit_text(screen, "        PAPER NAPKIN\n      10 PAPER WASTE", (430, 607), font3, (0, 0, 0))

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


        pygame.display.update()

    recycling_factory_music.stop()
    town_music.play(-1)

def townBackgrounds_Buttons(screen, recycling_area, supermarket, water_plant, recycling_plant,
                           business_center, touristic_area, eco_events, x):
    screen.blit(townhall, (910, 1))
    screen.blit(town_view, (0, 0))

    # buttons
    drawButton(screen, recycling_area, 13, (0, 0, 0))
    drawButton(screen, supermarket, 13, (0, 0, 0))
    drawButton(screen, water_plant, 13, (0, 0, 0))
    drawButton(screen, recycling_plant, 13, (0, 0, 0))
    drawButton(screen, business_center, 13, (0, 0, 0))
    drawButton(screen, touristic_area, 13, (0, 0, 0))
    drawButton(screen, eco_events, 13, (0, 0, 0))

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
                drawButton(screen, mayor_text_button, 13, (0, 0, 0)) # the message of the mayor
                blit_text(screen, intro_text, (952, 50), font_intro_text)

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
                drawButton(screen, visit_button, 13, (0, 0, 0))

                #mayor message
                mayor_text_button = BUTTON.button((255, 255, 255), 930, 50, 230, 100, ' ')
                drawButton(screen, mayor_text_button, 13, (0, 0, 0))
                mayor_text = "Welcome to the RECYCLING AREA!\nClick on the 'escape' button on your\nkeyboard if you " \
                             "want to leave the town\nor press on another area button!"
                blit_text(screen, mayor_text, (933, 50), font_intro_text)

                #description box text
                font = pygame.font.SysFont('arial', 15)
                description_text = "THE RECYCLING AREA is the place where you, as a citizen, can sort" \
                                   " your garbage. Paper to paper. Glass to glass. Plastic to plastic. And so on." \
                                   "\n\nIn order to keep the planet alive and help our future generations thrive, " \
                                   "we have to act responsibly.\n\nStep by step, every day, we encourage our citizens" \
                                   " to care and sort their garbage at least. Let me present you the recycling area fully!" \
                                   " Click on 'visit area' and let's go !!!"
                blit_text(screen, description_text, (915, 370), font, (255, 255, 255))


                if event.type == pygame.MOUSEMOTION:
                    if visit_button.isOver(pos):
                        visit_button.color = (0, 160, 0)
                    else:
                        visit_button.color = (150, 240, 0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if visit_button.isOver(pos):
                        town_music.stop()
                        visit_recycling_area(screen)


        elif clickedButton == 2:
            screen.fill((0, 0, 0))
            townBackgrounds_Buttons(screen, recycling_area, supermarket, water_plant, recycling_plant,
                                    business_center, touristic_area, eco_events, x)
            drawButton(screen, visit_button, 13, (0, 0, 0))

            # mayor message
            mayor_text_button = BUTTON.button((255, 255, 255), 930, 50, 230, 100, ' ')
            drawButton(screen, mayor_text_button, 13, (0, 0, 0))
            mayor_text = "Welcome to the SUPERMARKET!\nClick on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            blit_text(screen, mayor_text, (933, 50), font_intro_text)

            # description box text
            font = pygame.font.SysFont('arial', 15)
            description_text = "Our Supermarkets are completely eco. We have a whole healthy industry" \
                               " and provide our citizens with the best quality food. \n\nHow was it in the prehistorical" \
                               " era? Everyone could live without chocolate, chips and other poisoning foods... " \
                               "And even though humans could not get their food easily, they would at least" \
                               " eat healthy. We want to bring this back." \
                               "\n\nClick on 'visit area' and let's see how our business is going here!"
            blit_text(screen, description_text, (915, 370), font, (255, 255, 255))

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
            drawButton(screen, visit_button, 13, (0, 0, 0))

            # mayor message
            mayor_text_button = BUTTON.button((255, 255, 255), 930, 50, 230, 100, ' ')
            drawButton(screen, mayor_text_button, 13, (0, 0, 0))
            mayor_text = "Welcome to the\nWATER PURIFICATION CENTER!\nClick on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            blit_text(screen, mayor_text, (933, 50), font_intro_text)

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
            blit_text(screen, description_text, (915, 370), font, (255, 255, 255))

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
            drawButton(screen, visit_button, 13, (0, 0, 0))

            # mayor message
            mayor_text_button = BUTTON.button((255, 255, 255), 930, 50, 230, 100, ' ')
            drawButton(screen, mayor_text_button, 13, (0, 0, 0))
            mayor_text = "Welcome to the RECYCLING FACTORY!\nClick on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            blit_text(screen, mayor_text, (933, 50), font_intro_text)

            # description box text
            font = pygame.font.SysFont('arial', 15)
            description_text = "The RECYCLING FACTORY is the place where the sorted garbage arrives, from the recycling area." \
                               "\n\nAt this facility, items are sorted, compressed, baled, stored, and then shipped out to be " \
                               "made into new products.\n\n Easy said, but believe me: it is a hard thing" \
                               " to do. If you want to see how the business goes here, let's visit the factory! "
            blit_text(screen, description_text, (915, 370), font, (255, 255, 255))

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
            drawButton(screen, visit_button, 13, (0, 0, 0))

            # mayor message
            mayor_text_button = BUTTON.button((255, 255, 255), 930, 50, 230, 100, ' ')
            drawButton(screen, mayor_text_button, 13, (0, 0, 0))
            mayor_text = "Welcome to the BUSINESS CENTER!\nClick on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            blit_text(screen, mayor_text, (933, 50), font_intro_text)

            # description box text
            font = pygame.font.SysFont('arial', 15)
            description_text = "This is the heart of Green Landia. It is the place that conducts all the business, " \
                               "ranging from tourism, to the recycling actions. " \
                               "\n Here we establish the rules for the city and plans for the future, we create" \
                               " associations of people with different purposes and encourage the youth to participate." \
                               "\n\nLet's see how things go in here because I am indeed curious myself!"
            blit_text(screen, description_text, (915, 370), font, (255, 255, 255))

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
            drawButton(screen, visit_button, 13, (0, 0, 0))

            # mayor message
            mayor_text_button = BUTTON.button((255, 255, 255), 930, 50, 230, 100, ' ')
            drawButton(screen, mayor_text_button, 13, (0, 0, 0))
            mayor_text = "Welcome to the TOURISTIC AREA!\nClick on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            blit_text(screen, mayor_text, (933, 50), font_intro_text)

            # description box text
            font = pygame.font.SysFont('arial', 15)
            description_text = "This is one of our touristic areas. As you can see,it is a camping site, but we have so much more." \
                               "\n\nActually, we tend to focus more on getting people outside in the nature and appreciate " \
                               "its role in our lives. We have been born in nature and we evolved in nature. Not in a " \
                               "hospital. Not in our workplace. But among the trees and animals.\n\nLet's play some games " \
                               "in here, dear citizen!"
            blit_text(screen, description_text, (915, 370), font, (255, 255, 255))

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
            drawButton(screen, visit_button, 13, (0, 0, 0))

            # mayor message
            mayor_text_button = BUTTON.button((255, 255, 255), 930, 50, 230, 100, ' ')
            drawButton(screen, mayor_text_button, 13, (0, 0, 0))
            mayor_text = "Welcome to the EVENTS AREA!\nClick on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            blit_text(screen, mayor_text, (933, 50), font_intro_text)

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
            blit_text(screen, description_text, (915, 370), font, (255, 255, 255))

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

#menu

def main_menu():
    while True:

        menu_music.play(-1)
        screen = pygame.display.set_mode((900, 700))
        #background image
        screen.blit(backgroundMenu, (0,0))

        drawButton(screen, menuButton, 40, None)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos() #pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                pygame.quit()

            # menu button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menuButton.isOver(pos):
                    menu_music.stop()
                    townView(screen)
            if event.type == pygame.MOUSEMOTION:
                if menuButton.isOver(pos):
                    menuButton.color = (0, 160, 0)
                else:
                    menuButton.color = (255, 255, 255)


        pygame.display.update()


#print(pygame.font.get_fonts())
main_menu()