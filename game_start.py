import pygame, sys
import pygame.mixer
from constants import *
from button import Button

#####################################

### Carregando background
bg_play = pygame.image.load(BACKGROUND_PLAY).convert()

def game_start(is_hard_mode):
    
    paused = False
    counter = 0
    
    while True:
        
        clock.tick(FPS)

        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        SCREEN.fill("black")
        
        ### background durante o jogo
        
        
        ### contador
        counter_text = get_font(25).render(f"Score: {counter:03}", True, "White")
        counter_rect = counter_text.get_rect(topleft=(10, 10))
        SCREEN.blit(counter_text, counter_rect)
        
        ### var para tecla pressionada (permite segurar a tecla)
        press_key = pygame.key.get_pressed()
        
        ### draw player
        pygame.draw.rect(SCREEN, player_color, player) 
        
        for projetil in projeteis:
            pygame.draw.rect(SCREEN, projetil_color, projetil)       
        
        if not paused:
            
            ### atualiza o local do player
            if press_key[pygame.K_w] == True and player[1] > (HEIGHT/1.5):
                player.move_ip(0, -(player_speed))
            if press_key[pygame.K_a] == True and player[0] > 0:
                player.move_ip(-(player_speed), -0)
            if press_key[pygame.K_s] == True and player[1] < (HEIGHT-player_height):
                player.move_ip(0, (player_speed))
            if press_key[pygame.K_d] == True and player[0] < (WIDTH-player_width):
                player.move_ip((player_speed), 0)
            
            ### checa por eventos
            for event in pygame.event.get():
                
                ### event para fechar o game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                ### checa se uma tecla foi apertado (N permite segurar a tecla)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            # (TEMPORARIO) Incrementa o contador quando a barra de espaço é pressionada
                            counter += 1 
                            
                            ### desenha o projetil na tela baseado nas coords xy do player, 
                            ### o tiro deve sair no centro e um pouco acima do player 
                            projeteis.append(pygame.Rect( (player[0] + (round(player_width-projetil_width)/2)),
                                            player[1] - 20,
                                            projetil_width, projetil_height))
        
            for projetil in projeteis:
                projetil.y -= projetil_speed
                if projetil.bottom < 0:
                    projeteis.remove(projetil)
            
                        
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
                        from Menu import main_menu
                        main_menu()
                        
        pygame.display.update()