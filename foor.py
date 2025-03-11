import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Foor - martin Talvi")

screen.fill((0, 0, 0))

pygame.draw.rect(screen, (128, 128, 128), (100, 10, 100, 270), 2)

pygame.draw.circle(screen, (255, 0, 0), (150, 59), 39, 0)
pygame.draw.circle(screen, (255, 255, 0), (150, 144), 39, 0)
pygame.draw.circle(screen, (0, 255, 0), (150, 229), 39, 0)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()