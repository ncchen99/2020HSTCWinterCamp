import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
done = False

screen.fill((255, 255, 255))

comicsansms = pygame.font.SysFont("comicsansms", 72)
hello = comicsansms.render("Hello, World", True, (0, 128, 0))

notoSans = pygame.font.Font("NotoSansMonoCJKtc-Bold.otf" ,56) #思源黑體
chinesetext = notoSans.render("是在哈囉!", True ,(168, 0, 0)) 

screen.blit(hello,
    (320 - hello.get_width() // 2, 160 - hello.get_height() // 2))
screen.blit(chinesetext,
    (320 - chinesetext.get_width() // 2, 260 - chinesetext.get_height() // 2))
#置中

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.update()
    clock.tick(60) #60FPS
pygame.quit()
