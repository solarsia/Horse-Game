import pygame
import buttons

pygame.init()

dis_width = 1540
dis_height = 795

stable = pygame.image.load("stableeewip.png")
background_colour = [224, 215, 218] # Off White
title_colour = [120, 67, 82] # Dark Pink
start_btn_bg = [120, 67, 82]
start_btn_txt = [224, 215, 218]
quit_btn_bg = [120, 67, 82]
quit_btn_txt = [224, 215, 218]

myfont = pygame.font.SysFont('Comic Sans MS', 100)

# Display
display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Horse Game")

def game():
    game_close = False

    while not game_close:
        
        display.fill(background_colour)
        b1 = buttons.button(display, (800, 200), "Quit me", 50, quit_btn_txt, quit_btn_bg)
        b2 = buttons.button(display, (600, 200), "Start", 50, start_btn_txt, start_btn_bg)

        title = myfont.render('Horse Game', False, title_colour)
        title_rect = title.get_rect(center=(dis_width/2, 100))
        display.blit(title,title_rect)
            
        #Press X to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_start:
                    main.run(display)  # run game
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check when you click if the coordinates of the pointer are in the rectangle of the buttons
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    main.run(display)  # run game
        pygame.display.update()
    pygame.quit()
    quit()

game()