import pygame
import sys

pygame.init()

# comfigurações de janela
LARGURA, ALTURA = 600, 400
TAMANHO_BLOCO = 20
COR_FUNDO = (15, 15, 20)

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Cobrinha")
relogio = pygame.time.Clock()

def main():
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        tela.fill(COR_FUNDO)
        pygame.display.flip()
        relogio.tick(10) #10 quadros por segundo

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()        