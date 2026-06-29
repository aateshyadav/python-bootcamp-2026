import pygame
import random
import sys

# Game configuration
CELL_SIZE = 20
GRID_WIDTH = 20
GRID_HEIGHT = 20
WINDOW_WIDTH = GRID_WIDTH * CELL_SIZE
WINDOW_HEIGHT = GRID_HEIGHT * CELL_SIZE
FPS = 10

# Colors
COLOR_BG = (10, 10, 10)
COLOR_GRID = (40, 40, 40)
COLOR_SNAKE = (0, 255, 0)
COLOR_HEAD = (0, 200, 0)
COLOR_FOOD = (255, 50, 50)
COLOR_TEXT = (255, 255, 255)

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)


def draw_grid(surface):
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(surface, COLOR_GRID, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, COLOR_GRID, (0, y), (WINDOW_WIDTH, y))


def spawn_food(snake):
    available = [
        (x, y)
        for x in range(GRID_WIDTH)
        for y in range(GRID_HEIGHT)
        if (x, y) not in snake
    ]
    return random.choice(available) if available else None


def draw_game(surface, snake, food, score):
    surface.fill(COLOR_BG)
    draw_grid(surface)

    for segment in snake[1:]:
        rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, COLOR_SNAKE, rect)

    head = snake[0]
    head_rect = pygame.Rect(head[0] * CELL_SIZE, head[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, COLOR_HEAD, head_rect)

    if food:
        food_rect = pygame.Rect(food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, COLOR_FOOD, food_rect)

    score_text = font.render(f"Score: {score}", True, COLOR_TEXT)
    surface.blit(score_text, (10, 10))
    pygame.display.flip()


def game_over_screen(surface, score):
    surface.fill(COLOR_BG)
    text1 = font.render("Game Over", True, COLOR_TEXT)
    text2 = font.render(f"Score: {score}", True, COLOR_TEXT)
    text3 = font.render("Press R to restart or Q to quit", True, COLOR_TEXT)

    surface.blit(text1, (WINDOW_WIDTH // 2 - text1.get_width() // 2, WINDOW_HEIGHT // 2 - 60))
    surface.blit(text2, (WINDOW_WIDTH // 2 - text2.get_width() // 2, WINDOW_HEIGHT // 2 - 20))
    surface.blit(text3, (WINDOW_WIDTH // 2 - text3.get_width() // 2, WINDOW_HEIGHT // 2 + 20))
    pygame.display.flip()


def main():
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = (1, 0)
    food = spawn_food(snake)
    score = 0
    running = True
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    return main()
                if not paused:
                    if event.key == pygame.K_UP and direction != (0, 1):
                        direction = (0, -1)
                    elif event.key == pygame.K_DOWN and direction != (0, -1):
                        direction = (0, 1)
                    elif event.key == pygame.K_LEFT and direction != (1, 0):
                        direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                        direction = (1, 0)

        if paused:
            game_over_screen(window, score)
            clock.tick(FPS)
            continue

        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        if (
            new_head[0] < 0
            or new_head[0] >= GRID_WIDTH
            or new_head[1] < 0
            or new_head[1] >= GRID_HEIGHT
            or new_head in snake
        ):
            paused = True
            continue

        snake.insert(0, new_head)

        if food and new_head == food:
            score += 1
            food = spawn_food(snake)
        else:
            snake.pop()

        draw_game(window, snake, food, score)
        clock.tick(FPS)


if __name__ == "__main__":
    main()


