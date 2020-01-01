import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("偶的 First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')

clock = pygame.time.Clock()

x = 50 #先在左邊
dx = 1 #每次移動2個像素
y = 400 #固定
walkCount = 0 #用於圖片動畫顯示

#mainloop
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.blit(bg, (0,0))
    
    if walkCount + 1 >= 27: #這樣是為了移動三次，才換一個造型
        walkCount = 0

    if x>450: #到達右邊界
        dx = -1
    if x<50: #到達左邊界
        dx = 1
        
    if dx == 1: #向右走
        win.blit(walkRight[walkCount//3], (x,y))
    else: #向左走
        win.blit(walkLeft[walkCount//3], (x,y))
        
    x += dx    
    walkCount += 1
    
    pygame.display.update()

pygame.quit()
