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

def init():
    global grid_size
    grid_size = 64
    global screen_width
    screen_width = 1024
    global screen_height
    screen_height = 768
    global range_x_divided
    global range_y_divided
    
    range_x_divided =int(screen_width/grid_size)-1
    range_y_divided =int(screen_height/grid_size)-1
    
    global range_y
    global range_x
    
    range_y = range_y_divided*grid_size
    range_x = range_x_divided*grid_size