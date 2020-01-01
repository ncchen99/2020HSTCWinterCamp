import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("星空")

space = pygame.image.load("sky.JPG") #載入圖片
space.convert_alpha() 
 
screen.blit(space, (0,0)) #放在視窗最左上角
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
