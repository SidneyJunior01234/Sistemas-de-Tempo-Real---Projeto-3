import pygame
import pygame_gui

# Dimensões da tela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Cores
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTGRAY = (211, 211, 211)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BROWN = (150, 75, 0)

def control_view(train_1, train_2, train_3, train_4):
    # Inicialização do Pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Controle dos Trens")

    # Gerenciador de interface gráfica do pygame_gui
    gui_manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Criação dos sliders de velocidade
    slider_1_rect = pygame.Rect(430, 500, 200, 15)
    slider_1 = pygame_gui.elements.UIHorizontalSlider(slider_1_rect, 50.0, (1.0, 100.0), manager=gui_manager)

    slider_2_rect = pygame.Rect(430, 520, 200, 15)
    slider_2 = pygame_gui.elements.UIHorizontalSlider(slider_2_rect, 50.0, (1.0, 100.0), manager=gui_manager)

    slider_3_rect = pygame.Rect(430, 540, 200, 15)
    slider_3 = pygame_gui.elements.UIHorizontalSlider(slider_3_rect, 50.0, (1.0, 100.0), manager=gui_manager)

    slider_4_rect = pygame.Rect(430, 560, 200, 15)
    slider_4 = pygame_gui.elements.UIHorizontalSlider(slider_4_rect, 50.0, (1.0, 100.0), manager=gui_manager)

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

        # Quadrado com as alavancas de velocidade
        pygame.draw.rect(screen, LIGHTGRAY, (430,490,270,95))

        pygame.draw.rect(screen, train_1.color, (430, 500, 15, 15))
        text_1 = pygame.font.SysFont("Arial", 12).render(train_1.name, True, BLACK)
        text_rect_1 = text_1.get_rect(center=(267.5, 507.5))
        screen.blit(text_1, text_rect_1)

        pygame.draw.rect(screen, train_2.color, (430, 520, 15, 15))
        text_2 = pygame.font.SysFont("Arial", 12).render(train_2.name, True, BLACK)
        text_rect_2 = text_2.get_rect(center=(267.5, 527.5))
        screen.blit(text_2, text_rect_2)

        pygame.draw.rect(screen, train_3.color, (430, 540, 15, 15))
        text_3 = pygame.font.SysFont("Arial", 12).render(train_3.name, True, BLACK)
        text_rect_3 = text_3.get_rect(center=(267.5, 547.5))
        screen.blit(text_3, text_rect_3)

        pygame.draw.rect(screen, train_4.color, (430, 560, 15, 15))
        text_4 = pygame.font.SysFont("Arial", 12).render(train_4.name, True, BLACK)
        text_rect_4 = text_4.get_rect(center=(267.5, 567.5))
        screen.blit(text_4, text_rect_4)

        gui_manager.draw_ui(screen)
        pygame.display.update()


pygame.quit()