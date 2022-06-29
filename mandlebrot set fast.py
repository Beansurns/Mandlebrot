import pygame
import random
pygame.init()
surface = pygame.display.set_mode((1920,1028))
def mandlebrot():
    max_iteration = 20
    pygame.draw.rect(surface, (13,13,26), pygame.Rect(0 ,0 , 453, 1028))
    pygame.draw.rect(surface, (13,13,26), pygame.Rect(1467, 0, 453, 1028))
        
    for j in range(0,515):
        for i in range(453,1467):
            xtemp = 0
            iteration = 0
            x2 = 0
            y2 = 0
            x = 0
            y = 0
            x0 = (i-960)/250
            y0 = (j-514)/250
                

            while (x2 + y2 <= 4 and iteration < max_iteration):
                y = (x+x)*y + y0
                x = x2 - y2 + x0
                x2 = x*x
                y2 = y*y
        
                iteration +=  1 
                    
            if iteration == max_iteration:
                pygame.draw.rect(surface, (0,0,0), pygame.Rect(i, j, 1, 1))
                pygame.draw.rect(surface, (0,0,0), pygame.Rect(i, 1028-j, 1, 1))
            else:
                blue = iteration * 26
                if blue > 255:
                    blue = 255
                pygame.draw.rect(surface, (iteration*13,iteration*13,blue), pygame.Rect(i, j, 1, 1))
                pygame.draw.rect(surface, (iteration*13,iteration*13,blue), pygame.Rect(i, 1028-j, 1, 1))
            
    pygame.display.flip()
                    
    
    
mandlebrot()