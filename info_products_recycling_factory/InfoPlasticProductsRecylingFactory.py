
# backgrounds
import pygame

import Button
import BlitText
import GameGlobalVariables

# Initialize the pygame
pygame.init()

# descriptions
recycling_factory = pygame.image.load('design/backgrounds/recycling_factory.jpg')

# decriptions
plastic_utensils = pygame.image.load('design/recycled items/plastic/plastic_utensils.png')
description_utensils = pygame.image.load('design/recycled items/plastic/description utensils.jpg')
description_schoolbag = pygame.image.load('design/recycled items/plastic/description schoolbag.png')
description_plastic_bottle = pygame.image.load('design/recycled items/plastic/description plastic bottle.png')
description_cap = pygame.image.load('design/recycled items/plastic/description cap.png')
description_shoe = pygame.image.load('design/recycled items/plastic/description shoe.png')

def info_cap(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((200, 10, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 30 PLASTIC WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "    Recycled plastics are plastic made from\n" \
                "recycled plastic materials. In other words,\n" \
                "products that are recycled into something new.\n\n" \
                "  Upon collection, the plastic is then cleaned,\n" \
                "processed into flakes and heated into pellets,\n" \
                "before being stretched into a yarn-like fiber\n" \
                "and woven into a functional fabric. Like a cap!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_plastic) + " PLASTIC WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_cap, (520, 230))

        BlitText.blit_text(screen, "RECYCLED PLASTIC CAP", (240, 142), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (250, 240), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_plastic >= 30:
                        GameGlobalVariables.score_plastic -= 30
                        text_worker = "You have now " + str(GameGlobalVariables.score_plastic) + " PLASTIC WASTE!\n\n" \
                                                                           "You just created a recycled plastic cap! Congrats!\n" \
                                                                           "          I am indeed proud of you!"
                    else:
                        text_worker = "You don't have enough plastic waste\n" \
                                     "        to create a cap!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (200, 10, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()

def info_bioutensils(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((200, 10, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 50 PLASTIC WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 35)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Utensils manufactured with recycled plastic can be recycled again using existing recycling\n" \
                "resources.\n\n" \
                "  Recycled plastics are plastic made from recycled plastic materials. In other words, products\n" \
                "that are recycled into something new.\n\n" \
                "  While this is a great alternative to keeping a product out of the landfill, there are still\n" \
                "resources that go into the process of collecting and recycling an item.\n\n" \
                "  So still, it is better to avoid plastic utensils as much as you can!"

    text_worker = "You have now " + str(GameGlobalVariables.score_plastic) + " PLASTIC WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(plastic_utensils, (650, 65))
        screen.blit(description_utensils, (580, 355))

        BlitText.blit_text(screen, "REUSABLE UTENSILS", (210, 138), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (230, 220), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_plastic >= 50:
                        GameGlobalVariables.score_plastic -= 50
                        text_worker = "You have now " + str(GameGlobalVariables.score_plastic) + " PLASTIC WASTE!\n\n" \
                                                                           "You just created recycled utensils! Congrats!\n" \
                                                                           "         I am indeed proud of you!"
                    else:
                        text_worker = "You don't have enough plastic waste\n" \
                                     "     to create recycled utensils!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (200, 10, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()

def info_plastic_backpack(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((200, 10, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 70 PLASTIC WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  Recycled plastics are plastic made from recycled plastic\n" \
                "materials. In other words, products that are recycled into\n" \
                "something new.\n\n" \
                "  Upon collection, the plastic is then cleaned, processed into\n" \
                "flakes and heated into pellets, before being stretched into a\n" \
                "yarn-like fiber and woven into a functional fabric. Items from\n" \
                "this collection are shipped in a zero-waste packaging solution:\n" \
                "water-resistant reversible tote bags." \

    text_worker = "You have now " + str(GameGlobalVariables.score_plastic) + " PLASTIC WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_schoolbag, (550, 250))

        BlitText.blit_text(screen, "RECYCLED PLASTIC SCHOOLBAG", (200, 142), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (230, 270), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_plastic >= 70:
                        GameGlobalVariables.score_plastic -= 70
                        text_worker = "You have now " + str(GameGlobalVariables.score_plastic) + " PLASTIC WASTE!\n\n" \
                                                                           "You just created a recycled plastic schoolbag! Congrats!\n" \
                                                                           "          I am indeed proud of you!"
                    else:
                        text_worker = "You don't have enough plastic waste\n" \
                                     "       to create a schoolbag!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (200, 10, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()

def info_plastic_bottle(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((200, 10, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 10 PLASTIC WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "  After you put your plastic bottle into\n" \
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

    text_worker = "You have now " + str(GameGlobalVariables.score_plastic) + " PLASTIC WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_plastic_bottle, (520, 230))

        BlitText.blit_text(screen, "RECYCLED PLASTIC BOTTLE", (240, 142), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (250, 220), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_plastic >= 10:
                        GameGlobalVariables.score_plastic -= 10
                        text_worker = "You have now " + str(GameGlobalVariables.score_plastic) + " PLASTIC WASTE!\n\n" \
                                                                           "You just created a recycled plastic bottle! Congrats!\n" \
                                                                           "          I am indeed proud of you!"
                    else:
                        text_worker = "You don't have enough plastic waste\n" \
                                     "     to create a plastic bottle!\n" \
                                     "Recycle more in order to create it!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (200, 10, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()

def info_shoe(screen, worker):
    table1 = Button.Button((255, 255, 255), 200, 50, 590, 590, ' ')
    table2 = Button.Button((200, 10, 0), 200, 50, 590, 133, ' ')
    text_button = Button.Button((255, 255, 255), 850, 50, 350, 200, ' ')
    create_button = Button.Button((255, 180, 0), 385, 560, 200, 50, 'CREATE FOR 50 PLASTIC WASTE')

    font1 = pygame.font.SysFont('arial', 15)
    font2 = pygame.font.SysFont('arialblack', 32)
    font3 = pygame.font.SysFont('arial', 20)
    text_table = "    Recycled plastics are plastic made from\n" \
                "recycled plastic materials. In other words,\n" \
                "products that are recycled into something new.\n\n" \
                "  Upon collection, the plastic is then cleaned,\n" \
                "processed into flakes and heated into pellets,\n" \
                "before being stretched into a yarn-like fiber\n" \
                "and woven into a functional fabric. Like shoes!" \

    text_worker = "You have now " + str(GameGlobalVariables.score_plastic) + " PLASTIC WASTE!"
    run = True
    while run:
        screen.blit(recycling_factory, (0, 0))

        table1.draw(screen, 13, (0, 0, 0))
        table2.draw(screen, 13, (0, 0, 0))
        create_button.draw(screen, 13, (0, 0, 0))
        text_button.draw(screen, 13, (0, 0, 0))

        screen.blit(worker, (700, 0))
        screen.blit(description_shoe, (520, 230))

        BlitText.blit_text(screen, "RECYCLED PLASTIC SHOE", (240, 142), font2, (0, 0, 0))
        BlitText.blit_text(screen, text_table, (250, 260), font1, (0, 0, 0))
        BlitText.blit_text(screen, text_worker, (880, 100), font3, (0, 0, 0))

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()  # pos stores the x and y coordinates for the mouse

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if create_button.is_over(pos):
                    if GameGlobalVariables.score_plastic >= 50:
                        GameGlobalVariables.score_plastic -= 50
                        text_worker = "You have now " + str(GameGlobalVariables.score_plastic) + " PLASTIC WASTE!\n\n" \
                                                                           "You just created recycled plastic shoes! Congrats!\n" \
                                                                           "          I am indeed proud of you!"
                    else:
                        text_worker = "You don't have enough plastic waste\n" \
                                     "        to create shoes!\n" \
                                     "Recycle more in order to create them!"
            if event.type == pygame.MOUSEMOTION:
                if create_button.is_over(pos):
                    create_button.color = (200, 10, 0)
                else:
                    create_button.color = (255, 255, 255)

        pygame.display.update()
