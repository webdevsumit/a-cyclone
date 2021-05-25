import pygame
from math import pi
import random

pygame.init()
screen = pygame.display.set_mode((1500,1500))
width = screen.get_width()
height = screen.get_height()
Clock = pygame.time.Clock()
pygame.display.set_caption('Cyclone')



def hero_page():
    
    hero = True
    center = (1100,500)
    
    speed1 = pi/200
    speed2 = pi/150
    speed3 = pi/100
    speed4 = pi/50
    
    rect1_displacement = 0
    rect2_displacement = 0
    rect3_displacement = 0
    rect4_displacement = 0
    
    while hero:
        screen.fill((127,127,127))
        rect = pygame.draw.circle(screen,(0,0,125),center,200,1)
        
        rect1_displacement += speed1
        rect2_displacement += speed2
        rect3_displacement += speed3
        rect4_displacement += speed3
        
        rectArr = [
            [400,10,5,rect1_displacement,(0,0,125)],
            [410,15,13,rect2_displacement,(0,125,0)],
            [200,20,20,rect3_displacement,(225,0,0)],
            [35,25,25,rect4_displacement,(190,180,180)]
        ]
        
        for arr in rectArr:
            for j in range(1,20):
                rect.width = rect.height = arr[0]
                for i in range(1,100):
                    rect.width = rect.height = rect.height+i/arr[1]+j/arr[2]
                    rect.center = center
                    pygame.draw.arc(screen,arr[4],rect,0-i/40-j+arr[3],pi/4-i/10-j+arr[3],5)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hero = False
                
            
        pygame.display.update()
        pygame.display.flip()
        Clock.tick(35)
    pygame.quit()
    
hero_page()