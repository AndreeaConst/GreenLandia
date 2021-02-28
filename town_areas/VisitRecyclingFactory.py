import Button
import BlitText
import GameGlobalVariables
import MessageBoxSaveGame

from info_products_recycling_factory import InfoOrganicProductsRecylingFactory
from info_products_recycling_factory import InfoPlasticProductsRecylingFactory
from info_products_recycling_factory import InfoPaperProductsRecylingFactory
from info_products_recycling_factory import InfoMetalProductsRecyclingFactory
from info_products_recycling_factory import InfoGlassProductsRecylingFactory

import pygame
from pygame import mixer

# Initialize the pygame
pygame.init()

# backgrounds
recycling_factory = pygame.image.load('design/backgrounds/recycling_factory.jpg')

# music
recycling_factory_music = pygame.mixer.Sound('design/music/recycling_factory.wav')
town_music = mixer.Sound('design/music/town.wav')

# objects
bio_fuel = pygame.image.load('design/recycled items/organic/biofuel.png')
compost = pygame.image.load('design/recycled items/organic/fertilizer.png')

plastic_utensils = pygame.image.load('design/recycled items/plastic/plastic_utensils.png')
bottle = pygame.image.load('design/recycled items/plastic/bottle.jpg')
cap = pygame.image.load('design/recycled items/plastic/cap.png')
shoe = pygame.image.load('design/recycled items/plastic/shoe.png')
schoolbag = pygame.image.load('design/recycled items/plastic/schoolbag.png')

recycled_paper = pygame.image.load('design/recycled items/paper/paper.jpg')
notebook = pygame.image.load('design/recycled items/paper/notebook.jpg')
napkin = pygame.image.load('design/recycled items/paper/napkin.jpg')
pencils = pygame.image.load('design/recycled items/paper/pencils.png')
book = pygame.image.load('design/recycled items/paper/book.jpg')
paper_cups = pygame.image.load('design/recycled items/paper/paper cups.jpg')

plane = pygame.image.load('design/recycled items/metal/plane.png')
car = pygame.image.load('design/recycled items/metal/car.jpg')
lamp = pygame.image.load('design/recycled items/metal/lamp.jpg')
bench = pygame.image.load('design/recycled items/metal/bench.jpg')
chair = pygame.image.load('design/recycled items/metal/chair.jpg')
coffemaker = pygame.image.load('design/recycled items/metal/coffeemaker.jpg')
fridge = pygame.image.load('design/recycled items/metal/fridge.jpg')
metal_utensils = pygame.image.load('design/recycled items/metal/metal utensils.jpg')
microwave = pygame.image.load('design/recycled items/metal/microwave.jpg')
oven = pygame.image.load('design/recycled items/metal/oven.jpg')
toaster = pygame.image.load('design/recycled items/metal/toaster.jpg')

glass_bottle = pygame.image.load('design/recycled items/glass/glass bottle.png')
fiber_glass = pygame.image.load('design/recycled items/glass/fiberglass.jpg')
glass_bricks = pygame.image.load('design/recycled items/glass/glass bricks.jpg')
glassphalt = pygame.image.load('design/recycled items/glass/glassphalt.jpg')
reflective_paint = pygame.image.load('design/recycled items/glass/reflective paint.png')
tiles = pygame.image.load('design/recycled items/glass/tiles.jpg')

# arrows
arrow_right = pygame.image.load('design/arrows/arrow_right.png')
arrow_down = pygame.image.load('design/arrows/arrow_down.png')
arrow_up = pygame.image.load('design/arrows/arrow_up.png')
arrow_left = pygame.image.load('design/arrows/arrow_left.png')

# character
worker = pygame.image.load('design/poses/worker.png')


def table_of_contents_recycling_factory(screen):
    text = "   Hello! I am Paul, the chef worker here.\n   In the box to the left, you have the " \
           " amount of\nrecycled materials of each kind so far and how much\nmaterial we need to recreate something else." \
           "\n   We will create new products and put them\non the market." \
           " You choose which products\nwe can recreate by clicking on them." \
           "\n\n Go to the market after this process!\n\n You can return to the town by pressing\nthe escape button on your keyboard!"
    font = pygame.font.SysFont('arial', 20)
    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 30)

    text_button = Button.Button((255, 255, 255), 800, 50, 400, 290, ' ')
    table = Button.Button((0, 0, 0), 50, 50, 590, 630, ' ')
    glass_square = Button.Button((0, 180, 0), 50, 50, 120, 130, ' ')
    metal_square = Button.Button((0, 0, 255), 170, 50, 115, 130, ' ')
    organic_square = Button.Button((255, 200, 0), 285, 50, 115, 130, ' ')
    paper_square = Button.Button((255, 255, 0), 400, 50, 120, 130, ' ')
    plastic_square = Button.Button((255, 0, 0), 520, 50, 120, 130, ' ')

    glass = pygame.image.load('design/trash/trash1.png')
    metal = pygame.image.load('design/trash/trash12.png')
    organic = pygame.image.load('design/trash/trash36.png')
    paper = pygame.image.load('design/trash/trash42.png')
    plastic = pygame.image.load('design/trash/trash67.png')

    text_button.draw(screen, 13, (0, 0, 0))  # the message of the worker
    BlitText.blit_text(screen, text, (802, 50), font)
    table.draw(screen, 13, (0, 0, 0))

    glass_square.draw(screen, 13, (0, 0, 0))
    metal_square.draw(screen, 13, (0, 0, 0))
    organic_square.draw(screen, 13, (0, 0, 0))
    paper_square.draw(screen, 13, (0, 0, 0))
    plastic_square.draw(screen, 13, (0, 0, 0))

    screen.blit(glass, (43, 30))
    score = font1.render("Glass: " + str(GameGlobalVariables.score_glass), True, (0, 0, 0))
    screen.blit(score, (80, 150))

    screen.blit(metal, (190, 50))
    score = font1.render("Metal: " + str(GameGlobalVariables.score_metal), True, (0, 0, 0))
    screen.blit(score, (195, 150))

    screen.blit(organic, (307, 95))
    score = font1.render("Organic: " + str(GameGlobalVariables.score_organic), True, (0, 0, 0))
    screen.blit(score, (315, 150))

    screen.blit(paper, (395, 60))
    score = font1.render("Paper: " + str(GameGlobalVariables.score_paper), True, (0, 0, 0))
    screen.blit(score, (430, 150))

    screen.blit(plastic, (510, 70))
    score = font1.render("Plastic: " + str(GameGlobalVariables.score_plastic), True, (0, 0, 0))
    screen.blit(score, (555, 150))

    BlitText.blit_text(screen, "BUILD ITEMS", (223, 180), font2, (255, 255, 255))


def more_products_right_recycling_factory(screen):
    while True:
        font3 = pygame.font.SysFont('arialblack', 12)

        table_of_contents_recycling_factory(screen)

        screen.blit(arrow_left, (50, 422))
        screen.blit(worker, (700, 0))

        z = 250
        const = 2
        for i in range(0, 3):
            y = 80
            if i == 2:
                const += 1
            for j in range(0, const):
                white_square = Button.Button((255, 255, 255), y, z, 175, 130, ' ')
                white_square.draw(screen, 13, (0, 0, 0))
                y += 175
            z += 130

        screen.blit(bio_fuel, (130, 255))
        BlitText.blit_text(screen, "        BIOFUEL\n300 ORGANIC WASTE", (92, 344), font3, (0, 0, 0))

        screen.blit(compost, (300, 247))
        BlitText.blit_text(screen, "       COMPOST\n50 ORGANIC WASTE", (270, 344), font3, (0, 0, 0))

        screen.blit(cap, (100, 370))
        BlitText.blit_text(screen, "         CAP\n30 PLASTIC WASTE", (100, 475), font3, (0, 0, 0))

        screen.blit(shoe, (280, 370))
        BlitText.blit_text(screen, "         SHOE\n50 PLASTIC WASTE", (275, 475), font3, (0, 0, 0))

        screen.blit(pencils, (120, 495))
        BlitText.blit_text(screen, "RECYCLED PAPER PENCIL\n     30 PAPER WASTE", (80, 607), font3, (0, 0, 0))

        screen.blit(book, (280, 510))
        BlitText.blit_text(screen, "        BOOK\n80 PAPER WASTE", (280, 607), font3, (0, 0, 0))

        screen.blit(paper_cups, (470, 510))
        BlitText.blit_text(screen, "   PAPER CUPS\n20 PAPER WASTE", (460, 607), font3, (0, 0, 0))

        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if 40 <= mx <= 70 and 420 <= my <= 450:
                running = True
                return running

            if event.type == pygame.QUIT:
                MessageBoxSaveGame.quit_and_save()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    return running

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 130 <= mx <= 200 and 255 <= my <= 350:
                    InfoOrganicProductsRecylingFactory.info_biofuel(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 300 <= mx <= 360 and 247 <= my <= 350:
                    InfoOrganicProductsRecylingFactory.info_compost(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 100 <= mx <= 200 and 370 <= my <= 470:
                    InfoPlasticProductsRecylingFactory.info_cap(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 280 <= mx <= 390 and 370 <= my <= 460:
                    InfoPlasticProductsRecylingFactory.info_shoe(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 120 <= mx <= 210 and 475 <= my <= 570:
                    InfoPaperProductsRecylingFactory.info_pencils(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 280 <= mx <= 390 and 510 <= my <= 590:
                    InfoPaperProductsRecylingFactory.info_book(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 470 <= mx <= 570 and 510 <= my <= 610:
                    InfoPaperProductsRecylingFactory.info_cups(screen, worker)
                    screen.blit(recycling_factory, (0, 0))

        pygame.display.update()


def more_products_right1_recycling_factory(screen):
    while True:
        font3 = pygame.font.SysFont('arialblack', 12)

        table_of_contents_recycling_factory(screen)
        screen.blit(arrow_left, (50, 422))
        screen.blit(worker, (700, 0))

        z = 250
        const = 3
        for i in range(0, 3):
            if i == 2:
                const -= 1
            y = 80
            for j in range(0, const):
                white_square = Button.Button((255, 255, 255), y, z, 175, 130, ' ')
                white_square.draw(screen, 13, (0, 0, 0))
                y += 175
            z += 130

        screen.blit(glassphalt, (123, 250))
        BlitText.blit_text(screen, "    GLASSPHALT\n50 GLASS WASTE", (107, 345), font3, (0, 0, 0))

        screen.blit(reflective_paint, (293, 250))
        BlitText.blit_text(screen, "REFLECTIVE PAINT\n 20 GLASS WASTE", (280, 345), font3, (0, 0, 0))

        screen.blit(tiles, (467, 250))
        BlitText.blit_text(screen, "        TILES\n50 GLASS WASTE", (460, 345), font3, (0, 0, 0))

        screen.blit(fridge, (120, 380))
        BlitText.blit_text(screen, "      FRIDGE\n90 METAL WASTE", (110, 474), font3, (0, 0, 0))

        screen.blit(metal_utensils, (277, 380))
        BlitText.blit_text(screen, "METAL UTENSILS\n20 METAL WASTE", (280, 474), font3, (0, 0, 0))

        screen.blit(microwave, (465, 380))
        BlitText.blit_text(screen, "    MICROWAVE\n70 METAL WASTE", (460, 474), font3, (0, 0, 0))

        screen.blit(oven, (116, 510))
        BlitText.blit_text(screen, "        OVEN\n90 METAL WASTE", (105, 605), font3, (0, 0, 0))

        screen.blit(toaster, (283, 510))
        BlitText.blit_text(screen, "      TOASTER\n40 METAL WASTE", (280, 605), font3, (0, 0, 0))

        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if 40 <= mx <= 70 and 420 <= my <= 450:
                running = True
                return running

            if event.type == pygame.QUIT:
                MessageBoxSaveGame.quit_and_save()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    return running

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 123 <= mx <= 223 and 250 <= my <= 350:
                    InfoGlassProductsRecylingFactory.info_glassphalt(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 293 <= mx <= 380 and 250 <= my <= 350:
                    InfoGlassProductsRecylingFactory.info_reflective_paint(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 467 <= mx <= 567 and 250 <= my <= 350:
                    InfoGlassProductsRecylingFactory.info_glass_tiles(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 120 <= mx <= 185 and 380 <= my <= 470:
                    InfoMetalProductsRecyclingFactory.info_fridge(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 277 <= mx <= 380 <= my <= 465:
                    InfoMetalProductsRecyclingFactory.info_metal_utensils(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 465 <= mx <= 570 and 380 <= my <= 480:
                    InfoMetalProductsRecyclingFactory.info_microwave(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 116 <= mx <= 200 and 510 <= my <= 610:
                    InfoMetalProductsRecyclingFactory.info_oven(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 283 <= mx <= 380 and 510 <= my <= 600:
                    InfoMetalProductsRecyclingFactory.info_toaster(screen, worker)
                    screen.blit(recycling_factory, (0, 0))

        pygame.display.update()


def more_products_down_recycling_factory(screen):
    while True:
        font3 = pygame.font.SysFont('arialblack', 12)

        table_of_contents_recycling_factory(screen)
        screen.blit(worker, (700, 0))

        z = 250
        for i in range(0, 3):
            y = 80
            for j in range(0, 3):
                white_square = Button.Button((255, 255, 255), y, z, 175, 130, ' ')
                white_square.draw(screen, 13, (0, 0, 0))
                y += 175
            z += 130

        screen.blit(glass_bottle, (120, 247))
        BlitText.blit_text(screen, "      BOTTLE \n20 GLASS WASTE", (110, 345), font3, (0, 0, 0))

        screen.blit(fiber_glass, (290, 250))
        BlitText.blit_text(screen, "   FIBER GLASS\n20 GLASS WASTE", (280, 345), font3, (0, 0, 0))

        screen.blit(glass_bricks, (470, 250))
        BlitText.blit_text(screen, "  GLASS BRICKS\n20 GLASS WASTE", (460, 345), font3, (0, 0, 0))

        screen.blit(bench, (120, 380))
        BlitText.blit_text(screen, "       BENCH\n60 METAL WASTE", (100, 474), font3, (0, 0, 0))

        screen.blit(chair, (295, 380))
        BlitText.blit_text(screen, "       CHAIR\n40 METAL WASTE", (285, 474), font3, (0, 0, 0))

        screen.blit(coffemaker, (480, 380))
        BlitText.blit_text(screen, " COFFEE MAKER\n50 METAL WASTE", (460, 474), font3, (0, 0, 0))

        screen.blit(plane, (100, 525))
        BlitText.blit_text(screen, "       PLANE\n300 METAL WASTE", (100, 605), font3, (0, 0, 0))

        screen.blit(car, (280, 510))
        BlitText.blit_text(screen, "          CAR\n200 METAL WASTE", (275, 605), font3, (0, 0, 0))

        screen.blit(lamp, (465, 510))
        BlitText.blit_text(screen, "         LAMP\n 20 METAL WASTE", (450, 605), font3, (0, 0, 0))

        screen.blit(arrow_up, (320, 220))
        screen.blit(arrow_right, (610, 433))

        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if 315 <= mx <= 340 and 220 <= my <= 240:
                running = True
                return running
            if 605 <= mx <= 625 and 433 <= my <= 463:
                running = more_products_right1_recycling_factory(screen)
                if not running:
                    return running

            if event.type == pygame.QUIT:
                MessageBoxSaveGame.quit_and_save()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    return running

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 120 <= mx <= 190 and 247 <= my <= 350:
                    InfoGlassProductsRecylingFactory.info_glass_bottle(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 290 <= mx <= 405 and 250 <= my <= 350:
                    InfoGlassProductsRecylingFactory.info_fiber_glass(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 470 <= mx <= 570 and 250 <= my <= 350:
                    InfoGlassProductsRecylingFactory.info_glass_bricks(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 120 <= mx <= 220 and 380 <= my <= 480:
                    InfoMetalProductsRecyclingFactory.info_metal_bench(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 295 <= mx <= 370 and 380 <= my <= 480:
                    InfoMetalProductsRecyclingFactory.info_metal_chair(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 550 >= mx >= 480 >= my >= 380:
                    InfoMetalProductsRecyclingFactory.info_metal_coffeemaker(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 280 <= mx <= 390 and 510 <= my <= 577:
                    InfoMetalProductsRecyclingFactory.info_car(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 100 <= mx <= 200 and 525 <= my <= 580:
                    InfoMetalProductsRecyclingFactory.info_plane(screen, worker)
                    screen.blit(recycling_factory, (0, 0))
                if 465 <= mx <= 565 and 510 <= my <= 605:
                    InfoMetalProductsRecyclingFactory.info_metal_lamp(screen, worker)
                    screen.blit(recycling_factory, (0, 0))

        pygame.display.update()


def visit_recycling_factory(screen):
    # MAIN WINDOW FOR THE PRODUCTS

    font3 = pygame.font.SysFont('arialblack', 12)

    running = True
    x = 1000
    while running:
        recycling_factory_music.play(-1)
        screen.blit(recycling_factory, (0, 0))

        if x > 700:
            x -= 3
        else:
            table_of_contents_recycling_factory(screen)

            z = 250
            const = 2

            for i in range(0, 3):
                y = 80
                if i == 1:
                    const += 1
                for j in range(0, const):
                    white_square = Button.Button((255, 255, 255), y, z, 175, 130, ' ')
                    white_square.draw(screen, 13, (0, 0, 0))
                    y += 175
                z += 130

            screen.blit(bio_fuel, (130, 255))
            BlitText.blit_text(screen, "        BIOFUEL\n300 ORGANIC WASTE", (92, 344), font3, (0, 0, 0))

            screen.blit(compost, (300, 247))
            BlitText.blit_text(screen, "       COMPOST\n50 ORGANIC WASTE", (270, 344), font3, (0, 0, 0))

            screen.blit(plastic_utensils, (100, 370))
            BlitText.blit_text(screen, "REUSABLE UTENSILS\n 50 PLASTIC WASTE", (95, 475), font3, (0, 0, 0))

            screen.blit(schoolbag, (290, 370))
            BlitText.blit_text(screen, "      SCHOOLBAG\n 70 PLASTIC WASTE", (275, 475), font3, (0, 0, 0))

            screen.blit(bottle, (485, 380))
            BlitText.blit_text(screen, "REUSABLE BOTTLE\n10 PLASTIC WASTE", (450, 475), font3, (0, 0, 0))

            screen.blit(recycled_paper, (125, 520))
            BlitText.blit_text(screen, "       PAPER STOCK\n     50 PAPER WASTE", (85, 607), font3, (0, 0, 0))

            screen.blit(notebook, (280, 510))
            BlitText.blit_text(screen, "PAPER COVER NOTEBOOK\n     30 PAPER WASTE", (254, 607), font3, (0, 0, 0))

            screen.blit(napkin, (445, 510))
            BlitText.blit_text(screen, "        PAPER NAPKIN\n      10 PAPER WASTE", (430, 607), font3, (0, 0, 0))

            screen.blit(arrow_right, (610, 422))
            screen.blit(arrow_down, (320, 645))

            mx, my = pygame.mouse.get_pos()
            if 600 <= mx <= 640 and 422 <= my <= 440:
                running = more_products_right_recycling_factory(screen)
            if 315 <= mx <= 345 and 640 <= my <= 670:
                running = more_products_down_recycling_factory(screen)

        screen.blit(worker, (x, 0))

        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                MessageBoxSaveGame.quit_and_save()
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 130 <= mx <= 200 and 255 <= my <= 350:
                    InfoOrganicProductsRecylingFactory.info_biofuel(screen, worker)
                if 300 <= mx <= 360 and 247 <= my <= 350:
                    InfoOrganicProductsRecylingFactory.info_compost(screen, worker)
                if 100 <= mx <= 230 and 370 <= my <= 470:
                    InfoPlasticProductsRecylingFactory.info_bioutensils(screen, worker)
                if 290 <= mx <= 385 and 370 <= my <= 470:
                    InfoPlasticProductsRecylingFactory.info_plastic_backpack(screen, worker)
                if 485 <= mx <= 535 and 380 <= my <= 480:
                    InfoPlasticProductsRecylingFactory.info_plastic_bottle(screen, worker)
                if 125 <= mx <= 210 and 520 <= my <= 610:
                    InfoPaperProductsRecylingFactory.info_paper_stock(screen, worker)
                if 280 <= mx <= 390 and 510 <= my <= 600:
                    InfoPaperProductsRecylingFactory.info_notebook(screen, worker)
                if 445 <= mx <= 575 and 510 <= my <= 600:
                    InfoPaperProductsRecylingFactory.info_napkins(screen, worker)

        pygame.display.update()

    recycling_factory_music.stop()
