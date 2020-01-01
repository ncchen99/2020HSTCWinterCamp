#made by ncc
from pygame import mixer
import os
from time import sleep
from sys import exit
mixer.init()
alldir=os.walk(os.path.dirname(__file__))
print(os.path.dirname(__file__))
i=0
mp3f=[] # mp3檔暫存list
print('''
這是一個簡易的小小音樂播放氣，
輸入音樂前的編號可撥放該歌曲，
輸入英文字 p 可以播放前一首，
輸入英文字 n 可以播放後一首，
輸入英文字 e 可以離開。
請按任意鍵繼續... (◔⊖◔)つ
''')
input()
for dirname,subdir,files in alldir: #在這個程式的目錄下尋找所有mp3
    for file in files:
        ext=file.split('.')[-1]
        if ext=='mp3':
            print(str(i)+" . "+file)
            i+=1
            mp3f.append(os.path.join(dirname, file))
indexmp3=input('想幹啥? :')

while True:
    if indexmp3=='n':
        if a==len(mp3f)-1:
            a=0
        else:
            a+=1
    elif indexmp3=='p':
        if a==0:
            a=len(mp3f)-1
        else:
            a-=1
    elif indexmp3=='e':
        print("掰掰 (ó㉨ò)")
        sleep(1)
        exit()
    else:
        try:
            if int(indexmp3)>len(mp3f)-1:
                a=len(mp3f)-1
            else:
                a=int(indexmp3)
        except:
            print('蛤 ／/( ◕‿‿◕ )＼ ')
            indexmp3=input('想幹啥? :')
            continue
    mixer.music.load(mp3f[a])
    mixer.music.play(-1)
    print('正在播放: ' +mp3f[a].split('/')[-1][:-5])
    indexmp3=input('想幹啥? :')
    mixer.music.stop()
