import pygame
from pygame import mixer
import BUTTON

# Initialize the pygame
pygame.init()

#Backgrounds
backgroundMenu = pygame.image.load('images/menu_background.png')
town_view = pygame.image.load('images/town.png')
townhall = pygame.image.load('images/townhall.png')
recycling_area = pygame.image.load('images/recycling_area.jpg')
mayor_recycling_area_background = pygame.image.load('images/mayor_recycling_area_background.jpg')

mayor_normal_pose = pygame.image.load('poses/mayor_normal_pose.png')
mayor_normal_poseBig = pygame.image.load('poses/mayor_normal_pose(big).png')
mayor_superhero_pose = pygame.image.load('poses/mayor_superhero_pose.png')

#soundtrack
menu_music = mixer.Sound('music/menu.wav')
town_music = mixer.Sound('music/town.wav')
areas_music = mixer.Sound('music/recycling_area.wav')

# Title and Icon
pygame.display.set_caption("Green Landia")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

menuButton = BUTTON.button((255, 255, 255), 300, 180, 300, 70, 'START GAME')


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

def play_game_recycling_area(screen, text_button, score):
    text = "SCORE:"
    font = pygame.font.SysFont('arial', 50)

    running = True
    while running:
        pos = pygame.mouse.get_pos()  # mouse coordinates
        drawButton(screen, text_button, 13, (0, 0, 0))  # the message of the mayor
        blit_text(screen, text, (803, 50), font)

        running = False


def visit_recycling_area(screen):
    screen = pygame.display.set_mode((1200, 550))

    # texts
    text = "Let's test your knowledge in recycling!\n1.Pick up the garbage that appears on the grass." \
           "\n2.Put it in the right recycle bin.\n\nIf you're right, your number of recycled materials will\nincrease" \
           " and these materials will be used at the\nrecycling factory so you have to visit that afterwards." \
           "\n\nIf you don't recycle correctly, you will lose the material.\nTHE GAME ENDS AFTER 5 MISTAKES.\nGood luck!"

    # fonts
    font = pygame.font.SysFont('arial', 15)

    # "image" buttons description box town view
    text_button = BUTTON.button((255, 255, 255), 800, 50, 300, 300, ' ')
    play_button = BUTTON.button((150, 240, 0), 900, 300, 100, 35, 'PLAY')

    x = 1000
    running = True
    while running:

        pos = pygame.mouse.get_pos()  # mouse coordinates
        areas_music.play(-1)
        screen.blit(mayor_recycling_area_background, (790,0))
        screen.blit(recycling_area, (0, 0))

        if(x > 700):
            x -= 2
        else:
            drawButton(screen, text_button, 13, (0, 0, 0))  # the message of the mayor
            drawButton(screen, play_button, 35, (0,0,0))
            blit_text(screen, text, (803, 50), font)

            if event.type == pygame.MOUSEMOTION:
                if play_button.isOver(pos):
                    play_button.color = (0, 160, 0)
                else:
                    play_button.color = (150, 240, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.isOver(pos):
                    score = 0
                    play_game_recycling_area(screen, text_button, score)
                    text = 'Congratulations! You recycled '+str(score)+' objects!\n\nClose the window' \
                        ' if you want to leave\nthe area or play again!'
                    font = pygame.font.SysFont('arial', 20)
                    text_button = BUTTON.button((255, 255, 255), 800, 50, 300, 200, ' ')
                    play_button = BUTTON.button((150, 240, 0), 900, 200, 100, 35, 'PLAY')

        screen.blit(mayor_normal_poseBig, (x,60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False

        pygame.display.update()

    areas_music.stop()
    town_music.play(-1)
    screen = pygame.display.set_mode((1300, 700))

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

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if visit_button.isOver(pos):
            #         town_music.stop()
            #         visit_recycling_factory(screen)

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