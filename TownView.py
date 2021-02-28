import Button
import BlitText
import MessageBoxSaveGame
import os
import pygame
from pygame import mixer

from town_areas import VisitRecyclingFactory
from town_areas.RecyclingArea import VisitRecyclingArea

# GLOBAL VARIABLES--------------------------------------------------------------------------------------
# Initialize the pygame
pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'  # for centering the window game

# Backgrounds
town_view_image = pygame.image.load('design/backgrounds/town.png')
townhall = pygame.image.load('design/backgrounds/townhall.png')

# Characters
mayor_normal_pose = pygame.image.load('design/poses/mayor_normal_pose.png')

# soundtrack
town_music = mixer.Sound('design/music/town.wav')

# Title and Icon
pygame.display.set_caption("Green Landia")
icon = pygame.image.load('design/backgrounds/icon.png')
pygame.display.set_icon(icon)

# fonts
font_intro_text = pygame.font.SysFont('arial', 15)
font_text_before_after_mayor = pygame.font.SysFont('javanesetext', 20)

# "image" buttons description box town view
visit_button = Button.Button((150, 240, 0), 1030, 600, 120, 50, 'VISIT AREA')

# "image" buttons town view
recycling_area = Button.Button((255, 255, 0), 500, 650, 90, 30, 'Recycling area')
supermarket = Button.Button((255, 255, 0), 360, 50, 80, 30, 'Supermarket')
water_plant = Button.Button((255, 255, 0), 500, 50, 150, 30, 'Water purification center')
recycling_plant = Button.Button((255, 255, 0), 740, 10, 100, 30, 'Recycling factory')
business_center = Button.Button((255, 255, 0), 100, 350, 100, 30, 'Business center')
touristic_area = Button.Button((255, 255, 0), 700, 450, 100, 30, 'Touristic area')
eco_events = Button.Button((255, 255, 0), 400, 450, 100, 30, 'Eco-events area')


# FUNCTIONS-----------------------------------------------------------------------------

def town_backgrounds_buttons(screen, recycling_area, supermarket, water_plant, recycling_plant,
                             business_center, touristic_area, eco_events, x):
    screen.blit(townhall, (910, 1))
    screen.blit(town_view_image, (0, 0))

    # buttons
    recycling_area.draw(screen, 13, (0, 0, 0))
    supermarket.draw(screen, 13, (0, 0, 0))
    water_plant.draw(screen, 13, (0, 0, 0))
    recycling_plant.draw(screen, 13, (0, 0, 0))
    business_center.draw(screen, 13, (0, 0, 0))
    touristic_area.draw(screen, 13, (0, 0, 0))
    eco_events.draw(screen, 13, (0, 0, 0))

    screen.blit(mayor_normal_pose, (x, 39))

def present_area(screen, event, pos, description_text, mayor_text, x):
    screen.fill((0, 0, 0))
    town_backgrounds_buttons(screen, recycling_area, supermarket, water_plant, recycling_plant,
                             business_center, touristic_area, eco_events, x)
    visit_button.draw(screen, 13, (0, 0, 0))

    # mayor message
    mayor_text_button = Button.Button((255, 255, 255), 930, 50, 230, 100, ' ')
    mayor_text_button.draw(screen, 13, (0, 0, 0))
    BlitText.blit_text(screen, mayor_text, (933, 50), font_intro_text)

    # description box text
    font = pygame.font.SysFont('arial', 15)

    BlitText.blit_text(screen, description_text, (915, 370), font, (255, 255, 255))

    if event.type == pygame.MOUSEMOTION:
        if visit_button.is_over(pos):
            visit_button.color = (0, 160, 0)
        else:
            visit_button.color = (150, 240, 0)

def town_view():
    # town background music
    town_music.play(-1)

    # background
    screen = pygame.display.set_mode((1300, 700))

    mayor_text_button = Button.Button((255, 255, 255), 950, 50, 210, 150, ' ')
    # texts
    mayor_text = "Hello! Welcome to our eco city\ndestined to change the future: \nGREEN LANDIA!\nI am the mayor, Margaret Green." \
                 "\nClick on a button of an area to\ndiscover more or press on the\n'escape' button" \
                 " on your keyboard\nto leave the town!"

    running = True

    x = 1000
    clicked_button = 0
    while running:

        pos = pygame.mouse.get_pos()  # mouse coordinates
        # backgrounds screening
        town_backgrounds_buttons(screen, recycling_area, supermarket, water_plant, recycling_plant,
                                 business_center, touristic_area, eco_events, x)
        # mayor movement + texts

        if clicked_button == 0:
            if x > 900:
                x -= 2
                text = font_text_before_after_mayor.render("THE MAYOR IS COMING...", True, (255, 255, 255))
                screen.blit(text, (950, 480))
            else:
                # text boxes
                mayor_text_button.draw(screen, 13, (0, 0, 0))  # the message of the mayor
                BlitText.blit_text(screen, mayor_text, (952, 50), font_intro_text)

                # cover the old text
                text = font_text_before_after_mayor.render("THE MAYOR IS COMING...", True, (0, 0, 0))
                screen.blit(text, (950, 480))

                # make new text appear in description box
                text = font_text_before_after_mayor.render("THE MAYOR IS SPEAKING NOW...", True, (255, 255, 255))
                screen.blit(text, (915, 480))

        elif clicked_button == 1:
            mayor_text = "Welcome to the RECYCLING AREA!\nPress on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            description_text = "THE RECYCLING AREA is the place where you, as a citizen, can sort" \
                               " your garbage. Paper to paper. Glass to glass. Plastic to plastic. And so on." \
                               "\n\nIn order to keep the planet alive and help our future generations thrive, " \
                               "we have to act responsibly.\n\nStep by step, every day, we encourage our citizens" \
                               " to care and sort their garbage at least. Let me present you the recycling area fully!" \
                               " Click on 'visit area' and let's go !!!"
            present_area(screen, event, pos, description_text, mayor_text, x)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if visit_button.is_over(pos):
                    town_music.stop()
                    VisitRecyclingArea.visit_recycling_area()
                    town_music.play()

        elif clicked_button == 2:
            mayor_text = "Welcome to the SUPERMARKET!\nPress on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            description_text = "Our Supermarkets are completely eco. We have a whole healthy industry" \
                               " and provide our citizens with the best quality food. \n\nHow was it in the prehistorical" \
                               " era? Everyone could live without chocolate, chips and other poisoning foods... " \
                               "And even though humans could not get their food easily, they would at least" \
                               " eat healthy. We want to bring this back." \
                               "\n\nClick on 'visit area' and let's see how our business is going here!"
            present_area(screen, event, pos, description_text, mayor_text, x)

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if visit_button.is_over(pos):
            #         town_music.stop()
            #         visit_supermarket(screen)

        elif clicked_button == 3:
            mayor_text = "Welcome to the\nWATER PURIFICATION CENTER!\nPress on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            description_text = "Curious what our water purification center does?\n" \
                               "Well, water purification is the process of removing undesirable chemicals, " \
                               "biological contaminants, suspended solids, and gases from water. The goal is to produce " \
                               "water fit for specific purposes. Most water is purified and disinfected for human" \
                               " consumption (drinking water), but water purification may also be carried out for a" \
                               " variety of other purposes, including medical, pharmacological, chemical, " \
                               "and industrial applications.\nI know, dear, it sounds complicated but with this we make " \
                               "your life better and we think that you should know. " \
                               "\nIf you want to experiment with the process, let's visit the area!"
            present_area(screen, event, pos, description_text, mayor_text, x)
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if visit_button.is_over(pos):
            #         town_music.stop()
            #         visit_water_plant(screen)

        elif clicked_button == 4:
            mayor_text = "Welcome to the RECYCLING FACTORY!\nPress on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            description_text = "The RECYCLING FACTORY is the place where the sorted garbage arrives, from the recycling area." \
                               "\n\nAt this facility, items are sorted, compressed, baled, stored, and then shipped out to be " \
                               "made into new products.\n\n Easy said, but believe me: it is a hard thing" \
                               " to do. If you want to see how the business goes here, let's visit the factory! "
            present_area(screen, event, pos, description_text, mayor_text, x)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if visit_button.is_over(pos):
                    town_music.stop()
                    VisitRecyclingFactory.visit_recycling_factory(screen)
                    town_music.play()

        elif clicked_button == 5:
            mayor_text = "Welcome to the BUSINESS CENTER!\nPress on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            description_text = "This is the heart of Green Landia. It is the place that conducts all the business, " \
                               "ranging from tourism, to the recycling actions. " \
                               "\n Here we establish the rules for the city and plans for the future, we create" \
                               " associations of people with different purposes and encourage the youth to participate." \
                               "\n\nLet's see how things go in here because I am indeed curious myself!"
            present_area(screen, event, pos, description_text, mayor_text, x)

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if visit_button.is_over(pos):
            #         town_music.stop()
            #         visit_business_area(screen)

        elif clicked_button == 6:
            mayor_text = "Welcome to the TOURISTIC AREA!\nPress on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            description_text = "This is one of our touristic town_areas. As you can see,it is a camping site, but we have so much more." \
                               "\n\nActually, we tend to focus more on getting people outside in the nature and appreciate " \
                               "its role in our lives. We have been born in nature and we evolved in nature. Not in a " \
                               "hospital. Not in our workplace. But among the trees and animals.\n\nLet's play some games " \
                               "in here, dear citizen!"
            present_area(screen, event, pos, description_text, mayor_text, x)

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if visit_button.is_over(pos):
            #         town_music.stop()
            #         visit_touristic_area(screen)

        else:
            mayor_text = "Welcome to the EVENTS AREA!\nPress on the 'escape' button on your\nkeyboard if you " \
                         "want to leave the town\nor press on another area button!"
            description_text = "Would you guess what happens here?\n" \
                               "With the help of our citizens from the business center, we organize weekly events." \
                               "It is quite fun: concerts, painting contests, sports, meditation sessions and whatnot." \
                               "But all with the purpose of developing our citizens into better human beings. And..." \
                               "perhaps for a bit of fun too!\n\n" \
                               "Here is a rule, though: after you will have established a plan for an event in the " \
                               "business center, come here and make it happen! We are eager to see what is on your " \
                               "entrepreneur mind.\n" \
                               "Shall we see what is happening here now? "
            present_area(screen, event, pos, description_text, mayor_text, x)

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if visit_button.is_over(pos):
            #         town_music.stop()
            #         visit_event_area(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                MessageBoxSaveGame.quit_and_save()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if recycling_area.is_over(pos):
                    clicked_button = 1
                if supermarket.is_over(pos):
                    clicked_button = 2
                if water_plant.is_over(pos):
                    clicked_button = 3
                if recycling_plant.is_over(pos):
                    clicked_button = 4
                if business_center.is_over(pos):
                    clicked_button = 5
                if touristic_area.is_over(pos):
                    clicked_button = 6
                if eco_events.is_over(pos):
                    clicked_button = 7
            if event.type == pygame.MOUSEMOTION:
                if recycling_area.is_over(pos):
                    recycling_area.color = (0, 160, 0)
                else:
                    recycling_area.color = (255, 255, 0)
                if supermarket.is_over(pos):
                    supermarket.color = (0, 160, 0)
                else:
                    supermarket.color = (255, 255, 0)
                if water_plant.is_over(pos):
                    water_plant.color = (0, 160, 0)
                else:
                    water_plant.color = (255, 255, 0)
                if business_center.is_over(pos):
                    business_center.color = (0, 160, 0)
                else:
                    business_center.color = (255, 255, 0)
                if touristic_area.is_over(pos):
                    touristic_area.color = (0, 160, 0)
                else:
                    touristic_area.color = (255, 255, 0)
                if eco_events.is_over(pos):
                    eco_events.color = (0, 160, 0)
                else:
                    eco_events.color = (255, 255, 0)
                if recycling_plant.is_over(pos):
                    recycling_plant.color = (0, 160, 0)
                else:
                    recycling_plant.color = (255, 255, 0)

        pygame.display.update()

    town_music.stop()
