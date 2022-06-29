import pygame
import random
pygame.init()
surface = pygame.display.set_mode((1920,1028))
zoom = 0.001
start_x = 1450/zoom
start_y = 1027.5/zoom
def mandlebrot():
    max_iteration = 50
        
    for j in range(0,1028):
        j+=start_y
        for i in range(0,1920):
            i+=start_x
            xtemp = 0
            iteration = 0
            x2 = 0
            y2 = 0
            x = 0
            y = 0
            x0 = (i*zoom-1920)/250
            y0 = (j*zoom-1028)/250
                

            while (x2 + y2 <= 4 and iteration < max_iteration):
                y = (x+x)*y + y0
                x = x2 - y2 + x0
                x2 = x*x
                y2 = y*y
        
                iteration +=  1 
                    
            if iteration == max_iteration:
                pygame.draw.rect(surface, (0,0,0), pygame.Rect(i-start_x, j-start_y, 1, 1))
            else:
                blue = iteration * 26*20/max_iteration
                if blue > 255:
                    blue = 255
                pygame.draw.rect(surface, (iteration*13*20/max_iteration,iteration*13*20/max_iteration,blue), pygame.Rect(i-start_x, j-start_y, 1, 1))
                
                
    pygame.display.flip()
                    
    
    
mandlebrot()