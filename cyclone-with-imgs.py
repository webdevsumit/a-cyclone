import pygame
from math import pi
pygame.init()
screen = pygame.display.set_mode((1500,1500))
width = screen.get_width()
height = screen.get_height()
Clock = pygame.time.Clock()
pygame.display.set_caption('Cyclone')
font56 = pygame.font.SysFont(None,56)

    
c1 = pygame.image.load('./c1.png')
c2 = pygame.image.load('./c2.png')
c3 = pygame.image.load('./c3.png')
c4 = pygame.image.load('./c4.png')
c5 = pygame.image.load('./c5.png')

c5 = pygame.transform.scale(c5,(2*width,2*height))
c4 = pygame.transform.scale(c4,(800,800))
c3 = pygame.transform.scale(c3,(500,500))
c2 = pygame.transform.scale(c2,(200,200))
c1 = pygame.transform.scale(c1,(50,50))

c1_rect = c1.get_rect()
c1_rect.center = (width/2,height/2)
c2_rect = c2.get_rect()
c2_rect.center = (width/2,height/2)
c3_rect = c3.get_rect()
c3_rect.center = (width/2,height/2)

c5_rect = c5.get_rect()
c5_rect.center = (width/2,height/2)

c1_rpm = 2*pi
c2_rpm = pi
c3_rpm = pi/4
c4_rpm = pi/8
c5_rpm = pi/16


def hero_page():
    hero = True
    
    global c1
    global c2
    global c3
    global c4
    global c5
    
    while hero:
        screen.fill((170,170,170))
        head_img = font56.render('Cyclone',True,(0,0,0))
        head_img_rect = head_img.get_rect()
        head_img_rect.center = (width/2,100)
        screen.blit(head_img,head_img_rect)   
        
        c1 = pygame.transform.rotate(c1,c1_rpm)
        c1_rect = c1.get_rect()
        c1_rect.center = (width/2,height/2)
        
        c2 = pygame.transform.rotate(c2,c2_rpm)
        c2_rect = c2.get_rect()
        c2_rect.center = (width/2,height/2)
        
        c3 = pygame.transform.rotate(c3,c3_rpm)
        c3_rect = c3.get_rect()
        c3_rect.center = (width/2,height/2)
        
        c4 = pygame.transform.rotate(c4,c4_rpm)
        c4_rect = c4.get_rect()
        c4_rect.center = (width/2,height/2)
        
        c5 = pygame.transform.rotate(c5,c5_rpm)
        c5_rect = c5.get_rect()
        c5_rect.center = (width/2,height/2)
 
        screen.blit(c5, c5_rect)
        screen.blit(c4, c4_rect)
        screen.blit(c3, c3_rect)
        screen.blit(c2, c2_rect)
        screen.blit(c1, c1_rect)
 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hero = False
                
            
        pygame.display.update()
        pygame.display.flip()
        Clock.tick(60)
    pygame.quit()
    
hero_page()