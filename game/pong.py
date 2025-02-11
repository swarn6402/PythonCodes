import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pong Game")

# Game clock for controlling the frame rate
clock = pygame.time.Clock()

# Define game object dimensions
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create game objects: ball and paddles
ball_rect = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
player_rect = pygame.Rect(WIDTH - PADDLE_WIDTH - 10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
opponent_rect = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball speed (pixels per frame)
ball_speed_x = 5
ball_speed_y = 5

# Paddle speed
paddle_speed = 7

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y

    # Ball collision with top or bottom of the window
    if ball_rect.top <= 0 or ball_rect.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball_rect.colliderect(player_rect) or ball_rect.colliderect(opponent_rect):
        ball_speed_x *= -1

    # Player paddle movement (using the up and down arrow keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.y -= paddle_speed
    if keys[pygame.K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect.y += paddle_speed

    # Simple AI for the opponent paddle: follows the ball's vertical position
    if opponent_rect.centery < ball_rect.centery and opponent_rect.bottom < HEIGHT:
        opponent_rect.y += paddle_speed
    if opponent_rect.centery > ball_rect.centery and opponent_rect.top > 0:
        opponent_rect.y -= paddle_speed

    # Check if the ball goes off the screen (i.e., a point is scored)
    if ball_rect.left <= 0 or ball_rect.right >= WIDTH:
        # Reset the ball to the center
        ball_rect.center = (WIDTH // 2, HEIGHT // 2)
        # Reverse the ball's horizontal direction
        ball_speed_x *= -1

    # Drawing section
    screen.fill(BLACK)  # Fill the background with black
    pygame.draw.rect(screen, WHITE, player_rect)       # Draw the player paddle
    pygame.draw.rect(screen, WHITE, opponent_rect)       # Draw the opponent paddle
    pygame.draw.ellipse(screen, WHITE, ball_rect)        # Draw the ball
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))  # Draw the center line

    # Update the display
    pygame.display.flip()

    # Control the frame rate (60 frames per second)
    clock.tick(60)
