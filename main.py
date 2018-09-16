"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Danny Van Stemp
ID:     181549810
Email:  vans9810@mylaurier.ca
__updated__ = "2018-07-27"
------------------------------------------------------------------------
"""

import pygame
from SnakeSegment import SnakeSegment
from Food import Food
import random
import globals
globals.init()

x_movement = 50
y_movement = 0
speed = 20
tick = 0
direction=3
direction_old = 0
moved = True
eaten_food = False
score = 0


screen = pygame.display.set_mode((globals.screen_width,globals.screen_height))
pygame.display.set_caption('Nice Window')
pygame.display.flip()

game_segments = []

def reset_game():
    global direction
    game_segments.clear()
    direction = 3
    game_segments.append(SnakeSegment(globals.grid_size*3,globals.grid_size*2,direction))
    game_segments.append(SnakeSegment(globals.grid_size*2,globals.grid_size*2,direction))
    game_segments[1].set_type(1)
    game_segments.append(SnakeSegment(globals.grid_size*1,globals.grid_size*2,direction))
    game_segments[2].set_type(1)

           
game_food=Food(random.randint(1,globals.range_x_divided)*globals.grid_size,random.randint(1,globals.range_y_divided)*globals.grid_size)
clock = pygame.time.Clock()

def update():
    global direction
    global direction_old
    global x_movement
    global y_movement
    global running
    global speed
    global tick
    global moved
    global eaten_food
    global game_food
  
    
    for event in pygame.event.get():
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 3 and moved:
                direction = 1
                moved = False
            if event.key == pygame.K_RIGHT and direction != 1 and moved:

                direction = 3
                moved = False
               
            if event.key == pygame.K_UP and direction != 4 and moved:

                
                direction = 2
                moved = False
            if event.key == pygame.K_DOWN and direction != 2 and moved:

                direction = 4
                moved = False
            

        if event.type == pygame.QUIT:
            running = False
    
    if direction == 1:
        x_movement=-globals.grid_size
        y_movement=0
    if direction == 3:
        x_movement=globals.grid_size
        y_movement=0
    if direction == 4:
        x_movement=0
        y_movement=globals.grid_size
    if direction == 2:
        x_movement=0
        y_movement=-globals.grid_size
    
    tick=tick+1
    
    if(tick==speed):
        
        #print(str(direction) + "," + str(direction_old))        
        moved = True
        
        tick=0
        
        new_x = game_segments[0].x + x_movement
        new_y = game_segments[0].y + y_movement
        
        game_segments[0].set_type(1)
        game_segments.insert(0,SnakeSegment(new_x,new_y,direction))
        
        if(direction_old!=direction):
            print(str(direction) + "," + str(direction_old))
            game_segments[1].set_direction_old(direction_old)
            game_segments[1].set_direction(direction)
        
        
        for i in range(1,len(game_segments)-1):
            if game_segments[i].x == game_segments[0].x and game_segments[i].y == game_segments[0].y:
                reset_game()
        
        if not eaten_food:
            game_segments.pop(len(game_segments)-1)
        else:
            eaten_food=False
        if game_segments[0].x == game_food.x and game_segments[0].y == game_food.y:
            eaten_food=True
            game_food=Food(random.randint(1,globals.range_x_divided)*globals.grid_size,random.randint(1,globals.range_y_divided)*globals.grid_size)
        
        
        if(game_segments[0].x>globals.range_x or game_segments[0].y>globals.range_y or game_segments[0].x<0 or game_segments[0].y<0):
            reset_game()
            
        direction_old=direction

def draw():
    
    
    screen.fill((255,255,255))
    
    pygame.draw.rect(screen,(0,0,0),[0,0,globals.range_x+globals.grid_size,globals.range_y+globals.grid_size],3)

    
    for items in game_segments:
        items.draw(screen)
    
    game_food.draw(screen)
        

    
    pygame.display.update()
    
    
running = True

reset_game()
while running:
    
    clock.tick(60)
    
    
    update()
    draw()
    

    
    


