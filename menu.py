import pygame
import main
import buttons

# display height and width
dis_width = 1540
dis_height = 795

# title colour
title_colour = [120, 67, 82] # Dark Pink

# background colour
background_colour = [224, 215, 218] # Off White

# button colours
start_btn_bg = [120, 67, 82]
start_btn_txt = [224, 215, 218]
quit_btn_bg = [120, 67, 82]
quit_btn_txt = [224, 215, 218]

# function to create the menu display
def run(display=None):
    print('[menu] run')

    if not display:
        pygame.init()
        display = pygame.display.set_mode((dis_width,dis_height))

    mainloop(display)

# display the menu page
def mainloop(display):
    print('[menu] mainloop')

    running = True
    while running:

        print('running menu ...')

        for event in pygame.event.get():
            # if user presses X quit game
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            # if user prsses escape quit game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

                # press s OR right OR up to start
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_start:
                    main.run(display)  # run game

            # if user clicks on either of the buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                # click quit button to quit
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                # click start button to start
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    main.run(display)  # run game

        # fill background
        display.fill(background_colour)

        # display the title 
        titleFont = pygame.font.SysFont('Comic Sans MS', 100)
        title = titleFont.render('Horse Game', False, title_colour)
        title_rect = title.get_rect(center=(dis_width/2, 100))
        display.blit(title,title_rect)

        # display the instructions ############### TO FIX ###############
        # instructionsFont = pygame.font.SysFont('Comic Sans MS', 40)
        # instructions = instructionsFont.render('Instructions \n X is a game where you can look after your horses. \n You can buy equipment, feed, and hay from the store. \n You can also earn money, which you can use at the store.', False, title_colour)
        # instructions_rect = instructions.get_rect(center=(dis_width/2, 300))
        # display.blit(instructions,instructions_rect)

        # display the buttons 
        b1 = buttons.button(display, (800, 200), "Quit me", 50, quit_btn_txt, quit_btn_bg)
        b2 = buttons.button(display, (600, 200), "Start", 50, start_btn_txt, start_btn_bg)

        pygame.display.flip()
   

# call the run function to display the menu
if __name__ == '__main__':
    run()