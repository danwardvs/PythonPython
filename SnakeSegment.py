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
    direction_old = 0
    printed = False
    
    def set_type(self,new_type):
        self.type = new_type
    
    def set_direction_old(self,new_direction_old):
        self.direction_old = new_direction_old
        #print(str(self.direction) + "," + str(self.direction_old))
    
    def set_direction(self,new_direction):
        self.direction = new_direction
         
    def __init__ (self,new_x,new_y,new_direction):
        self.x=new_x
        self.y=new_y
        self.type = 2
        self.direction = new_direction
        
    
    def draw(self,new_screen):
        #pygame.draw.rect(new_screen,(0,0,255),[self.x,self.y,globals.grid_size,globals.grid_size],2)
        imagerect.x = self.x
        imagerect.y = self.y
        if(self.type==2):
            if(self.direction==2):
                new_screen.blit(myimage, (self.x,self.y),(64*3,0,64,64))
            if(self.direction==3):
                new_screen.blit(myimage, (self.x,self.y),(64*4,0,64,64))
            if(self.direction==1):
                new_screen.blit(myimage, (self.x,self.y),(64*3,64,64,64))
            if(self.direction==4):
                new_screen.blit(myimage, (self.x,self.y),(64*4,64,64,64))
        if(self.type==1):
            
            if((self.direction==1 or self.direction == 3) and self.direction_old == 0 ):
                new_screen.blit(myimage, (self.x,self.y),(64,0,64,64))
            if((self.direction==2 or self.direction == 4) and self.direction_old == 0 ):
                new_screen.blit(myimage, (self.x,self.y),(64*2,64,64,64))
            
            if(self.direction_old!=0 and not self.printed):
                print(str(self.direction) + "," + str(self.direction_old))
                self.printed=True
            
            if((self.direction==1  and self.direction_old == 4 ) or (self.direction==2  and self.direction_old == 3 )):
                new_screen.blit(myimage, (self.x,self.y),(64*2,64*2,64,64))
                
            if((self.direction==3  and self.direction_old == 2 ) or (self.direction==4  and self.direction_old == 1 )):
                new_screen.blit(myimage, (self.x,self.y),(0,0,64,64))
            
            if((self.direction==2  and self.direction_old == 1 ) or (self.direction==3  and self.direction_old == 4 )):
                new_screen.blit(myimage, (self.x,self.y),(0,64,64,64))
            
            
            if((self.direction==4  and self.direction_old == 3 ) or (self.direction==1  and self.direction_old == 2 )):
                new_screen.blit(myimage, (self.x,self.y),(64*2,0,64,64))
        if(self.type==0):
            if(self.direction==2):
                new_screen.blit(myimage, (self.x,self.y),(64*3,64*2,64,64))
            if(self.direction==3):
                new_screen.blit(myimage, (self.x,self.y),(64*4,64*2,64,64))
            if(self.direction==1):
                new_screen.blit(myimage, (self.x,self.y),(64*3,64*3,64,64))
            if(self.direction==4):
                new_screen.blit(myimage, (self.x,self.y),(64*4,64*3,64,64))
            
            
            













