import pygame
import random
pygame.init()
surface = pygame.display.set_mode((1920,1028))
for r in range(1,6):
    q = round(20/(2**(r-1)))
    max_iteration = r*5
    pygame.draw.rect(surface, (1*(255/max_iteration),1*(255/max_iteration),2*(255/max_iteration)), pygame.Rect(0 ,0 , 453, 1028))
    pygame.draw.rect(surface, (1*(255/max_iteration),1*(255/max_iteration),2*(255/max_iteration)), pygame.Rect((1920-453), 0, 453, 1028))
        
    for j in range(0,int(1048/2),q):
        for i in range(453,(1920 - 453),q):
            xtemp = 0
            iteration = 0
            x2 = 0
            y2 = 0
            x = 0
            y = 0
            x0 = (i-1920/2)/250
            y0 = (j-1028/2)/250
                

            while (x2 + y2 <= 4 and iteration < max_iteration):
                y = (x+x)*y + y0
                x = x2 - y2 + x0
                x2 = x*x
                y2 = y*y
        
                iteration +=  1 
                    
            if iteration == max_iteration:
                pygame.draw.rect(surface, (0,0,0), pygame.Rect(i, j, q, q))
                pygame.draw.rect(surface, (0,0,0), pygame.Rect(i, 1028-j, q, q))
            else:
                blue = 2 * iteration * (255 / max_iteration)
                if blue > 255:
                    blue = 255
                pygame.draw.rect(surface, (iteration*(255/max_iteration),iteration*(255/max_iteration),blue), pygame.Rect(i, j, q, q))
                pygame.draw.rect(surface, (iteration*(255/max_iteration),iteration*(255/max_iteration),blue), pygame.Rect(i, 1028-j, q, q))
                
                    
    pygame.display.flip() 
                    
                
                        

