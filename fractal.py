from vpython import *
import os

if os.name == "posix":
    scene = canvas(width=950, height=1870)
else:
    scene = canvas(width=1500, height=690)

def tree(arr, le, re, c):
    arr2 = []
    #l = rotate(le, radians(45+ang))
    #r = rotate(re, radians(-45+ang))
    for i, ang in arr:
        pos = i.point(1)["pos"]
        arr2.append([curve(pos, pos+rotate(le, radians(45+ang)), radius=0.1/(c+1)), 45+ang])
        arr2.append([curve(pos, pos+rotate(re, radians(-45+ang)), radius=0.1/(c+1)), -45+ang])
    return arr2

le = vec(0, 1, 0)
st_v = vec(0, -1, 0)
start = [[curve(st_v, st_v+le, radius=0.1), 0]]
c = 1
max = 10

while True:
    if c <= max:
        ev = scene.waitfor('mousedown mouseup')
        if ev.event == 'mousedown':
            le = vec(0, 1/c, 0)
            re = vec(0, 1/c, 0)
            start = tree(start, le, re, c)
            c += 1


'''# Importing the python libraries 
import pygame, math 
  
# Initialize all imported pygame modules 
pygame.init() 
  
# Create a new surface and window. 
surface_height, surface_width = 800, 600        #Surface variables 
main_surface = pygame.display.set_mode((surface_height,surface_width)) 
  
# Captioning the window 
pygame.display.set_caption("Fractal_Tree_geeksforgeeks") 
  
def draw_tree(order, theta, sz, posn, heading, color=(0,0,0), depth=0): 
  
   # The relative ratio of the trunk to the whole tree   
   trunk_ratio = 0.29     
  
   # Length of the trunk   
   trunk = sz * trunk_ratio 
   delta_x = trunk * math.cos(heading) 
   delta_y = trunk * math.sin(heading) 
   (u, v) = posn 
   newpos = (u + delta_x, v + delta_y) 
   pygame.draw.line(main_surface, color, posn, newpos) 
  
   if order > 0:   # Draw another layer of subtrees 
  
      # These next six lines are a simple hack to make  
      # the two major halves of the recursion different  
      # colors. Fiddle here to change colors at other  
      # depths, or when depth is even, or odd, etc. 
      if depth == 0: 
          color1 = (255, 0, 0) 
          color2 = (0, 0, 255) 
      else: 
          color1 = color 
          color2 = color 
  
      # make the recursive calls to draw the two subtrees 
      newsz = sz*(1 - trunk_ratio) 
      draw_tree(order-1, theta, newsz, newpos, heading-theta, color1, depth+1) 
      draw_tree(order-1, theta, newsz, newpos, heading+theta, color2, depth+1) 
  
  
def main(): 
    theta = 0.5
  
    while True: 
  
        # Update the angle 
        #theta += 0.01
  
        # This little part lets us draw the stuffs  
        # in the screen everything 
        main_surface.fill((255, 255, 0)) 
        draw_tree(9, theta, surface_height*0.7, (surface_width//2, surface_width), -math.pi/2) 
        pygame.display.flip() 
  
# Calling the main function 
main() 
pygame.quit() '''