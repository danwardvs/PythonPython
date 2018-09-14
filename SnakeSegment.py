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



myimage = pygame.image.load("r.png")
imagerect = myimage.get_rect()



class SnakeSegment(object):
    

    x=0
    y=0
    type = 0
    direction = 0
         
    def __init__ (self,new_x,new_y,new_direction):
        self.x=new_x
        self.y=new_y
        self.type = 2
        self.direction = new_direction
        
    
    def draw(self,new_screen):
        #pygame.draw.rect(new_screen,(0,0,255),[self.x,self.y,globals.grid_size,globals.grid_size],2)
        imagerect.x = self.x
        imagerect.y = self.y
        if(self.direction==2):
            new_screen.blit(myimage, (self.x,self.y),(64*3,0,64,64))
        if(self.direction==3):
            new_screen.blit(myimage, (self.x,self.y),(64*4,0,64,64))
        if(self.direction==1):
            new_screen.blit(myimage, (self.x,self.y),(64*3,64,64,64))
        if(self.direction==4):
            new_screen.blit(myimage, (self.x,self.y),(64*4,64,64,64))
        













