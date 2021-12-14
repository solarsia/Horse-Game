import pygame

# Button Function
def button(screen, position, text, size, txt_colour, bg_colour):
    font = pygame.font.SysFont("Comic Sans MS", size)
    text_render = font.render(text, 1, txt_colour)
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, bg_colour, (x, y, w , h))
    return screen.blit(text_render, (x, y))