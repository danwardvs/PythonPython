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
import globals

myimage = pygame.image.load("segment.png")
imagerect = myimage.get_rect()


class SnakeSegment(object):
    x=0
    y=0
    game_screen = pygame.display.init
    
    def __init__ (self,new_x,new_y):
        self.x=new_x
        self.y=new_y
    
    def draw(self,new_screen):
 
        #pygame.draw.rect(new_screen,(0,0,255),[self.x,self.y,globals.grid_size,globals.grid_size],2)
        imagerect.x = self.x
        imagerect.y = self.y
        new_screen.blit(myimage, imagerect)