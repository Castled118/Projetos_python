import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da tela
largura = 800
altura = 600

# Crie a tela
tela = pygame.display.set_mode((largura, altura))

# Defina o título da janela
pygame.display.set_caption("Minha Tela Pygame")

# Loop principal
while True:
    # Verifique eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualize a tela
    pygame.display.update