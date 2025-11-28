import pygame
import sys

# אתחול
pygame.init()

# הגדרות מסך
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("הכדור הקופץ")

# צבעים
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# הגדרות הכדור
ball_radius = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 4
ball_speed_y = 4

# שעון לקצב רענון
clock = pygame.time.Clock()

# לולאת המשחק
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # תזוזת הכדור
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # התנגשויות בקירות
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_speed_x *= -1
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        ball_speed_y *= -1

    # ציור
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

