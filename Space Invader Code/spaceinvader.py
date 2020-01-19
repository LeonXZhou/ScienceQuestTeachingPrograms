import pygame

screen = pygame.display.set_mode([200,200])
backgroundColour = [0,0,0]
screen.fill(backgroundColour)

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
