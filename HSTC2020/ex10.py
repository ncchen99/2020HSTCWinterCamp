import pygame as pg, random, math
pg.init()

#設定視窗背景
width, height = 640, 480                      
screen = pg.display.set_mode((width, height))   
pg.display.set_caption("NCC's game")         
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255,255,255))

#藍球建立
ball = pg.Surface((70,70))
ball.fill((255,255,255))
pg.draw.circle(ball, (0,0,255), (35,35), 35, 0)
rect = ball.get_rect()
rect.center = (320,240)     
x, y = rect.topleft              
clock = pg.time.Clock()


#關閉程式的程式碼

running = True
playing = False  #開始時球不能移動
while running:
    clock.tick(30)        #每秒執行30次
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    buttons = pg.mouse.get_pressed()
    if buttons[0]:          #按滑鼠左鍵後球可移動
        playing = True
    elif buttons[2]:        #按滑鼠右鍵後球不能移動
        playing = False
    if playing == True:     #球可移動狀態
        mouses = pg.mouse.get_pos()  #取得滑鼠坐標
        rect.centerx = mouses[0]     #移動滑鼠
        rect.centery = mouses[1]
    screen.blit(bg, (0,0))
    screen.blit(ball, rect.topleft) 
    pg.display.update()    
    
pg.quit()
