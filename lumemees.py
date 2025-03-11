import pygame

pygame.init()  # Initialize pygame first

screen = pygame.display.set_mode([300, 300])
pygame.display.set_caption("Lumemees - Martin Talvi")

pygame.draw.circle(screen, [0, 0, 255], [150,200], 50, 1)

pygame.display.update()

# Event loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()