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


class Cobra:
    def __init__(self):
        #começa no centro da tela, com 1 segmento
        x_inicial = (LARGURA // 2)  // TAMANHO_BLOCO * TAMANHO_BLOCO
        y_inicial = (ALTURA // 2)  // TAMANHO_BLOCO * TAMANHO_BLOCO
        self.corpo = [(x_inicial, y_inicial)]
        self.direcao = (TAMANHO_BLOCO, 0) #começa indo para a direita

    def desenhar(self, tela):
        for segmento in self.corpo:
            retangulo = pygame.Rect(segmento[0], segmento[1], TAMANHO_BLOCO, TAMANHO_BLOCO)
            pygame.draw.rect(tela, (80, 200, 120), retangulo)
            pygame.draw.rect(tela, (15, 15, 20), retangulo, 1) # contorno

    def mudar_direcao(self, nova_direcao):
        #impede movimento 180 graus (voltar sobre o próprio corpo)
        oposto = (-self.direcao[0], -self.direcao[1])
        if nova_direcao != oposto:
            self.direcao = nova_direcao

    def mover(self):
        cabeca_x, cabeca_y = self.corpo[0]
        nova_cabeca = (cabeca_x + self.direcao[0], cabeca_y + self.direcao[1])
        self.corpo.insert(0, nova_cabeca) # adiciona nova cabeça
        self.corpo.pop()        # remove o último segmento

def main():
    cobra = Cobra()
    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    cobra.mudar_direcao((0, -TAMANHO_BLOCO))
                elif evento.key == pygame.K_DOWN:
                    cobra.mudar_direcao((0, TAMANHO_BLOCO))
                elif evento.key == pygame.K_LEFT:
                    cobra.mudar_direcao((-TAMANHO_BLOCO, 0))
                elif evento.key == pygame.K_RIGHT:
                    cobra.mudar_direcao((TAMANHO_BLOCO, 0))

        cobra.mover()

        tela.fill(COR_FUNDO)
        cobra.desenhar(tela)
        pygame.display.flip()
        relogio.tick(10) #10 quadros por segundo    

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()        