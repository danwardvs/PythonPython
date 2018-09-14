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
from SnakeSegment import SnakeSegment

myimage = pygame.image.load("food.png")
imagerect = myimage.get_rect()

class Food(SnakeSegment):
    
    def draw(self,new_screen):
        #pygame.draw.rect(new_screen,(255,0,0),[self.x,self.y,globals.grid_size,globals.grid_size],2)
        imagerect.x = self.x
        imagerect.y = self.y
        new_screen.blit(myimage, imagerect)
