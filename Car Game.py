import pygame
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

scr_width = 800
scr_height = 500
scr = pygame.display.set_mode((scr_width, scr_height))

clk = pygame.time.Clock()

dino_img = pygame.image.load('car.png').convert()


def Car(x, y):
    scr.blit(dino_img, (x, y))


font = pygame.font.SysFont('Times new Roman', 100)


def Crash_text(text, color):
    scr_text = font.render(text, True, color)
    text_width = int(scr_width * 0.23)
    text_height = int(scr_height * 0.3)
    scr.blit(scr_text, [text_width, text_height])


font2 = pygame.font.SysFont('Times new Roman', 25)


def Crash_text2(text, color):
    scr_text = font2.render(text, True, color)
    text_width = int(scr_width * 0.23)
    text_height = int(scr_height * 0.49)
    scr.blit(scr_text, [text_width, text_height])


def Blocks(blockX, blockY, blockW, blockH, color):
    pygame.draw.rect(scr, color, [blockX, blockY, blockW, blockH])


def game_loop():
    x = (scr_width - 750)
    y = (scr_height - 250)
    FPS = 40

    y_move = 0

    block_startX = scr_width
    block_startY = random.randrange(0, scr_height - 50)
    block_speed = -20
    block_width = 100
    block_height = 60

    game_quit = False
    game_Over = False
    while not game_quit:
        while game_Over == True:
            Crash_text("You Crashed", red)
            Crash_text2("Press \n'ESC' To Exit And Press \n'SPACE' To Retry", white)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_Over = False
                    game_quit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_Over = False
                        game_quit = True

                    if event.key == pygame.K_SPACE:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = - 15

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move += 15

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_move = + 15

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    y_move -= 15

        y += y_move

        scr.fill(black)

        Blocks(block_startX, block_startY, block_width, block_height, white)
        block_startX += block_speed
        Car(x, y)

        if y > scr_height - 60 or y < 0:
            game_Over = True

        if block_startX < 0:
            block_startX = scr_width
            block_startY = random.randrange(0, scr_height - 50)

        if block_startY == y:
            print("jjhjhj")

        pygame.display.flip()
        clk.tick(FPS)


game_loop()
pygame.quit()
quit()
