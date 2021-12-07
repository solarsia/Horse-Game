import pygame
import buttons

pygame.init()

dis_width = 1540
dis_height = 800

background_colour = [30, 49, 55] # Dark Blue

# Display
display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Horse Game")

def game():
    game_close = False

    while not game_close:
        
        display.fill(background_colour)
        b1 = buttons.button(display, (300, 300), "Quit me", 50, "red on yellow")
        b2 = buttons.button(display, (500, 300), "Start", 50, "white on green")
            
        #Press X to quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                key_to_start = event.key == pygame.K_s or event.key == pygame.K_RIGHT or event.key == pygame.K_UP
                if key_to_start:
                    print("Ok, let's go")
            if event.type == pygame.MOUSEBUTTONDOWN:
                # check when you click if the coordinates of the pointer are in the rectangle of the buttons
                if b1.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif b2.collidepoint(pygame.mouse.get_pos()):
                    print("Ok, let's go")
        pygame.display.update()
    pygame.quit()
    quit()

game()