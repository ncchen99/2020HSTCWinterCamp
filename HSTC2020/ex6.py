import pygame as pg
pg.init()

#設定視窗
width, height = 640, 480        #寬、高的變數，方便後修改              
screen = pg.display.set_mode((width, height))   
pg.display.set_caption("NCC's game")         
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255,255,255)) 

clock = pg.time.Clock()   #建立時間元件

#關閉程式的程式碼
running = True
while running:
    clock.tick(30)        #每秒執行30次 ，FPS = 30
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.blit(bg, (0,0))  #重繪視窗
    pg.display.update()     #更新視窗
    
pg.quit()  
