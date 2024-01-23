import pygame

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
ORANGE = (182, 143, 64)

# Configurações da tela
WIDTH = 1280
HEIGHT = 720
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 30

# Arquivos de recursos
BACKGROUND_PLAY = "assets/Background_Play.png"
BACKGROUND_MENU = "assets/Background_Menu.png"
FONT_FILE = "assets/font.ttf"
MUSIC_FILE = "assets/arcade-171561.wav"

# Variaveis globais
is_sound_enabled = True
is_hard_mode = False 
player_width, player_height = 50, 50


### setup do player
player_width = 50
player_height = 50
player_x = (WIDTH - 50) // 2
player_y = (HEIGHT - 50) // 1.25
player_color = (255, 0, 0)
player = pygame.Rect(player_x, player_y, player_width, player_height)
player_speed = 5

### setup do projetil
projeteis = []
projetil_width = 5
projetil_height = 20
projetil_color = (0, 255, 0)
projetil_speed = 10

#funções globais
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)