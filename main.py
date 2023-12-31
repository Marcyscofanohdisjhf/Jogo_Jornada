import pygame
import sys

# Inicialização do Pygame
pygame.init()

#dimensões da tela
largura, altura = 900, 700
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo")

# Cores
preto = (0, 0, 0)
branco = (255, 255, 255)
cinza = (169, 169, 169)
azul_ciano = (173 , 216, 230)
cor_transparente = (0, 0, 0, 128)  # Adiciona transparência para a cor preta

#desenhar as serras que ficarão nas laterias
imagem_serras_paredes_1 = [
    pygame.image.load("Big Disc/sprite_0.png"),
    pygame.image.load("Big Disc/sprite_1.png"),
    pygame.image.load("Big Disc/sprite_2.png"),
    pygame.image.load("Big Disc/sprite_3.png"),
    pygame.image.load("Big Disc/sprite_4.png"),
    pygame.image.load("Big Disc/sprite_5.png"),
    pygame.image.load("Big Disc/sprite_6.png"),
    pygame.image.load("Big Disc/sprite_7.png")
]
imagem_serras_paredes_1 = [
    pygame.transform.scale(pygame.image.load(f"Big Disc/sprite_{i}.png"), (110, 110))
    for i in range(8)
]
indice_serra_atual_1 = 0
tempo_entre_frames_serra_1 = 50
posicao_x_serra_1 = 2
posicao_y_serra_1 = 2
velocidade_serra_1 = 2
tempo_anterior_serra_1 = pygame.time.get_ticks()

imagem_serras_paredes_2 = [
    pygame.image.load("Big Disc/sprite_0.png"),
    pygame.image.load("Big Disc/sprite_1.png"),
    pygame.image.load("Big Disc/sprite_2.png"),
    pygame.image.load("Big Disc/sprite_3.png"),
    pygame.image.load("Big Disc/sprite_4.png"),
    pygame.image.load("Big Disc/sprite_5.png"),
    pygame.image.load("Big Disc/sprite_6.png"),
    pygame.image.load("Big Disc/sprite_7.png")
]
imagem_serras_paredes_2 = [
    pygame.transform.scale(pygame.image.load(f"Big Disc/sprite_{i}.png"), (110, 110))
    for i in range(8)
]
indice_serra_atual_2 = 0
tempo_entre_frames_serra_2 = 50
posicao_x_serra_2 = 790
posicao_y_serra_2 = 595
velocidade_serra_2 = 2
tempo_anterior_serra_2 = pygame.time.get_ticks()

# Imagem de fundo do menu
imagem_plano_de_fundo = pygame.image.load("plano_fundo_menu.png")
imagem_plano_de_fundo = pygame.transform.scale(imagem_plano_de_fundo,(largura,altura))

# imagem de fundo do botao "controles"
imagem_controles = pygame.image.load("plano_fundo_botao_controles.jpg")
imagem_controles = pygame.transform.scale(imagem_controles, (largura, altura))

#imagens de fundo para o jogo com logica das fases
imagem_jogo_1 = pygame.image.load("Nivel 1.png")
imagem_jogo_1 = pygame.transform.scale(imagem_jogo_1, (largura, altura))
imagem_jogo_2 = pygame.image.load("Nivel 2.png")
imagem_jogo_2 = pygame.transform.scale(imagem_jogo_2, (largura, altura))
imagem_jogo_3 = pygame.image.load("Nivel 3.png")
imagem_jogo_3 = pygame.transform.scale(imagem_jogo_3, (largura, altura))
imagem_fundo = imagem_jogo_1

# imagem do personagem
personagem_imagem = pygame.image.load("player sprites/personagem_normal.png")
personagem_imagem = pygame.transform.scale(personagem_imagem,(56,70))
#posiçao inicial do personagem
personagem_x = largura / 2 - 50
personagem_y = altura / 2 - 50
velocidade_personagem = 2
personagem_costas = pygame.image.load("player sprites/personagem_costas.png")
personagem_costas = pygame.transform.scale(personagem_costas,(56,70))
personagem_direita = pygame.image.load("player sprites/personagem_direita.png")
personagem_direita = pygame.transform.scale(personagem_direita,(56,70))
personagem_esquerda = pygame.image.load("player sprites/personagem_esquerda.png")
personagem_esquerda = pygame.transform.scale(personagem_esquerda,(56,70))

sprites_andando_cima = [
    pygame.image.load("player sprites/cima/Player_07.png"),
    pygame.image.load("player sprites/cima/Player_08.png"),
    pygame.image.load("player sprites/cima/Player_09.png")
]

sprites_andando_baixo = [
    pygame.image.load("player sprites/baixo/Player_04.png"),
    pygame.image.load("player sprites/baixo/Player_05.png"),
    pygame.image.load("player sprites/baixo/Player_06.png")
]

sprites_andando_direito = [
    pygame.image.load("player sprites/direita/Player_13.png"),
    pygame.image.load("player sprites/direita/Player_14.png"),
    pygame.image.load("player sprites/direita/Player_15.png")
]

sprites_andando_esquerdo = [
    pygame.image.load("player sprites/esquerda/Player_10.png"),
    pygame.image.load("player sprites/esquerda/Player_11.png"),
    pygame.image.load("player sprites/esquerda/Player_12.png")
]
indice_sprite_atual = 0
tempo_entre_frames = 10

# Variável para armazenar a última direção do personagem
ultima_direcao = None

# Estado do jogo
ESTADO_MENU_PRINCIPAL = "menu_principal"
ESTADO_CONTROLES = "controles"
ESTADO_JOGO = "jogo"
ESTADO_PAUSA = "pausa"
ESTADO_RETORNAR_MENU = "retornar_menu"
estado_atual = ESTADO_MENU_PRINCIPAL

#estado do personagem
DIRECAO_PARADO = "parado"
DIRECAO_CIMA = "cima"
DIRECAO_BAIXO = "baixo"
DIRECAO_ESQUERDA = "esquerda"
DIRECAO_DIREITA = "direita"
direcao_atual = DIRECAO_PARADO

#imagens das setas de controle
setas_imagem = pygame.image.load("setas_botao_controles.png")
setas_imagem = pygame.transform.scale(setas_imagem,(290,200))

# Lista para armazenar as informações da seta, posicao que elas vão ficar
setas = [{"imagem": setas_imagem, "x": 130, "y": 100}]

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

# Função para criar botões
def criar_botao(texto, x, y, largura, altura, cor_normal, cor_destaque, acao):
    texto_obj, texto_rect = criar_texto(texto, 36, preto, x + largura / 2, y + altura / 2)
    retangulo = pygame.Rect(x, y, largura, altura)
    cor_atual = cor_normal

    if mouse_sobre_retângulo(retangulo):
        cor_atual = cor_destaque
        for evento in pygame.event.get():
            if evento.type == pygame.MOUSEBUTTONDOWN:
                acao()

    pygame.draw.rect(tela, cor_atual, retangulo)
    tela.blit(texto_obj, texto_rect)

# Funções para ação dos botões
def iniciar_jogo():
    print("Iniciando jogo...")
    global estado_atual
    estado_atual = ESTADO_JOGO
    jogo_iniciado = True

#botao para acessar os controles
def controles():
    print("Mostrando controles...")
    global estado_atual
    estado_atual = ESTADO_CONTROLES

#botao para sair do jogo
def sair_do_jogo():
    pygame.quit()
    sys.exit()

def pausar_jogo():
    global estado_atual
    estado_atual = ESTADO_PAUSA

def retornar_ao_menu():
    global estado_atual
    estado_atual = ESTADO_MENU_PRINCIPAL

def animar_serra_no_retangulo_1():
    global posicao_x_serra_1, posicao_y_serra_1
    global indice_serra_atual_1, tempo_anterior_serra_1
    global velocidade_serra_1

    # Defina as coordenadas do retângulo
    retangulo_esquerdo = 2
    retangulo_direito = 790
    retangulo_superior = 2
    retangulo_inferior = 590

    # Atualiza o índice da sprite da primeira serra
    if pygame.time.get_ticks() - tempo_anterior_serra_1 > tempo_entre_frames_serra_1:
        indice_serra_atual_1 = (indice_serra_atual_1 + 1) % len(imagem_serras_paredes_1)
        tempo_anterior_serra_1 = pygame.time.get_ticks()

    # Move a serra dentro do retângulo
    if posicao_x_serra_1 < retangulo_direito and posicao_y_serra_1 == retangulo_superior:
        # Move para a direita até o limite direito
        posicao_x_serra_1 += velocidade_serra_1
    elif posicao_x_serra_1 == retangulo_direito and posicao_y_serra_1 < retangulo_inferior:
        # Move para baixo até o limite inferior
        posicao_y_serra_1 += velocidade_serra_1
    elif posicao_x_serra_1 > retangulo_esquerdo and posicao_y_serra_1 == retangulo_inferior:
        # Move para a esquerda até o limite esquerdo
        posicao_x_serra_1 -= velocidade_serra_1
    elif posicao_x_serra_1 == retangulo_esquerdo and posicao_y_serra_1 > retangulo_superior:
        # Move para cima até o limite superior
        posicao_y_serra_1 -= velocidade_serra_1

    # Renderiza a sprite da primeira serra na tela
    tela.blit(imagem_serras_paredes_1[indice_serra_atual_1], (posicao_x_serra_1, posicao_y_serra_1))

def animar_serra_no_retangulo_2():
    global posicao_x_serra_2, posicao_y_serra_2
    global indice_serra_atual_2, tempo_anterior_serra_2
    global velocidade_serra_2

    # Defina as coordenadas do retângulo
    retangulo_esquerdo_2 = 2
    retangulo_direito_2 = 790
    retangulo_superior_2 = 3
    retangulo_inferior_2 = 595

    # Atualiza o índice da sprite da segunda serra
    if pygame.time.get_ticks() - tempo_anterior_serra_2 > tempo_entre_frames_serra_2:
        indice_serra_atual_2 = (indice_serra_atual_2 + 1) % len(imagem_serras_paredes_2)
        tempo_anterior_serra_2 = pygame.time.get_ticks()

    # Move a serra_2 dentro do retângulo
    if posicao_x_serra_2 > retangulo_esquerdo_2 and posicao_y_serra_2 == retangulo_inferior_2:
        # Move para a esquerda até o limite esquerdo
        posicao_x_serra_2 -= velocidade_serra_2
    elif posicao_x_serra_2 == retangulo_esquerdo_2 and posicao_y_serra_2 > retangulo_superior_2:
        # Move para cima até o limite superior
        posicao_y_serra_2 -= velocidade_serra_2
    elif posicao_x_serra_2 < retangulo_direito_2 and posicao_y_serra_2 == retangulo_superior_2:
        # Move para a direita até o limite direito
        posicao_x_serra_2 += velocidade_serra_2
    elif posicao_x_serra_2 == retangulo_direito_2 and posicao_y_serra_2 < retangulo_inferior_2:
        # Move para baixo até o limite inferior
        posicao_y_serra_2 += velocidade_serra_2

    # Renderiza a sprite da segunda serra na tela
    tela.blit(imagem_serras_paredes_2[indice_serra_atual_2], (posicao_x_serra_2, posicao_y_serra_2))

# Função para mostrar a tela de controles
def mostrar_tela_controles():
    while estado_atual == ESTADO_CONTROLES:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Desenhar a tela de controles com o plano de fundo
        tela.blit(imagem_controles, (0, 0))

        # Desenha as setas na tela
        for seta in setas:
            tela.blit(seta["imagem"], (seta["x"], seta["y"]))

        #texto dentro do botao controles
        texto_instrucao = "Pressione as setas para movimentar-se."
        texto_obj, texto_rect = criar_texto(texto_instrucao, 38, preto, 290, 50)
        tela.blit(texto_obj, texto_rect)

        #usa a funcao para criar um novo botao para retornar ao menu
        criar_botao("Voltar ao Menu", 150, 600, 200, 50, cinza, branco, voltar_ao_menu)

        pygame.display.flip()

def andando(teclas):
    if(teclas[pygame.K_w] or teclas[pygame.K_s] or teclas[pygame.K_a] or teclas[pygame.K_d]):
        return True
    else:
        return False

#varificação das colisoes do personagem com os limites do jogo
def verificar_colisao():
    global personagem_x, personagem_y, posicao_x_serra, posicao_y_serra

    # Limites da tela
    limite_esquerdo = 53
    limite_direito = 790
    limite_superior = 47
    limite_inferior = 590

    # Verifica e corrige a posição do personagem se estiver fora dos limites
    if personagem_x < limite_esquerdo:
        personagem_x = limite_esquerdo
    elif personagem_x > limite_direito:
        personagem_x = limite_direito

    if personagem_y < limite_superior:
        personagem_y = limite_superior
    elif personagem_y > limite_inferior:
        personagem_y = limite_inferior

movimento_ativo = False
# Função para mostrar a tela do jogo
def mostrar_tela_jogo():
    global personagem_x, personagem_y, indice_sprite_atual, direcao_atual, ultima_direcao,movimento_ativo

    # Movimentação do personagem com as teclas WASD
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_w]:
        personagem_y -= velocidade_personagem
        direcao_atual = DIRECAO_CIMA
        movimento_ativo = True
    if teclas[pygame.K_s]:
        personagem_y += velocidade_personagem
        direcao_atual = DIRECAO_BAIXO
        movimento_ativo = True
    if teclas[pygame.K_a]:
        personagem_x -= velocidade_personagem
        direcao_atual = DIRECAO_ESQUERDA
        movimento_ativo = True
    if teclas[pygame.K_d]:
        personagem_x += velocidade_personagem
        direcao_atual = DIRECAO_DIREITA
        movimento_ativo = True

    # Atualiza a última direção ao mover
    if direcao_atual:
        ultima_direcao = direcao_atual

    # Atualiza a animação
    if movimento_ativo:
        atualizar_animacao(obter_lista_sprites())

    # Verifica se todas as teclas de movimento estão soltas
    if not (teclas[pygame.K_w] or teclas[pygame.K_s] or teclas[pygame.K_a] or teclas[pygame.K_d]):
        movimento_ativo = False

    if teclas[pygame.K_ESCAPE]:
        pausar_jogo()

    # Desenhar a tela do jogo
    tela.blit(imagem_jogo_1, (0, 0))
    # Renderizar a sprite da serra girando
    animar_serra_no_retangulo_1()
    animar_serra_no_retangulo_2()

    # Renderizar a sprite do personagem no meio da tela
    if 0 <= indice_sprite_atual < len(obter_lista_sprites()):
        sprite_atual = pygame.transform.scale(obter_lista_sprites()[indice_sprite_atual], (56, 70))
        if andando(teclas):
            tela.blit(sprite_atual, (personagem_x, personagem_y))
        else:
            tela.blit(obter_sprite_parado(), (personagem_x, personagem_y))
    elif ultima_direcao:
        # Se a direção atual não estiver definida, use a última direção
        tela.blit(obter_sprite_parado(), (personagem_x, personagem_y))

    pygame.display.flip()

def obter_lista_sprites():
    # Retorna a lista de sprites com base na última direção
    if ultima_direcao == DIRECAO_CIMA:
        return sprites_andando_cima
    elif ultima_direcao == DIRECAO_BAIXO:
        return sprites_andando_baixo
    elif ultima_direcao == DIRECAO_ESQUERDA:
        return sprites_andando_esquerdo
    elif ultima_direcao == DIRECAO_DIREITA:
        return sprites_andando_direito
    else:
        return [personagem_imagem]

def obter_sprite_parado():
    # Retorna a sprite fixa com base na última direção
    if ultima_direcao == DIRECAO_CIMA:
        return personagem_costas
    elif ultima_direcao == DIRECAO_BAIXO:
        return personagem_imagem
    elif ultima_direcao == DIRECAO_ESQUERDA:
        return personagem_esquerda
    elif ultima_direcao == DIRECAO_DIREITA:
        return personagem_direita
    else:
        return personagem_imagem

def atualizar_animacao(lista_sprites):
    global indice_sprite_atual

    # Atualiza o índice da sprite a cada tempo_entre_frames quadros
    if pygame.time.get_ticks() % tempo_entre_frames == 0:
        indice_sprite_atual = (indice_sprite_atual + 1) % len(lista_sprites)

# Função para pausar o jogo
def mostrar_tela_pausa():
    while estado_atual == ESTADO_PAUSA:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Desenha a imagem de fundo escurecida
        tela.blit(imagem_jogo_1, (0, 0))
        superficie_transparente = pygame.Surface((largura, altura), pygame.SRCALPHA)
        superficie_transparente.fill(cor_transparente)
        tela.blit(superficie_transparente, (0, 0))

        # Renderizar o retângulo indicando "Jogo Pausado" e as opções
        pygame.draw.rect(tela, azul_ciano, (250, 200, 400, 350))
        texto_pausado, texto_pausado_rect = criar_texto("Jogo Pausado", 48, preto, largura // 2, altura // 3)
        tela.blit(texto_pausado, texto_pausado_rect)

        # Calcula o posicionamento central dos botões
        botao_width = largura // 3
        botao_height = 40
        centro_x = largura // 2 - botao_width // 2
        centro_y = altura // 2 - botao_height // 2

        # Criar botões de pausa
        criar_botao("Retornar ao Jogo", centro_x, centro_y, botao_width, botao_height, cinza, branco,despausar_jogo)
        criar_botao("Recomeçar o Jogo", centro_x, centro_y + 50, botao_width, botao_height, cinza, branco,reiniciar_jogo)
        criar_botao("Voltar ao Menu", centro_x, centro_y + 100, botao_width, botao_height, cinza, branco,voltar_ao_menu)
        criar_botao("Sair", centro_x, centro_y + 150, botao_width, botao_height, cinza, branco, sair_do_jogo)

        pygame.display.flip()

def mostrar_tela_fim_de_jogo():
    global estado_atual

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tela.fill(preto)  # Preenche a tela com a cor preta

        # Exibe a mensagem de fim de jogo
        fonte = pygame.font.SysFont(None, 50)
        mensagem = fonte.render("Fim de Jogo", True, branco)
        tela.blit(mensagem, (largura / 2 - mensagem.get_width() / 2, altura / 4))

        # Adiciona botões
        criar_botao("Recomeçar", 120, 400, 200, 50, cinza, branco, reiniciar_jogo)
        criar_botao("Menu Principal", 120, 500, 200, 50, cinza, branco, voltar_ao_menu)
        criar_botao("Fechar Jogo", 120, 600, 200, 50, cinza, branco, sair_do_jogo)

        pygame.display.flip()

# Função para reiniciar o jogo
def reiniciar_jogo():
    global personagem_x, personagem_y
    personagem_x = largura / 2 - 50
    personagem_y = altura / 2 - 50
    despausar_jogo()

# Função para despausar o jogo
def despausar_jogo():
    global estado_atual
    estado_atual = ESTADO_JOGO

# Função para voltar ao menu
def voltar_ao_menu():
    global estado_atual
    estado_atual = ESTADO_MENU_PRINCIPAL

def reiniciar_jogo():
    global personagem_x, personagem_y
    personagem_x = largura // 2 - 50
    personagem_y = altura // 2 - 50
    despausar_jogo()

def retornar_ao_menu():
    global estado_atual
    estado_atual = ESTADO_MENU_PRINCIPAL

# Função para verificar a colisão entre o personagem e uma serra
def verificar_colisao_cerra_personagem():
    global personagem_x, personagem_y, posicao_x_serra_1, posicao_y_serra_1, posicao_x_serra_2, posicao_y_serra_2

    # Áreas retangulares ocupadas pelo personagem e pela serra
    retangulo_personagem = pygame.Rect(personagem_x, personagem_y, 48, 63)
    retangulo_serra_1 = pygame.Rect(posicao_x_serra_1, posicao_y_serra_1, 110, 100)
    retangulo_serra_2 = pygame.Rect(posicao_x_serra_2, posicao_y_serra_2, 110, 110)

    # Verifica a colisão com a serra 1
    if retangulo_personagem.colliderect(retangulo_serra_1):
        mostrar_tela_fim_de_jogo()

    # Verifica a colisão com a serra 2
    if retangulo_personagem.colliderect(retangulo_serra_2):
        mostrar_tela_fim_de_jogo()

jogo_iniciado = False
executando_jogo = True
# Loop principal
while executando_jogo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando_jogo = False

    # Lógica de colisão
    verificar_colisao()
    verificar_colisao_cerra_personagem()
    # Desenhar a imagem de fundo
    if estado_atual == ESTADO_MENU_PRINCIPAL:
        tela.blit(imagem_plano_de_fundo, (0, 0))
    elif estado_atual == ESTADO_CONTROLES:
        tela.blit(imagem_controles, (0, 0))
    elif estado_atual == ESTADO_JOGO:
        mostrar_tela_jogo()
    elif estado_atual == ESTADO_PAUSA:
        mostrar_tela_pausa()
    # Lógica do estado do jogo
    if estado_atual == ESTADO_MENU_PRINCIPAL:
        # Criar botões do menu principal
        criar_botao("Iniciar Jogo", 120, 300, 200, 50, cinza, branco, iniciar_jogo)
        criar_botao("Controles", 120, 400, 200, 50, cinza, branco, controles)
        criar_botao("Sair do Jogo", 120, 500, 200, 50, cinza, branco, sair_do_jogo)
    elif estado_atual == ESTADO_CONTROLES:
        # Mostrar tela de controles
        mostrar_tela_controles()

    pygame.display.flip()
# Finaliza o pygame e sai do programa
pygame.quit()
sys.exit()