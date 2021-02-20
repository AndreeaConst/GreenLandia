import pygame

import Button
import BlitText
import GameGlobalVariables

# Initialize the pygame
pygame.init()

# backgrounds
recycling_factory = pygame.image.load('design/backgrounds/recycling_factory.jpg')

# descriptions
description_glass_bottle = pygame.image.load('design/recycled items/glass/description glass bottle.png')
description_fiber_glass = pygame.image.load('design/recycled items/glass/description fiber glass.png')
description_glass_bricks = pygame.image.load('design/recycled items/glass/description glass bricks.jpg')
description_glassphalt1 = pygame.image.load('design/recycled items/glass/description glassphalt 1.jpg')
description_glassphalt2 = pygame.image.load('design/recycled items/glass/description glassphalt 2.jpg')
description_reflective_paint = pygame.image.load('design/recycled items/glass/description reflective paint.png')
description_glass_tiles1 = pygame.image.load('design/recycled items/glass/description glass tiles 1.jpg')
description_glass_tiles2 = pygame.image.load('design/recycled items/glass/description glass tiles 2.jpg')
description_glass_tiles3 = pygame.image.load('design/recycled items/glass/description glass tiles 3.jpg')


def info_glass_bottle(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((0, 150, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 20 GLASS WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Glass bottles and jars are infinitely recyclable.\n" \
                 "Glass recycling is the processing of waste\n" \
                 "glass into usable products, like these glass\n" \
                 "bottles here.\n\n\n" \
                 "  To be recycled, glass waste needs to be\n" \
                 "purified and cleaned of contamination. Then,\n" \
                 "it might also have to be separated into different\n" \
                 "colors. Many recyclers collect different colors of\n" \
                 "glass separately since glass retains its color after\n" \
                 "recycling." \

    text_worker = "You have now " + str(GameGlobalVariables.score_glass) + " GLASS WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_glass_bottle, (530, 220))

        BlitText.blit_text(screen, "RECYCLED GLASS BOTTLE", (200, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_glass >= 20:
                        GameGlobalVariables.score_glass -= 20
                        text_worker = "You have now " + str(GameGlobalVariables.score_glass) + " GLASS WASTE!\n\n" \
                                                                                  "You just created a glass bottle! Congrats!\n" \
                                                                                  "      I am indeed proud of you!"
                    else:
                        text_worker = "You don't have enough glass waste\n" \
                                     "     to create a glass bottle!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (0, 150, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()


def info_fiber_glass(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((0, 150, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 20 GLASS WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Fiberglass is material made from extremely\n" \
                "fine fibers of glass.\n\n\n" \
                "  Fiberglass is used in the telecommunications\n" \
                "industry for shrouding antennas. Other uses include\n" \
                "sheet-form electrical insulators and structural\n" \
                "components commonly found in power-industry products.\n\n" \
                "  Because of fiberglass's light weight and durability,\n" \
                "it is often used in protective equipment such as helmets.\n" \
                "Many sports use fiberglass protective gear, such as\n" \
                "goaltenders' and catchers' masks." \

    text_worker = "You have now " + str(GameGlobalVariables.score_glass) + " GLASS WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_fiber_glass, (560, 220))

        BlitText.blit_text(screen, "FIBER GLASS", (240, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_glass >= 20:
                        GameGlobalVariables.score_glass -= 20
                        text_worker = "You have now " + str(GameGlobalVariables.score_glass) + " GLASS WASTE!\n\n" \
                                                                                  "You just created fiber glass! Congrats!\n" \
                                                                                  "      I am indeed proud of you!"
                    else:
                        text_worker = "You don't have enough glass waste\n" \
                                     "     to create fiber glass!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (0, 150, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()


def info_glass_bricks(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((0, 150, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 20 GLASS WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Glass brick, also known as glass block,\n" \
                "is an architectural element made from glass.\n\n" \
                "  The appearance of glass blocks can vary in\n" \
                "color, size, texture and form.\n\n" \
                "  Glass bricks provide visual obscuration while\n" \
                "admitting light.\n\n" \
                "  Today glass blocks are used in walls, skylights,\n" \
                "and sidewalk lights." \

    text_worker = "You have now " + str(GameGlobalVariables.score_glass) + " GLASS WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_glass_bricks, (560, 220))

        BlitText.blit_text(screen, "GLASS BRICKS", (240, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_glass >= 20:
                        GameGlobalVariables.score_glass -= 20
                        text_worker = "You have now " + str(GameGlobalVariables.score_glass) + " GLASS WASTE!\n\n" \
                                                                                  "You just created glass bricks! Congrats!\n" \
                                                                                  "      I am indeed proud of you!"
                    else:
                        text_worker = "You don't have enough glass waste\n" \
                                     "     to create glass bricks!\n" \
                                     "Recycle more in order to create them!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (0, 150, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()


def info_glassphalt(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((0, 150, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 50 GLASS WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  You may not realize it, but you drive over glass\n" \
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

    text_worker = "You have now " + str(GameGlobalVariables.score_glass) + " GLASS WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_glassphalt1, (560, 420))
        screen.blit(description_glassphalt2, (560, 200))

        BlitText.blit_text(screen, "GLASSPHALT", (250, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_glass >= 50:
                        GameGlobalVariables.score_glass -= 50
                        text_worker = "You have now " + str(GameGlobalVariables.score_glass) + " GLASS WASTE!\n\n" \
                                                                                  "You just created glassphalt! Congrats!\n" \
                                                                                  "      I am indeed proud of you!"
                    else:
                        text_worker = "You don't have enough glass waste\n" \
                                     "     to create glassphalt!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (0, 150, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()


def info_reflective_paint(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((0, 150, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 20 GLASS WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Reflective paint is regular paint with a reflective quality.\n" \
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

    text_worker = "You have now " + str(GameGlobalVariables.score_glass) + " GLASS WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_reflective_paint, (560, 250))

        BlitText.blit_text(screen, "REFLECTIVE PAINT", (250, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_glass >= 20:
                        GameGlobalVariables.score_glass -= 20
                        text_worker = "You have now " + str(GameGlobalVariables.score_glass) + " GLASS WASTE!\n\n" \
                                                                                  "You just created reflective paint! Congrats!\n" \
                                                                                  "      I am indeed proud of you!"
                    else:
                        text_worker = "You don't have enough glass waste\n" \
                                     "    to create reflective paint!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (0, 150, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()


def info_glass_tiles(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((0, 150, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 50 GLASS WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 40)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  The variety of garden and landscape products made from recycled glass has led to\n" \
                "the term 'greenscaping'. Unlike wood, glass mulch doesn't absorb moisture, which improves\n" \
                "water delivery while reducing the frequency of watering.\n\n" \
                "  It also comes in a wide variety of colors. Manufacturers combine recycled glass with\n" \
                "crushed porcelain embedded in concrete slab to create decorative pathways and patios."

    text_worker = "You have now " + str(GameGlobalVariables.score_glass) + " GLASS WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_glass_tiles1, (210, 350))
        screen.blit(description_glass_tiles3, (405, 400))
        screen.blit(description_glass_tiles2, (600, 350))

        BlitText.blit_text(screen, "GLASS TILES", (250, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (240, 220), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_glass >= 50:
                        GameGlobalVariables.score_glass -= 50
                        text_worker = "You have now " + str(GameGlobalVariables.score_glass) + " GLASS WASTE!\n\n" \
                                                                                  "You just created glass tiles! Congrats!\n" \
                                                                                  "      I am indeed proud of you!"
                    else:
                        text_worker = "You don't have enough glass waste\n" \
                                     "      to create glass tiles!\n" \
                                     "Recycle more in order to create them!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (0, 150, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()
