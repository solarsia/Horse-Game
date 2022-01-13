import pygame
import menu

dis_width = 1540
dis_height = 795

stable = pygame.image.load("stableeewip.png")

def run(display=None):
    print('[main] run')

    if not display:
        pygame.init()
        display = pygame.display.set_mode((dis_width,dis_height))

    mainloop(display)

def mainloop(display):
    print('[main] mainloop')

    running = True
    while running:

        print('running game ...')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() # skip rest of code
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    menu.run(display)

        display.blit(stable,(0,0))
        pygame.display.flip()

if __name__ == '__main__':
    run()