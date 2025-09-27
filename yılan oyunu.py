import pygame
import random
import asyncio
import platform

# Pygame başlatma
pygame.init()

# Oyun alanı boyutları
WIDTH = 400
HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Renkler
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Yılan ve yem
class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (1, 0)
        self.length = 1

    def move(self):
        head_x, head_y = self.positions[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)
        # Duvarlardan geçme
        new_head = (new_head[0] % GRID_WIDTH, new_head[1] % GRID_HEIGHT)
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()

    def check_collision(self):
        return self.positions[0] in self.positions[1:]

    def grow(self):
        self.length += 1

class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        return (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Oyun ekranı
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yılan Oyunu")
clock = pygame.time.Clock()
FPS = 10

def setup():
    global snake, food, game_over, score
    snake = Snake()
    food = Food()
    game_over = False
    score = 0

def update_loop():
    global game_over, score
    if not game_over:
        # Yön tuşları ile kontrol
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    snake.direction = (1, 0)

        # Yılan hareketi
        snake.move()

        # Yem yeme kontrolü
        if snake.positions[0] == food.position:
            snake.grow()
            food.position = food.random_position()
            score += 1

        # Çarpışma kontrolü
        if snake.check_collision():
            game_over = True

        # Ekranı çiz
        screen.fill(BLACK)
        # Yemi çiz
        pygame.draw.rect(screen, RED, (food.position[0] * GRID_SIZE, food.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        # Yılanı çiz
        for pos in snake.positions:
            pygame.draw.rect(screen, GREEN, (pos[0] * GRID_SIZE, pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        # Skoru göster
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Skor: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        # Oyun bittiğinde mesaj
        if game_over:
            game_over_text = font.render("Oyun Bitti! Skor: " + str(score), True, WHITE)
            screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))
        pygame.display.flip()

async def main():
    setup()
    while True:
        update_loop()
        await asyncio.sleep(1.0 / FPS)

if platform.system() == "Emscripten":
    asyncio.ensure_future(main())
else:
    if __name__ == "__main__":
        asyncio.run(main())