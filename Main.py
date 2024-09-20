import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
SPEED = 10

Running = True

# Set up some colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 69, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

def random_color_generator():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


Random_Color = random_color_generator()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the snake and food
snake = [(200, 200), (220, 200), (240, 200)]
food = (400, 300)

# Set up the direction
direction = "RIGHT"

# Set up the score
score = 0

# Game loop
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
            elif event.key == pygame.K_w and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.s and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_d and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_a and direction != "LEFT":
                direction = "RIGHT"

    # Move the snake
    head = snake[-1]
    if direction == "UP":
        new_head = (head[0], head[1] - BLOCK_SIZE)
    elif direction == "DOWN":
        new_head = (head[0], head[1] + BLOCK_SIZE)
    elif direction == "LEFT":
        new_head = (head[0] - BLOCK_SIZE, head[1])
    elif direction == "RIGHT":
        new_head = (head[0] + BLOCK_SIZE, head[1])
    snake.append(new_head)

    # Check for collision with food
    if snake[-1] == food:
        score += 1
        food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
    else:
        snake.pop(0)

    # Check for collision with wall or self
    if (snake[-1][0] < 0 or snake[-1][0] >= WIDTH or
            snake[-1][1] < 0 or snake[-1][1] >= HEIGHT or
            snake[-1] in snake[:-1]):
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BLACK)
    for pos in snake:
        color = random_color_generator()  # Generate a random color for each block
        pygame.draw.rect(screen, color, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))
    text_surface = font.render('Created By Thenuja', False, WHITE)
    screen.blit(text_surface, (550, 10))
    text_surface = font.render('Use WASD or Arrow keys to move', False, WHITE)
    screen.blit(text_surface, (400, 550))
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.delay(1000 // SPEED)