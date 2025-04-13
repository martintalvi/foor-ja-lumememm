import pygame

# Käivita Pygame
pygame.init()

# Loo 300x300 suurusega aken
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Foor - Martin Talvi")  # Määra akna pealkiri

# Täida ekraan musta taustaga
screen.fill((0, 0, 0))

# Joonista foori kast
pygame.draw.rect(screen, (128, 128, 128), (100, 10, 100, 270), 2)

# Joonista foori tuled (punane, kollane, roheline)
pygame.draw.circle(screen, (255, 0, 0), (150, 59), 39, 0)       # Punane tuli
pygame.draw.circle(screen, (255, 255, 0), (150, 144), 39, 0)    # Kollane tuli
pygame.draw.circle(screen, (0, 255, 0), (150, 229), 39, 0)      # Roheline tuli

# Uuenda ekraani
pygame.display.update()

# Tsükkel, mis hoiab akna avatuna kuni kasutaja selle sulgeb
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Sulge Pygame
pygame.quit()
