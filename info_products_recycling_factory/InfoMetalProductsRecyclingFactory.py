import pygame

import Button
import BlitText
import GameGlobalVariables

# Initialize the pygame
import MessageBoxSaveGame

pygame.init()

# backgrounds
recycling_factory = pygame.image.load('design/backgrounds/recycling_factory.jpg')

# descriptions
description_metal_bench = pygame.image.load('design/recycled items/metal/description metal bench.jpg')
description_metal_chair = pygame.image.load('design/recycled items/metal/description metal chair.png')
description_metal_coffeeMaker = pygame.image.load('design/recycled items/metal/description metal coffeemaker.png')
description_car = pygame.image.load('design/recycled items/metal/description car.png')
description_plane = pygame.image.load('design/recycled items/metal/description plane.png')
description_metal_lamp = pygame.image.load('design/recycled items/metal/description metal lamp.png')
description_fridge = pygame.image.load('design/recycled items/metal/description fridge.png')
description_metal_utensils = pygame.image.load('design/recycled items/metal/description metal utensils.png')
description_microwave = pygame.image.load('design/recycled items/metal/description microwave.png')
description_oven = pygame.image.load('design/recycled items/metal/description oven.png')
description_toaster = pygame.image.load('design/recycled items/metal/description toaster.png')

def info_metal_bench(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 60 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this metal bench here!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_metal_bench, (560, 240))

        BlitText.blit_text(screen, "METAL BENCH", (240, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
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
                    if GameGlobalVariables.score_metal >= 60:
                        GameGlobalVariables.score_metal -= 60
                        text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!\n\n" \
                                                                         "You just created a metal bench!\n" \
                                                                         "            Congrats!"
                    else:
                        text_worker = "You don't have enough metal waste\n" \
                                     "     to create a metal bench!\n" \
                                     "Recycle more in order to create it"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (50, 0, 200)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()

def info_metal_chair(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 40 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this metal chair here!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_metal_chair, (560, 240))

        BlitText.blit_text(screen, "METAL CHAIR", (240, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
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
                    if GameGlobalVariables.score_metal >= 40:
                        GameGlobalVariables.score_metal -= 40
                        text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!\n\n" \
                                                                         "You just created a metal chair!\n" \
                                                                         "             Congrats!"
                    else:
                        text_worker = "You don't have enough metal waste\n" \
                                     "     to create a metal chair!\n" \
                                     "Recycle more in order to create it"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (50, 0, 200)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()

def info_metal_coffeemaker(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 50 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this metal coffeemaker here!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_metal_coffeeMaker, (560, 200))

        BlitText.blit_text(screen, "METAL COFFEEMAKER", (240, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
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
                    if GameGlobalVariables.score_metal >= 50:
                        GameGlobalVariables.score_metal -= 50
                        text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!\n\n" \
                                                                         "You just created a metal coffeemaker!\n" \
                                                                         "              Congrats!"
                    else:
                        text_worker = "You don't have enough metal waste\n" \
                                     "  to create a metal coffeemaker!\n" \
                                     "Recycle more in order to create it"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (50, 0, 200)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()

def info_car(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 200 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this car here!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_car, (560, 260))

        BlitText.blit_text(screen, "CAR", (280, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
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
                    if GameGlobalVariables.score_metal >= 200:
                        GameGlobalVariables.score_metal -= 200
                        text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!\n\n" \
                                                                         "You just created a car!\n" \
                                                                         "       Congrats!"
                    else:
                        text_worker = "You don't have enough metal waste\n" \
                                     "        to create a car!\n" \
                                     "Recycle more in order to create it"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (50, 0, 200)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()

def info_plane(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 300 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this plane here!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_plane, (560, 240))

        BlitText.blit_text(screen, "PLANE", (240, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
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
                    if GameGlobalVariables.score_metal >= 300:
                        GameGlobalVariables.score_metal -= 300
                        text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!\n\n" \
                                                                         "You just created a plane!\n" \
                                                                         "         Congrats!"
                    else:
                        text_worker = "You don't have enough metal waste\n" \
                                     "       to create a plane!\n" \
                                     "Recycle more in order to create it"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (50, 0, 200)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()

def info_metal_lamp(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 20 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this metal lamp here!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_metal_lamp, (630, 220))

        BlitText.blit_text(screen, "METAL LAMP", (240, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
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
                    if GameGlobalVariables.score_metal >= 20:
                        GameGlobalVariables.score_metal -= 20
                        text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!\n\n" \
                                                                         "You just created a metal lamp!\n" \
                                                                         "          Congrats!"
                    else:
                        text_worker = "You don't have enough metal waste\n" \
                                     "     to create a metal lamp!\n" \
                                     "Recycle more in order to create it"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (50, 0, 200)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()


def info_fridge(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 90 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this fridge here!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_fridge, (560, 240))

        BlitText.blit_text(screen, "FRIDGE", (240, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
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
                    if GameGlobalVariables.score_metal >= 90:
                        GameGlobalVariables.score_metal -= 90
                        text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!\n\n" \
                                                                         "You just created a fridge!\n" \
                                                                         "         Congrats!"
                    else:
                        text_worker = "You don't have enough metal waste\n" \
                                     "       to create a fridge!\n" \
                                     "Recycle more in order to create it"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (50, 0, 200)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()

def info_metal_utensils(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 20 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made these metal utensils here!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_metal_utensils, (560, 240))

        BlitText.blit_text(screen, "METAL UTENSILS", (240, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
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
                    if GameGlobalVariables.score_metal >= 20:
                        GameGlobalVariables.score_metal -= 20
                        text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!\n\n" \
                                                                         "You just created metal utensils!\n" \
                                                                         "             Congrats!"
                    else:
                        text_worker = "You don't have enough metal waste\n" \
                                     "     to create metal utensils!\n" \
                                     "Recycle more in order to create them!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (50, 0, 200)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()

def info_microwave(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 70 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this microwave here!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_microwave, (560, 240))

        BlitText.blit_text(screen, "MICROWAVE", (240, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
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
                    if GameGlobalVariables.score_metal >= 70:
                        GameGlobalVariables.score_metal -= 70
                        text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!\n\n" \
                                                                         "You just created a microwave!\n" \
                                                                         "          Congrats!"
                    else:
                        text_worker = "You don't have enough metal waste\n" \
                                     "     to create a microwave!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (50, 0, 200)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()

def info_oven(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 90 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this oven here!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_oven, (560, 240))

        BlitText.blit_text(screen, "OVEN", (240, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
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
                    if GameGlobalVariables.score_metal >= 90:
                        GameGlobalVariables.score_metal -= 90
                        text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!\n\n" \
                                                                         "You just created an oven!\n" \
                                                                         "         Congrats!"
                    else:
                        text_worker = "You don't have enough metal waste\n" \
                                     "     to create an oven!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (50, 0, 200)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()

def info_toaster(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((50, 0, 200), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 40 METAL WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Metal is one of the major materials that\n" \
                "can be recycled repeatedly without altering\n" \
                "its properties.\n\n" \
                "  Recycling emits less carbon dioxide and other\n" \
                "harmful gasses. More importantly, it saves money and\n" \
                "allows manufacturing businesses to reduce their\n" \
                "production cost. Recycling also creates jobs.\n\n" \
                "  Many of the recycled metals are reused to make\n" \
                "new appliances, or reused in construction.\n" \
                "  This is how we made this toaster here!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_toaster, (560, 240))

        BlitText.blit_text(screen, "TOASTER", (230, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
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
                    if GameGlobalVariables.score_metal >= 40:
                        GameGlobalVariables.score_metal -= 40
                        text_worker = "You have now " + str(GameGlobalVariables.score_metal) + " METAL WASTE!\n\n" \
                                                                         "You just created a toaster!\n" \
                                                                         "         Congrats!"
                    else:
                        text_worker = "You don't have enough metal waste\n" \
                                     "       to create a toaster!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (50, 0, 200)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()
