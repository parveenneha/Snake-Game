import pygame
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating Window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title

pygame.display.set_caption("Snakes")
pygame.display.update()

# Game Specific Variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
velocity_x = 0
velocity_y = 0
snake_size = 8
score = 0
food_x = random.randint(0, screen_width)
food_y = random.randint(0, screen_height)
fps = 20
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def plot_snake(gameWindow1, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow1, color, [x, y, snake_size, snake_size])


snk_list = []
snk_length = 1
# Game Loop
while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 5
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                # snake_x = snake_x - 10
                velocity_x = -5
                velocity_y = 0
            if event.key == pygame.K_UP:
                # snake_y = snake_y - 10
                velocity_y = -5
                velocity_x = 0
            if event.key == pygame.K_DOWN:
                # snake_y = snake_y + 10
                velocity_x = 0
                velocity_y = 5

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y
    if abs(snake_x - food_x) < 5 and abs(snake_y - food_y) < 5:
        score += 10
        # print(score)
        food_x = random.randint(10, screen_width / 2)
        food_y = random.randint(10, screen_height / 2)
        snk_length += 5

    gameWindow.fill(white)
    text_screen("Score: " + str(score), red, 10, 10)
    # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if (len(snk_list)) > snk_length:
        del snk_list[0]
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    plot_snake(gameWindow, black, snk_list, snake_size)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
