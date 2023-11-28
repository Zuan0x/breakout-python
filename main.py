# main.py
import pygame
from ball import Ball
from paddle import Paddle
from brick import Brick

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout Game")

# Set up the colors
bg_color = (255, 255, 255)
ball_color = (0, 0, 255)
paddle_color = (255, 0, 0)
brick_color = (0, 255, 0)

# Set up the game objects
ball = Ball(width // 2, height // 2, 10, ball_color)
paddle = Paddle(width // 2 - 50, height - 20, 100, 10, paddle_color)

bricks = []
brick_width = 80
brick_height = 20
for i in range(5):
    for j in range(8):
        brick = Brick(j * brick_width + 20, i * brick_height + 50, brick_width, brick_height, brick_color)
        bricks.append(brick)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.x > 0:
        paddle.move_left()
    if keys[pygame.K_RIGHT] and paddle.x < width - paddle.width:
        paddle.move_right()

    # Move the ball
    ball.move()

    # Check for collisions with walls
    if ball.x - ball.radius <= 0 or ball.x + ball.radius >= width:
        ball.dx *= -1
    if ball.y - ball.radius <= 0:
        ball.dy *= -1

    # Check for collisions with paddle
    if (
        paddle.x <= ball.x <= paddle.x + paddle.width
        and paddle.y <= ball.y + ball.radius <= paddle.y + paddle.height
    ):
        ball.dy *= -1

    # Check for collisions with bricks
    for brick in bricks:
        if (
            brick.is_visible
            and brick.x <= ball.x <= brick.x + brick.width
            and brick.y <= ball.y + ball.radius <= brick.y + brick.height
        ):
            brick.is_visible = False
            ball.dy *= -1

    # Draw everything
    screen.fill(bg_color)
    ball.draw(screen)
    paddle.draw(screen)
    for brick in bricks:
        brick.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()