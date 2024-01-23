import pygame, sys
import pygame.mixer
from button import Button
from slider import Slider
from constants import *
from game_start import game_start

# Inicializa o módulo pygame e o módulo pygame.mixer
pygame.init()
pygame.mixer.init()

# Carrega um arquivo de música para ser reproduzido
pygame.mixer.music.load(MUSIC_FILE)
# Configura o volume da música para 20% do volume total
pygame.mixer.music.set_volume(0.2)
# Inicia a reprodução da música em um loop infinito (-1 indica looping infinito)
pygame.mixer.music.play(-1)

# Cria a janela do jogo com largura e altura especificadas
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Captura a posição do Mouse
PLAY_MOUSE_POS = pygame.mouse.get_pos()

# Define o título da janela
pygame.display.set_caption("Menu")

# Carrega uma imagem de fundo
BG = pygame.image.load(BACKGROUND_MENU)

player_char = pygame.Rect(WIDTH // 2 - player_width // 2,HEIGHT // 2 - player_height // 2,player_width,player_height)

def options_button(): #Função do botão OPTIONS
    # Configura as variáveis globais
    global is_sound_enabled
    global is_hard_mode

    # Cria um slider para ajustar o volume da música
    volume_slider = Slider(pos=(830, 357), width=200, height=20, min_value=0, max_value=1, initial_value=pygame.mixer.music.get_volume())

    # Loop principal da tela de configurações
    while True:
        # Obtém a posição do mouse
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        # Desenha a imagem de fundo
        SCREEN.blit(BG, (0, 0))

        # Renderiza o texto "Settings"
        OPTIONS_TEXT = get_font(45).render("Settings", True, WHITE)
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        # Renderiza o texto "Adjust Volume:"
        SLIDER_TEXT = get_font(40).render("Adjust Volume:", True, WHITE)
        SLIDER_RECT = SLIDER_TEXT.get_rect(center=(530, 370))
        SCREEN.blit(SLIDER_TEXT, SLIDER_RECT)
        
        # Define os botões
        OPTIONS_BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(40), base_color=WHITE, hovering_color=GREEN)
        
        SOUND_BUTTON = Button(image=None, pos=(640, 250),
                            text_input="Sound: ON" if is_sound_enabled else "Sound: OFF",
                            font=get_font(40), base_color=WHITE, hovering_color=GREEN)

        DIFFICULTY_BUTTON = Button(image=None, pos=(640, 490),
                            text_input=f"Set Difficulty: {'Hard' if is_hard_mode else 'Easy'}", 
                            font=get_font(40), base_color=WHITE, hovering_color=GREEN)
        
        # Muda a cor e atualiza os botões
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        
        SOUND_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        SOUND_BUTTON.update(SCREEN)
        
        DIFFICULTY_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        DIFFICULTY_BUTTON.update(SCREEN)
        
        # Eventos da tela
        for event in pygame.event.get():
            # Verifica se o jogo foi fechado
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Verifica se ocorreu um clique do mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                elif SOUND_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    # Inverte o estado do som e pausa ou despausa a música conforme necessário
                    is_sound_enabled = not is_sound_enabled
                    SOUND_BUTTON.text_input = "Sound: ON" if is_sound_enabled else "Sound: OFF"
                    if is_sound_enabled:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                elif DIFFICULTY_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    # Inverte o modo de dificuldade
                    is_hard_mode = not is_hard_mode
        
            # Atualiza o slider do volume
            volume_slider.handle_event(event)              

        # Atualiza o slider do volume na tela
        volume_slider.update(SCREEN)

        # Atualiza a tela
        pygame.display.update()

def customize_button(): #Função do botão CUSTOMIZE

    # Loop principal para a tela de personalização da nave
    while True:
        # Desenha a imagem de fundo
        SCREEN.blit(BG, (0, 0))

        # Obtém a posição do mouse
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        # Renderiza o texto da tela de personalização
        MENU_TEXT = get_font(45).render("Customize Ship", True, ORANGE)
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Cria o botão "BACK" para retornar ao menu principal
        BACK_BUTTON = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(40), base_color=WHITE, hovering_color=GREEN)

        # Muda a cor do botão e o atualiza na tela
        BACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        # Eventos do teclado e mouse
        for event in pygame.event.get():
            # Verifica se o jogo foi fechado
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Verifica se ocorreu um clique do mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica se o botão "BACK" foi clicado
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            
            # Verifica eventos de teclado
            if event.type == pygame.KEYDOWN:
                # Pausa o jogo quando a tecla ESC é pressionada
                if event.key == pygame.K_ESCAPE:
                    paused = True
                # Incrementa o contador quando a tecla de espaço é pressionada
                elif event.key == pygame.K_SPACE:
                    counter += 1 

        # Atualiza a tela
        pygame.display.update()

def main_menu(): #Função do MAIN MENU

    # Loop principal para a tela do menu principal do jogo
    while True:
        # Desenha a imagem de fundo
        SCREEN.blit(BG, (0, 0))

        # Obtém a posição do mouse
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # Renderiza o texto principal
        MENU_TEXT = get_font(45).render("Luis Inacio Lula da Silva", True, ORANGE)
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        # Cria botões para as opções do menu
        PLAY_BUTTON = Button(image=None, pos=(640, 250), 
                            text_input="PLAY", font=get_font(55), base_color=WHITE, hovering_color="Green")
        CUSTOMIZE_BUTTON = Button(image=None, pos=(640, 350), 
                            text_input="CUSTOMIZE", font=get_font(55), base_color=WHITE, hovering_color="Green")
        OPTIONS_BUTTON = Button(image=None, pos=(640, 450), 
                            text_input="OPTIONS", font=get_font(55), base_color=WHITE, hovering_color="Green")
        QUIT_BUTTON = Button(image=None, pos=(640, 650), 
                            text_input="QUIT", font=get_font(55), base_color=WHITE, hovering_color="Green")

        # Renderiza o texto na tela
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        # Atualiza e muda a cor dos botões caso o mouse passe por cima
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, CUSTOMIZE_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        # Eventos da tela
        for event in pygame.event.get():
            # Verifica se o jogo foi fechado
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Verifica se ocorreu um clique do mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verifica qual botão foi clicado e chama a função correspondente
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game_start(is_hard_mode)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options_button()
                if CUSTOMIZE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    customize_button()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        # Verifica se o estado do som foi alterado e pausa ou despausa a música
        if is_sound_enabled:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

        # Atualiza a tela
        pygame.display.update()
