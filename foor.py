import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Foor - martin Talvi")

screen.fill((0, 0, 0))

pygame.draw.rect(screen, (255, 255, 255), (95, 20, 110, 270), 2)

pygame.draw.circle(screen, (255, 0, 0), (150, 70), 38, 0)
pygame.draw.circle(screen, (255, 255, 0), (150, 150), 38, 0)
pygame.draw.circle(screen, (0, 255, 0), (150, 230), 38, 0)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()