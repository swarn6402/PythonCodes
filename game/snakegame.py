import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Define game constants
WIDTH, HEIGHT = 600, 600       # Window dimensions
BLOCK_SIZE = 20                # Size of each grid/block
FPS = 10                       # Frames per second (game speed)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up the clock for controlling frame rate
clock = pygame.time.Clock()

# Define colors (R, G, B)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)

# Initialize snake starting position and body segments
snake_pos = [100, 50]
snake_body = [
    [100, 50],
    [80, 50],
    [60, 50]
]

# Initial movement direction (can be 'UP', 'DOWN', 'LEFT', or 'RIGHT')
direction = 'RIGHT'
change_to = direction

# Initialize food position and spawn flag
food_pos = [
    random.randrange(0, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
    random.randrange(0, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE
]
food_spawn = True

# Initialize score
score = 0

def game_over():
    """Display Game Over screen and exit the game."""
    font = pygame.font.SysFont('arial', 50)
    game_over_surface = font.render(f'Game Over! Score: {score}', True, RED)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (WIDTH / 2, HEIGHT / 4)
    
    screen.fill(BLACK)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    pygame.time.delay(3000)  # Wait for 3 seconds before quitting
    pygame.quit()
    sys.exit()

# Main Game Loop
while True:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Handling key events for snake direction
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, ord('w')):
                change_to = 'UP'
            elif event.key in (pygame.K_DOWN, ord('s')):
                change_to = 'DOWN'
            elif event.key in (pygame.K_LEFT, ord('a')):
                change_to = 'LEFT'
            elif event.key in (pygame.K_RIGHT, ord('d')):
                change_to = 'RIGHT'

    # --- Validate Direction Change ---
    # Prevent the snake from reversing directly
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # --- Update Snake Position ---
    if direction == 'UP':
        snake_pos[1] -= BLOCK_SIZE
    elif direction == 'DOWN':
        snake_pos[1] += BLOCK_SIZE
    elif direction == 'LEFT':
        snake_pos[0] -= BLOCK_SIZE
    elif direction == 'RIGHT':
        snake_pos[0] += BLOCK_SIZE

    # Insert new position as the first segment of the snake body
    snake_body.insert(0, list(snake_pos))

    # --- Check if Snake Eats the Food ---
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False  # Food has been eaten, so respawn it
    else:
        # Remove the last segment if food not eaten
        snake_body.pop()

    # --- Food Spawn ---
    if not food_spawn:
        food_pos = [
            random.randrange(0, (WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
            random.randrange(0, (HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE
        ]
        food_spawn = True

    # --- Draw Everything on the Screen ---
    screen.fill(BLACK)  # Clear the screen with black

    # Draw snake segments
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

    # --- Collision Detection ---
    # Check if snake hits the boundaries
    if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
        snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
        game_over()

    # Check if snake hits itself (ignoring the head)
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    # --- Display the Score ---
    font = pygame.font.SysFont('arial', 20)
    score_surface = font.render('Score: ' + str(score), True, WHITE)
    screen.blit(score_surface, (10, 10))

    # Update the display
    pygame.display.update()

    # Control the game speed
    clock.tick(FPS)
