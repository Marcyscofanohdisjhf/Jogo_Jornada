import pygame
import sys
import pplay

# Inicialização do Pygame
pygame.init()

# Definir dimensões da tela
largura, altura = 900, 700
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("A Odisseia")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Carregar a imagem do personagem principal
personagem_imagem = pygame.image.load("dungeon_sheet (3).png")
personagem_imagem = pygame.transform.scale(personagem_imagem, (80, 80))
# Ajuste o tamanho conforme necessário

# Posição inicial do personagem
personagem_x = largura // 2 - personagem_imagem.get_width() // 2
personagem_y = altura // 2 - personagem_imagem.get_height() // 2
#camera_x = personagem_x - largura//2
#camera_y = personagem_y - altura//2

#velocidade do personagem
velocidade = 0.2

#colocar fundo nos botoes
retangulo_terra = pygame.image.load("retangulo_mine.png")
retangulo_terra = pygame.transform.scale(retangulo_terra, (200,120))
nuvem_titulo = pygame.image.load("nuvem_2-removebg-preview.png")
nuvem_titulo = pygame.transform.scale(nuvem_titulo, (320,220))
# Função para criar texto
def criar_texto(texto, tamanho, cor, x, y):
    fonte = pygame.font.Font(None, tamanho)
    texto_obj = fonte.render(texto, True, cor)
    texto_rect = texto_obj.get_rect()
    texto_rect.center = (x, y)
    return texto_obj, texto_rect

# Função para verificar se o mouse está sobre um retângulo
def mouse_sobre_retângulo(retangulo):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return retangulo.collidepoint(mouse_x, mouse_y)

# Definir o estado inicial do jogo
estado_jogo = "menu"  # Pode ser "menu" ou "jogando"
retangulo1 = pygame.Rect(355,285,200,50)
retangulo2 = pygame.Rect(355,365,200,50)
nuvem1 = pygame.Rect(280,50,200,50)
exibir_retangulo_mine = True
exibir_nuvem = True

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if estado_jogo == "menu":
                if mouse_sobre_retângulo(opcao1_rect):
                    print("Iniciar jogo clicando")
                    # Coloque a lógica para iniciar o jogo aqui
                    estado_jogo = "jogando"
                    exibir_retangulo_mine = False
                    exibir_nuvem = False
                elif mouse_sobre_retângulo(opcao2_rect):
                    print("Sair clicando")
                    rodando = False  # Sair do loop principal para encerrar o jogo

    # capturar teclas pressionadas
    teclas = pygame.key.get_pressed()

    if estado_jogo == "jogando":
        if teclas[pygame.K_LEFT]:
            personagem_x -= velocidade
        if teclas[pygame.K_RIGHT]:
            personagem_x += velocidade
        if teclas[pygame.K_UP]:
            personagem_y -= velocidade
        if teclas[pygame.K_DOWN]:
            personagem_y += velocidade

        if teclas[pygame.K_0]:
            estado_jogo = "menu"
            exibir_retangulo_mine = True
            exibir_nuvem = True

    #atualizar a posiçao da camera para seguir o personagem
    #camera_x = personagem_x + personagem_imagem.get_width()// 2 - largura // 2
    #camera_y = personagem_y + personagem_imagem.get_height()// 2 - altura // 2

    # Preencher a tela com a cor de fundo
    tela.fill(preto)

    if estado_jogo == "menu":
        #desenhar or etangulo se exibir retangulo for True
        if exibir_retangulo_mine:
            tela.blit(retangulo_terra, retangulo1)
            tela.blit(retangulo_terra, retangulo2)
        if exibir_nuvem:
            tela.blit(nuvem_titulo, nuvem1)

        # Desenhar o título do menu
        titulo_texto, titulo_rect = criar_texto("A Jornada", 64, preto, largura // 2, altura // 4)
        tela.blit(titulo_texto, titulo_rect)

        # Desenhar as opções do menu
        opcao1_texto, opcao1_rect = criar_texto("Iniciar Jogo", 36, branco, largura // 2, altura // 2)
        opcao2_texto, opcao2_rect = criar_texto("Sair", 36, branco, largura // 2, altura // 2 + 80)

        tela.blit(opcao1_texto, opcao1_rect)
        tela.blit(opcao2_texto, opcao2_rect)

    elif estado_jogo == "jogando":
        # Desenhar o personagem na tela
        tela.blit(personagem_imagem, (personagem_x, personagem_y))
        #tela.blit(personagem_imagem, (personagem_x - camera_x, personagem_y - camera_y))

    pygame.display.flip()

# Finalizar o Pygame e encerrar o programa
pygame.quit()
sys.exit()
