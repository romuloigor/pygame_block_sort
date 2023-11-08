import pygame
import sys
import random

# Configurações iniciais
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game of Stacks')

# Definição de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)

# Constantes de jogo
SQUARE_SIZE = 50
SPACING = 10
BORDER_COLOR = RED
BORDER_WIDTH = 3
STATUS_BAR_HEIGHT = 50
STATUS_BAR_COLOR = BLACK

# Estado do jogo
num_squares_per_stack = 3
colors = [RED, GREEN, BLUE, YELLOW, MAGENTA]  # Lista de cores disponíveis
stacks = {}

def is_within_bounds(x, y, rect_x, rect_y):
    return rect_x < x < rect_x + SQUARE_SIZE and rect_y < y < rect_y + SQUARE_SIZE

def find_stack_with_space(exclude_stack_key):
    for stack_key, stack in stacks.items():
        if stack_key != exclude_stack_key and len(stack['colors']) < num_squares_per_stack:
            return stack_key
    return None

def draw_stacks_and_borders(mouse_x, mouse_y):
    for stack_key, stack in stacks.items():
        for i, color in enumerate(stack['colors']):
            rect_x, rect_y = stack['pos']
            rect_y += (SQUARE_SIZE + SPACING) * i
            pygame.draw.rect(screen, color, (rect_x, rect_y, SQUARE_SIZE, SQUARE_SIZE))
            if is_within_bounds(mouse_x, mouse_y, rect_x, rect_y):
                pygame.draw.rect(screen, BORDER_COLOR, (rect_x, rect_y, SQUARE_SIZE, SQUARE_SIZE), BORDER_WIDTH)

def handle_mouse_click(mouse_x, mouse_y):
    for stack_key, stack in stacks.items():
        for i in range(len(stack['colors']) - 1, -1, -1):
            rect_x, rect_y = stack['pos']
            rect_y += (SQUARE_SIZE + SPACING) * i
            if is_within_bounds(mouse_x, mouse_y, rect_x, rect_y):
                target_stack_key = find_stack_with_space(stack_key)
                if target_stack_key:
                    stacks[target_stack_key]['colors'].append(stack['colors'].pop(i))
                return

def draw_status_bar():
    y_pos = SCREEN_HEIGHT - STATUS_BAR_HEIGHT
    pygame.draw.rect(screen, STATUS_BAR_COLOR, (0, y_pos, SCREEN_WIDTH, STATUS_BAR_HEIGHT))
    level_completed = all_stacks_one_color()
    if level_completed:
        font = pygame.font.Font(None, 36)
        text = font.render('Objetivo alcançado!', True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, y_pos + STATUS_BAR_HEIGHT/2))
        screen.blit(text, text_rect)
    return level_completed

def all_stacks_one_color():
    for stack_key, stack in stacks.items():
        if stack['colors']:
            if len(stack['colors']) != num_squares_per_stack or not all(color == stack['colors'][0] for color in stack['colors']):
                return False
    return True

def setup_stacks(num_stacks=5):
    global num_squares_per_stack
    available_colors = colors[:num_stacks - 1]  # Seleciona as cores com base no número de pilhas
    initial_colors = available_colors * num_squares_per_stack  # Duplica as cores
    random.shuffle(initial_colors)  # Embaralha as cores

    stacks.clear()
    for i in range(num_stacks):
        stack_key = f'stack{i+1}'
        stacks[stack_key] = {'pos': [100 + 150 * i, 100], 'colors': initial_colors[i*num_squares_per_stack:(i+1)*num_squares_per_stack] if i < num_stacks - 1 else []}

def main_game_loop():
    global num_squares_per_stack
    num_stacks = 5
    setup_stacks(num_stacks)

    running = True
    while running:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                handle_mouse_click(mouse_x, mouse_y)

        screen.fill(WHITE)
        draw_stacks_and_borders(mouse_x, mouse_y)
        level_completed = draw_status_bar()

        pygame.display.flip()
        pygame.time.delay(30)

        if level_completed:
            pygame.time.delay(2000)  # Pausa para o jogador ver a mensagem de vitória
            num_squares_per_stack += 1  # Aumenta a dificuldade para o próximo nível
            if num_squares_per_stack > len(colors):  # Se ultrapassar o número de cores disponíveis, o jogo termina
                running = False
            else:
                setup_stacks(num_stacks)  # Reinicia as pilhas para o próximo nível

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main_game_loop()
