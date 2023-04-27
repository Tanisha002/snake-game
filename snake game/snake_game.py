import pygame
import time
import random

pygame.init()

bg="#107332"
sc="#FF0096"
fc="#FF0000"
w,h=400,500

game_display=pygame.display.set_mode((w,h))
pygame.display.set_caption("Snake Game")

clock=pygame.time.Clock()

s_size=25
s_speed=8

mssg_font=pygame.font.SysFont('ubuntu',55)
score_font=pygame.font.SysFont('ubuntu',35)

def print_score(score):
    text=score_font.render("Score : "+ str(score), True, "#ECF8EF")
    game_display.blit(text,[10,10])


def draw_snake(snake_size,snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display,sc,[pixel[0],pixel[1],snake_size,snake_size])

def run_game():
    game_close=False
    game_over=False

    x=w/2
    y=h/2

    x_speed=0
    y_speed=0

    snake_pixels=[]
    snake_length=1

    food_x=round(random.randrange(s_size+1//2,w- s_size)/25.0)*25.0 
    food_y=round(random.randrange(s_size+1//2,h- s_size)/25.0)*25.0

    while not game_close:



        while game_over:
            game_display.fill("#292C29")
            game_mssg=mssg_font.render("GAME OVER!!!",True,"#EE192F")
            game_display.blit(game_mssg,[w/7,h/4])
            print_score(snake_length-1)
            close_mssg=score_font.render("Press 1 to Exit ",True,"#ECF8EF")
            game_display.blit(close_mssg,[w/5,h/4+60])
            restart_mssg=score_font.render("Press 2 to Play Again",True,"#ECF8EF")
            game_display.blit(restart_mssg,[w/5,h/4+100])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        # game is closed
                        game_close=True
                        game_over=False
                    if event.key ==  pygame.K_2:
                        #restart
                        run_game()
                if event.type ==pygame.QUIT:
                    game_close=True
                    game_over=False


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameover=True
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_LEFT:
                    x_speed=-s_size
                    y_speed=0
                if event.key== pygame.K_RIGHT:
                    x_speed=s_size
                    y_speed=0
                if event.key== pygame.K_UP:
                    x_speed=0
                    y_speed=-s_size
                if event.key== pygame.K_DOWN:
                    x_speed=0
                    y_speed=s_size
        if x>=w or x<0 or y>=h or y<0:
            game_over=True

        x+=x_speed
        y+=y_speed

        game_display.fill(bg)
        pygame.draw.circle(game_display,fc,[food_x,food_y],s_size/2,0)

        snake_pixels.append([x,y])
        if len(snake_pixels)>snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel==[x,y]:
                game_over=True

        draw_snake(s_size,snake_pixels)
        print_score(snake_length-1)

        pygame.display.update()

        if( x==food_x and y==food_y):
            food_x=round(random.randrange(s_size+1//2 ,w- s_size)/25.0)*25.0
            food_y=round(random.randrange(s_size+1//2 ,h- s_size)/25.0)*25.0
            snake_length+=1

        clock.tick(s_speed)

    

    pygame.quit()
    quit()


run_game()

