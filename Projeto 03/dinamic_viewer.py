import pygame
import pygame_gui
from settings import *

def dinamic_viewer(train_1, train_2, train_3, train_4):

    # Inicialização do Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Trens com Threads")

    # Gerenciador de interface gráfica do pygame_gui
    gui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Criação dos sliders de velocidade
    slider_1_rect = pygame.Rect(480, 320, 200, 15)
    slider_1 = pygame_gui.elements.UIHorizontalSlider(slider_1_rect, 20.0, (1.0, 100.0), manager=gui_manager)

    slider_2_rect = pygame.Rect(480, 340, 200, 15)
    slider_2 = pygame_gui.elements.UIHorizontalSlider(slider_2_rect, 20.0, (1.0, 100.0), manager=gui_manager)

    slider_3_rect = pygame.Rect(480, 360, 200, 15)
    slider_3 = pygame_gui.elements.UIHorizontalSlider(slider_3_rect, 20.0, (1.0, 100.0), manager=gui_manager)

    slider_4_rect = pygame.Rect(480, 380, 200, 15)
    slider_4 = pygame_gui.elements.UIHorizontalSlider(slider_4_rect, 20.0, (1.0, 100.0), manager=gui_manager)
    
    # Definição dos trilhos
    #              T1         T2         T3          T4
    #rails_1 = [(220, 70), (390, 70), (390, 240), (220, 240)]
    #rails_2 = [(410, 70), (580, 70), (580, 240), (410, 240)]
    #rails_3 = [(220, 260), (390, 260), (390, 430), (220, 430)]
    #rails_4 = [(410, 260), (580, 260), (580, 430), (410, 430)]

    # Loop principal
    running = True
    clock = pygame.time.Clock()
    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            gui_manager.process_events(event)

        gui_manager.update(time_delta)

        # Atualiza a velocidade dos trens com base nos sliders
        train_1.setSpeed(slider_1.get_current_value())
        train_2.setSpeed(slider_2.get_current_value())
        train_3.setSpeed(slider_3.get_current_value())
        train_4.setSpeed(slider_4.get_current_value())

        screen.fill(WHITE)  # Limpa a tela
        # Quadrado com os trilhos e trens
        #pygame.draw.rect(screen, GRAY, (50,30,360,410))

        # Desenhar os trilhos
        pygame.draw.rect(screen, LIGHTGRAY, (50,30,360,170),2)#T1
        pygame.draw.rect(screen, LIGHTGRAY, (50,220,170,170),2)#T2
        pygame.draw.rect(screen, LIGHTGRAY, (240,220,170,170),2)#T3
        pygame.draw.rect(screen, LIGHTGRAY, (50,410,360,170),2)#T4

        # Desenhar os trens
        pygame.draw.rect(screen, train_1.color, (train_1.x, train_1.y, 20, 20))
        text_1 = pygame.font.SysFont("Arial", 20).render(train_1.name, True, BLACK)
        text_rect_1 = text_1.get_rect(center=(train_1.x + 10, train_1.y + 10))
        screen.blit(text_1, text_rect_1)

        pygame.draw.rect(screen, train_2.color, (train_2.x, train_2.y, 20, 20))
        text_2 = pygame.font.SysFont("Arial", 20).render(train_2.name, True, WHITE)
        text_rect_2 = text_2.get_rect(center=(train_2.x + 10, train_2.y + 10))
        screen.blit(text_2, text_rect_2)

        pygame.draw.rect(screen, train_3.color, (train_3.x, train_3.y, 20, 20))
        text_3 = pygame.font.SysFont("Arial", 20).render(train_3.name, True, BLACK)
        text_rect_3 = text_3.get_rect(center=(train_3.x + 10, train_3.y + 10))
        screen.blit(text_3, text_rect_3)

        pygame.draw.rect(screen, train_4.color, (train_4.x, train_4.y, 20, 20))
        text_4 = pygame.font.SysFont("Arial", 20).render(train_4.name, True, BLACK)
        text_rect_4 = text_4.get_rect(center=(train_4.x + 10, train_4.y + 10))
        screen.blit(text_4, text_rect_4)

        # Quadrado com as alavancas de velocidade
        pygame.draw.rect(screen, LIGHTGRAY, (430,300,270,110))

        pygame.draw.rect(screen, train_1.color, (450, 320, 15, 15))
        text_1 = pygame.font.SysFont("Arial", 12).render(train_1.name, True, BLACK)
        text_rect_1 = text_1.get_rect(center=(440, 327.5))
        screen.blit(text_1, text_rect_1)

        pygame.draw.rect(screen, train_2.color, (450, 340, 15, 15))
        text_2 = pygame.font.SysFont("Arial", 12).render(train_2.name, True, BLACK)
        text_rect_2 = text_2.get_rect(center=(440, 347.5))
        screen.blit(text_2, text_rect_2)

        pygame.draw.rect(screen, train_3.color, (450, 360, 15, 15))
        text_3 = pygame.font.SysFont("Arial", 12).render(train_3.name, True, BLACK)
        text_rect_3 = text_3.get_rect(center=(440, 367.5))
        screen.blit(text_3, text_rect_3)

        pygame.draw.rect(screen, train_4.color, (450, 380, 15, 15))
        text_4 = pygame.font.SysFont("Arial", 12).render(train_4.name, True, BLACK)
        text_rect_4 = text_4.get_rect(center=(440, 387.5))
        screen.blit(text_4, text_rect_4)

        gui_manager.draw_ui(screen)
        pygame.display.update()

    pygame.quit()