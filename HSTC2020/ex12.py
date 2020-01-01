import pygame, sys
pygame.init()
pygame.display.set_caption('Keybroad Example')
screen= pygame.display.set_mode([640, 480])
clock= pygame.time.Clock()
font = pygame.font.Font("HanyiSentyCrayon.ttf", 150)
bg = pygame.Surface([640, 480])
bg.fill((0,0,0))

def drawText(command):
    text = font.render(command,True,(255,255,255))
    screen.blit(bg,(0,0))
    screen.blit(text,
                (320- text.get_width() // 2, 240- text.get_height() // 2))
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                drawText('left')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                drawText('right')
            if event.key == pygame.K_UP or event.key == ord('w'):
                drawText('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                drawText('left stop')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                drawText('right stop')
            if event.key == ord('q'):
                pygame.quit()
