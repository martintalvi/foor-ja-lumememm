import pygame

# Käivita pygame
pygame.init()

# Loo ekraan suurusega 300x300 pikslit
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumemees - Martin Talvi")  # Määra akna pealkiri

# Täida ekraan musta taustavärviga
screen.fill((0, 0, 0))

# Joonista lumememme keha (kolm valget ringi)
pygame.draw.circle(screen, (255, 255, 255), (150, 230), 50, 0)  # Alumine osa
pygame.draw.circle(screen, (255, 255, 255), (150, 145), 40, 0)  # Keskmine osa
pygame.draw.circle(screen, (255, 255, 255), (150, 80), 30, 0)   # Ülemine osa (pea)

# Joonista silmad (kaks musta ringi)
pygame.draw.circle(screen, (0, 0, 0), (140, 73), 5, 0)  # Vasak silm
pygame.draw.circle(screen, (0, 0, 0), (160, 73), 5, 0)  # Parem silm

# Joonista porgandnina (punane kolmnurk)
pygame.draw.polygon(screen, (255, 0, 0), [(145, 85), (155, 85), (150, 100)], 0)

# Uuenda ekraani
pygame.display.update()

# Tsükkel, mis hoiab akent avatuna kuni kasutaja selle sulgeb
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Kui vajutatakse "sulge" nuppu, lõpetatakse tsükkel

# Sulge Pygame'i aken
pygame.quit()