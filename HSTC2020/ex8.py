import pygame
import random
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("sprite 範例")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg') #背景

clock = pygame.time.Clock()

class player(pygame.sprite.Sprite):
    def __init__(self,x,dx,y,width,height):
        super().__init__()
        self.walkCount = 0
        self.image = walkRight[self.walkCount//3]
        # 回傳位置
        self.rect = self.image.get_rect()
        # 定位
        self.rect.center = (x, y)
        self.x = x
        self.y = y
        self.dx = dx

    def draw(self):
        if self.walkCount + 1 >= 27: #這樣是為了移動三次，才換一個造型
            self.walkCount = 0
        if self.x>450 or self.x<50: #到達右邊界 或 左邊界
            self.dx *= -1 #水平速度變號
        if self.dx > 0: #向右走
            self.image = walkRight[self.walkCount//3]
        else: #向左走
            self.image = walkLeft[self.walkCount//3]
        self.rect.center = (self.x,self.y)   
        self.x += self.dx
        self.walkCount += 1


# 亂數建立三個在不同位子的呆子，把他們存在man中
mans = [player(random.randint(50,300), 1, random.randint(200,400), 64,64),
       player(random.randint(50,300), -1, random.randint(200,400), 64,64),
       player(random.randint(50,300), 2, random.randint(200,400), 64,64)]

#建立角色群組
allMan = pygame.sprite.Group() 
#將他們依序加入角色群組
for man in mans:
    allMan.add(man)
    print (man)

run = True
#mainloop
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.blit(bg, (0,0))
    for man in mans:
        man.draw()
    allMan.draw(win)
    pygame.display.update()

pygame.quit()
