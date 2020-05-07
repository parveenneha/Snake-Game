import pygame
import random
import os
import pygame.mixer

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Touching_Moment.mp3')
pygame.mixer.music.play()

screen_width = 900
screen_height = 600

# background image
img = pygame.image.load("background.jpg")
img = pygame.transform.scale(img, (screen_width, screen_height))
img_snake = pygame.image.load("final_background.jpg")
img_snake = pygame.transform.scale(img_snake, (screen_width, screen_height))
img_last = pygame.image.load("image_last.png")
img_last = pygame.transform.scale(img_last, (screen_width, screen_height))

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating Window

gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title

pygame.display.set_caption("Snakes")
pygame.display.update()

# Game Specific Variables

clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [int(x), int(y)])


# def image_screen(image, x1, y1):
# screen_image = image.load(image, True)
# gameWindow.blit(screen_image, [int(x1), int(y1)])


def plot_snake(gameWindow1, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow1, color, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:

        gameWindow.fill(red)
        # image_screen("snakes.gif", 200, 280)
        gameWindow.blit(img_snake, (0, 0))

        text_screen("Snake it up!", red, 80, 150)
        text_screen("Press spacebar to continue", black, 80, 200)
    # text_screen()
        #text_screen("to continue!",black,280,200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
            pygame.display.update()
            clock.tick(60)


# Game Loop
def game():
    pygame.mixer.music.load('Touching_Moment.mp3')
    pygame.mixer.music.play()
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snake_size = 15
    score = 0
    snk_list = []
    snk_length = 1
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    fps = 20
    if not os.path.exists("HighScore.py"):
        with open("HighScore.py", "w") as f:
            f.write("0")
    with open("HighScore.py", "r") as f:
        highscore = f.read()
    while not exit_game:
        if game_over:
            with open("HighScore.py", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            gameWindow.blit(img_last, (0, 0))
            text_screen("Game Over", red, 0, 0)
            text_screen("Press                 Spacebar to play!", red, 50, 50)
            text_screen("     Score : " +str(score), black, 200, 200)


            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        welcome()
                        pygame.display.update()
                        clock.tick(60)
        else:
            for event in pygame.event.get():
                # print(event)
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
                pygame.mixer.music.load('beep.mp3')
                pygame.mixer.music.play()
       


                # print(score)
                food_x = random.randint(10, screen_width / 2)
                food_y = random.randint(10, screen_height / 2)
                snk_length += 5
                if score > int(highscore):
                    highscore = score

            gameWindow.fill(white)
            gameWindow.blit(img, (0, 0))
            text_screen("Score: " + str(score) + "  HighScore: " + str(highscore), black, 10, 10)
            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if (len(snk_list)) > snk_length:
                del snk_list[0]
                if head in snk_list[:-1]:
                    game_over = True
                    pygame.mixer.music.load('Hollywood_Traffic_Jam.mp3')
                    pygame.mixer.music.play()
                if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                    game_over = True
                    # print("Game Over")
                    pygame.mixer.music.load('Hollywood_Traffic_Jam.mp3')
                    pygame.mixer.music.play()
            pygame.draw.circle(gameWindow, red, [food_x, food_y], 10)
            plot_snake(gameWindow, black, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
