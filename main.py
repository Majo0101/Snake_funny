import pygame
import time
import random

pygame.init()

gameOver = False
red = (255, 0, 0)
green = (0, 179, 60)
orange = (230, 92, 0)
black = (0, 26, 9)
height = 400
width = 400
snake = 5
snake_body = []
position_x = int(height/2)
position_y = int(width/2)
points = 0
x = -5
y = 0
food_x = round(random.randrange(10, 390)/5)*5
food_y = round(random.randrange(10, 390)/5)*5

display = pygame.display.set_mode((height, width))
myIcon = pygame.image.load("icon.jpg")
pygame.display.set_caption("Snake 0.1")
pygame.display.set_icon(myIcon)

font = pygame.font.SysFont('Calibri', 30)
game_time = pygame.time.Clock()


def winner_constellation():
    white = (255, 255, 255)
    rred = (255, 0, 0)
    blue = (0, 0, 255)
    global x
    global y
    global gameOver
    x = 0
    y = 0
    counter = 0
    pygame.mixer.music.load('winsong.mp3')
    pygame.mixer.music.play(-1)
    while counter < 12:
        display.fill(white)
        runtime_message('WINNER F YEAH!', black, height/2, width/5)
        pygame.display.update()
        game_time.tick(2)
        counter += 0.5
        display.fill(rred)
        runtime_message('WINNER F YEAH!', white, height/2, width/4)
        pygame.display.update()
        game_time.tick(2)
        counter += 0.5
        display.fill(blue)
        runtime_message('WINNER F YEAH!', red, height/2, width/5)
        pygame.display.update()
        game_time.tick(2)
        counter += 0.5

    gameOver = True


def score(nom_nom_nom):
    runtime_message(f'Score: {nom_nom_nom}', orange, 10, 10)


def snake_food(move_x, move_y):
    pygame.draw.rect(display, black, [move_y, move_x, snake, snake])


def snake_move(arr_in):
    display.fill(green)
    for body in arr_in:
        pygame.draw.rect(display, black, [body[0], body[1], snake, snake])


def runtime_message(text, color, pos_x, pos_y):
    message = font.render(text, True, color)
    display.blit(message, [pos_y, pos_x])


display.fill(green)
pygame.display.update()

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x = -5
                y = 0
            elif event.key == pygame.K_DOWN:
                x = 5
                y = 0
            elif event.key == pygame.K_LEFT:
                x = 0
                y = -5
            elif event.key == pygame.K_RIGHT:
                x = 0
                y = 5
            elif event.key == pygame.K_ESCAPE:
                runtime_message("You LOSE!!", red, height/2, width/3)
                pygame.display.update()
                time.sleep(1)
                gameOver = True

    if position_x < 1 or position_x > height-10 or position_y < 1 or position_y > width-10:
        runtime_message("You LOSE", red, height/2, width/3)
        pygame.display.update()
        time.sleep(2)
        gameOver = True

    position_x += x
    position_y += y
    snake_head = [position_y, position_x]
    snake_body.append(snake_head)

    snake_move(snake_body)
    snake_food(food_x, food_y)

    if len(snake_body) > points+1:
        snake_body.pop(0)

    if food_x == position_x and food_y == position_y:
        food_x = int(round(random.randrange(10, 390)/5)*5)
        food_y = int(round(random.randrange(10, 390)/5)*5)
        points += 1

    for check in snake_body[:-1]:
        if snake_head == check:
            runtime_message("You LOSE", red, height/2, width/3)
            pygame.display.update()
            time.sleep(2)
            gameOver = True

    if points == 20:
        winner_constellation()

    score(points)

    pygame.display.update()
    game_time.tick(20)

pygame.display.quit()
quit()
