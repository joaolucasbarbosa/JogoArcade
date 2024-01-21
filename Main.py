import pygame, sys
import pygame.mixer
from button import Button
from slider import Slider


#criar em assets as cores
white = (255,255,255)

pygame.init()

pygame.mixer.init()

pygame.mixer.music.load("assets\\arcade-171561.wav")

is_sound_enabled = True
is_hard_mode = False 

width = 1280
height = 720
SCREEN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Menu")


pygame.mixer.music.set_volume(0.2)  # Ajuste o volume conforme necessário
pygame.mixer.music.play(-1)  # -1 indica looping infinito

BG = pygame.image.load("assets/Background.png")

player_width, player_height = 50, 50
player_char = pygame.Rect(width // 2 - player_width // 2,height // 2 - player_height // 2,player_width,player_height)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play(is_hard_mode):
    paused = False
    counter = 0
    
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        
       
        
        counter_text = get_font(25).render(f"Score: {counter:03}", True, "White")
        counter_rect = counter_text.get_rect(topleft=(10, 10))
        SCREEN.blit(counter_text, counter_rect)
        
        
        ###Player Render & Movement by:Lucca
        ##Player Render
        pygame.draw.rect(SCREEN, white, player_char)
        ##Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_char.move_ip(0,-1)
        elif keys[pygame.K_a]:
            player_char.move_ip(-1,0)
        elif keys[pygame.K_s]:
            player_char.move_ip(0,1)
        elif keys[pygame.K_d]:
            player_char.move_ip(1,0)

        if not paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            # Incrementa o contador quando a barra de espaço é pressionada
                            counter += 1 
                

                        
        else:
            # Se o jogo estiver pausado, exiba a tela de pausa
            pause_overlay = pygame.Surface((1280, 720), pygame.SRCALPHA)
            pygame.draw.rect(pause_overlay, (128, 128, 128, 128), pause_overlay.get_rect())

            resume_button = Button(image=None, pos=(640, 260), 
                                    text_input="Resume", font=get_font(50), base_color="White", hovering_color="Green")
            resume_button.changeColor(PLAY_MOUSE_POS)
            resume_button.update(pause_overlay)

            menu_button = Button(image=None, pos=(640, 360), 
                                    text_input="Return to Menu", font=get_font(50), base_color="White", hovering_color="Green")
            menu_button.changeColor(PLAY_MOUSE_POS)
            menu_button.update(pause_overlay)
            
            SCREEN.blit(pause_overlay, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if resume_button.checkForInput(PLAY_MOUSE_POS):
                        paused = False
                    elif menu_button.checkForInput(PLAY_MOUSE_POS):
                        main_menu()
         
              
            
        pygame.display.update()
    
def options():
    
    global is_sound_enabled
    global is_hard_mode
    global volume
    
    volume_slider = Slider(pos=(830, 357), width=200, height=20, min_value=0, max_value=1, initial_value=pygame.mixer.music.get_volume())
    
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(45).render("Settings", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        
        SLIDER_TEXT = get_font(40).render("Adjust Volume:", True, "Black")
        SLIDER_RECT = SLIDER_TEXT.get_rect(center=(530, 370))
        SCREEN.blit(SLIDER_TEXT, SLIDER_RECT)
        
        
        #Definição dos botões

        OPTIONS_BACK = Button(image=None, pos=(640, 650), 
                            text_input="BACK", font=get_font(40), base_color="Black", hovering_color="Green")
        
        SOUND_BUTTON = Button(image=None, pos=(640, 250),
                             text_input="Sound: ON" if is_sound_enabled else "Sound: OFF",
                             font=get_font(40), base_color="Black", hovering_color="Green")

        DIFFICULTY_BUTTON = Button(image=None, pos=(640, 490),
                             text_input=f"Set Difficulty: {'Hard' if is_hard_mode else 'Easy'}", 
                             font=get_font(40), base_color="Black", hovering_color="Green")

        
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        
        SOUND_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        SOUND_BUTTON.update(SCREEN)
        
        DIFFICULTY_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        DIFFICULTY_BUTTON.update(SCREEN)
        

        #Eventos da tela

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
                elif SOUND_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    is_sound_enabled = not is_sound_enabled
                    SOUND_BUTTON.text_input = "Sound: ON" if is_sound_enabled else "Sound: OFF"
                    if is_sound_enabled:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                elif DIFFICULTY_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    is_hard_mode = not is_hard_mode
                    DIFFICULTY_BUTTON.text_input = f"Set Difficulty: {'Hard' if is_hard_mode else 'Easy/Medium'}"
                    print("Difficulty set to:", 'Hard' if is_hard_mode else 'Easy/Medium')
                 
            volume_slider.handle_event(event)              

        volume_slider.update(SCREEN)

        pygame.display.update()

def customize():

    while True:
        SCREEN.blit(BG, (0, 0))

        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(45).render("Customize Ship", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        BACK_BUTTON = Button(image=None, pos=(640, 650), 
        text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")

        BACK_BUTTON.changeColor(PLAY_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Incrementa o contador quando a barra de espaço é pressionada
                        counter += 1 

        pygame.display.update()

def main_menu():
    global is_sound_enabled
    global is_hard_mode
    
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(45).render("Luis Inacio Lula da Silva", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=None, pos=(640, 250), 
                            text_input="PLAY", font=get_font(55), base_color="#d7fcd4", hovering_color="Green")
        CUSTOMIZE_BUTTON = Button(image=None, pos=(640, 350), 
                            text_input="CUSTOMIZE", font=get_font(55), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_BUTTON = Button(image=None, pos=(640, 450), 
                            text_input="OPTIONS", font=get_font(55), base_color="#d7fcd4", hovering_color="Green")
        QUIT_BUTTON = Button(image=None, pos=(640, 650), 
                            text_input="QUIT", font=get_font(55), base_color="#d7fcd4", hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON, CUSTOMIZE_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play(is_hard_mode)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if CUSTOMIZE_BUTTON.checkForInput(MENU_MOUSE_POS):
                    customize()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

    # Verifica se o estado do som foi alterado e para a música se necessário
        if is_sound_enabled:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()


        pygame.display.update()

main_menu()