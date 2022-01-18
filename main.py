import pygame
import menu
import buttons

dis_width = 1540
dis_height = 795

stable = pygame.image.load("stable.png")
back_btn_bg = [120, 67, 82]
back_btn_txt = [224, 215, 218]

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
                if back.collidepoint(pygame.mouse.get_pos()):
                    menu.run(display)

        display.blit(stable,(0,0))
        back = buttons.button(display, (50, 50), "Back", 50, back_btn_txt, back_btn_bg)
        pygame.display.flip()

if __name__ == '__main__':
    run()