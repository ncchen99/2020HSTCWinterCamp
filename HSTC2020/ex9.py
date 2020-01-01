import pygame, sys

white= (255, 255, 255)
black= (0, 0, 0)

pygame.init()
pygame.display.set_caption('Mouse Example')
size= [640, 480]
screen= pygame.display.set_mode(size)
clock= pygame.time.Clock()

# 使系統鼠標圖標不可見
pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            sys.exit()
       # 如果按下鼠標
       # get_pressed() 告訴您按下哪個鼠標按鈕
        if event.type == pygame.MOUSEBUTTONDOWN:
            print ('mouse pressed',pygame.mouse.get_pressed())
       # 如果釋放鼠標
        elif event.type == pygame.MOUSEBUTTONUP:
            print ('mouse released', pygame.mouse.get_pressed())
       # 如果鼠標在運動中
       # get_rel() - 返回自上次調用此函數以來X和Y的移動量
        if event.type == pygame.MOUSEMOTION:
            print ('mouse is moving', pygame.mouse.get_rel()) 
           
    screen.fill((255, 255, 255))

    # 在鼠標周圍畫一個圓
    pos= (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    pygame.draw.circle(screen, black, pos, 10, 0)

    pygame.display.update()

    clock.tick(20)
