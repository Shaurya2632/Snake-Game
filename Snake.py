from Projects.Pygame.Commands import *
import random

def show_text(text, color, x, y):
    screen_text = font.render(text, True, color)
    win.blit(screen_text, [x, y])

def plot_snake():
    for x, y in snake_list:
       pygame.draw.rect(win, YELLOW, [x, y, snake_size, snake_size])

def plot_food():
    pygame.draw.rect(win, CYAN, [food_x, food_y, food_size, food_size])

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

win = setWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
setTitle("Snake")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
img = pygame.image.load(r"E:\coding\python\Images\fake_grass_Resized.jpg")
exit_ = False
game_over = False
snake_x = 35
snake_y = 35
snake_size = 12
food_x = random.randint(40, SCREEN_WIDTH-100)
food_y = random.randint(40, SCREEN_HEIGHT-100)
food_size = snake_size
fps = 25
velocity_x = 0
velocity_y = 0
game_started = False
score = 0
ran = 8
speed = 1.0

snake_list = []

snake_length = 1

while not exit_:
    for event in getEvent():
        if is_close(event.type):
            exit_ = True

        if event.type == pygame.KEYDOWN:
            game_started = True
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                velocity_x = 0
                velocity_y = -5 * speed
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                velocity_x = 0
                velocity_y = 5 * speed
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                velocity_x = 5 * speed
                velocity_y = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                velocity_x = -5 * speed
                velocity_y = 0

    if game_started:
        snake_x += velocity_x
        snake_y += velocity_y

    if snake_x > SCREEN_WIDTH:
        snake_x = 0

    if snake_y > SCREEN_HEIGHT:
        snake_y = 0

    if abs(snake_x - food_x) < ran and abs(snake_y - food_y) < ran:
        speed += .05
        food_x = random.randint(40, SCREEN_WIDTH-100)
        food_y = random.randint(40, SCREEN_HEIGHT-100)
        snake_length += 3
        score += 1

    head = [snake_x, snake_y]
    snake_list.append(head)

    if len(snake_list) > snake_length+2:
        del snake_list[0]

    if len(snake_list) > 3 and head in snake_list[:-1]:
        game_over = True

    if not 0 < snake_x < SCREEN_WIDTH or not 0 < snake_y < SCREEN_HEIGHT:
        if snake_x > SCREEN_WIDTH:
            snake_x = 0

        if snake_x < 0:
            snake_x = SCREEN_WIDTH

        if snake_y > SCREEN_HEIGHT:
            snake_y = 0

        if snake_y < 0:
            snake_y = SCREEN_HEIGHT

    if game_over:
        break

    win.blit(img, (0, 0))
    plot_snake()
    plot_food()
    show_text(f"Score: {score}", WHITE, 4, 4)

    update()
    clock.tick(fps)

pygame.quit()