import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumemees - Martin Talvi")

screen.fill((0, 0, 0))

pygame.draw.circle(screen, (255, 255, 255), (150, 230), 50, 0)
pygame.draw.circle(screen, (255, 255, 255), (150, 145), 40, 0)
pygame.draw.circle(screen, (255, 255, 255), (150, 80), 30, 0)

pygame.draw.circle(screen, (0, 0, 0), (140, 73), 5, 0)
pygame.draw.circle(screen, (0, 0, 0), (160, 73), 5, 0)

pygame.draw.polygon(screen, (255, 0, 0), [(145, 85), (155, 85), (150, 100)], 0)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
