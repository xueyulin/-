
'''
B0329003_資工二_林學宇
訊號與系統、機率與統計
pygame作業
'''

#pygame music

import os, pygame
from pygame.locals import *
from sys import exit
from random import *


if not pygame.mixer: print('Warning, sound disabled!')
if not pygame.font: print('Warning, fonts disabled!')

pygame.init()

視窗寬度 = 1000
視窗高度 = 600
視窗預設大小 = (視窗寬度, 視窗高度 + 20)
音量 = 5
圖片開始座標 = (60, 60)
圖片結束座標 = (245, 245)
圓圈座標 = [(85, 350), (150, 350), (215, 350), (280, 350), (555, 425)]
圓圈半徑 = 25
圓環寬度 = 3

撥放鍵狀態 = True
收藏鍵狀態 = True


資料路徑 = 'data'
圖片路徑 = 'image'
背景圖片路徑 = 'image\\background'
字型路徑 = 'font'
聲音路徑 = 'sound'

背景檔名 = 'bg.jpg'

#size:(240*240)
BGS = []
音樂編號狀態 = 0
音樂 = [('1.OGG', 'You Raise Me Up', 'WestLife', '1.png'),
         ('2.OGG', '不完整的旋律', '王力宏', '2.png'),
         ('3.OGG', 'A Place Nearby' , 'Lene Marlin', '3.png'),
         ('4.OGG', 'Just Give Me A Reason' , 'Pink', '4.png'),
         ('5.OGG', '我 ' , '張國榮', '5.png'),
         ('6.OGG', '大城小愛' , '王力宏', '6.png'),
         ('7.OGG', '聊天' , '郭静', '7.png')]
westlift = 'westlife.png'

音量值 = []
音量值初始位置 = []
音量值顏色 = []
for p in range(170, 250, 7):
    音量值.append([視窗寬度 - p,視窗高度 + 20])
for ps in range(175, 250, 7):
    音量值初始位置.append([視窗寬度 - ps, 視窗高度])
    音量值顏色.append((randint(0, 255), randint(0, 255), randint(0, 255)))

視窗 = pygame.display.set_mode(視窗預設大小, 0, 32)
bg = pygame.image.load(os.path.join(資料路徑, 背景圖片路徑, 背景檔名)).convert()


音樂的陣列 = []
圖片的陣列 = []
for song in range(len(音樂)):
    音樂的陣列.append(pygame.mixer.Sound(os.path.join(資料路徑, 聲音路徑, 音樂[song][0])))
    圖片的陣列.append(pygame.image.load(os.path.join(資料路徑, 圖片路徑, 音樂[song][3])).convert())

font = pygame.font.Font(os.path.join(資料路徑, 字型路徑, 'TORK____.ttf'), 14)
標題字型 = pygame.font.Font(os.path.join(資料路徑, 字型路徑, 'msyhbd.ttf'), 24)
歌曲字型 = pygame.font.Font(os.path.join(資料路徑, 字型路徑, 'msyh.ttf'), 16)

def draw_picture_rect():
     #picture rect
    pygame.draw.rect(視窗,
                     (255, 255, 255),
                     Rect(圖片開始座標, 圖片結束座標))

def button_play(視窗, color):
    pygame.draw.circle(視窗, color, 圓圈座標[0], 圓圈半徑, 圓環寬度)
    points=[(77,340),(77,360),(95,350)]
    pygame.draw.polygon(視窗,color,points)

def button_stop(視窗, color):
    pygame.draw.circle(視窗, color, 圓圈座標[0], 圓圈半徑, 圓環寬度)
    pygame.draw.rect(視窗,
                     color,
                     Rect(77, 340, 5, 23 ))
    pygame.draw.rect(視窗,
                     color,
                     Rect(88, 340, 5, 23 ))

def button_perfer(視窗, color):
    pygame.draw.circle(視窗, color, 圓圈座標[1], 圓圈半徑, 圓環寬度)
    points=[(138,340),(162,340),(150,363)]
    pygame.draw.polygon(視窗,color,points)

def button_del(視窗, color):
    pygame.draw.circle(視窗, color, 圓圈座標[2], 圓圈半徑, 圓環寬度)
    pygame.draw.circle(視窗, color, (215, 340), 6, 3)
    pygame.draw.rect(視窗,
                     color,
                     Rect(200, 340, 30, 6 ))
    pygame.draw.rect(視窗,
                     color,
                     Rect(204, 340, 3, 20 ))
    pygame.draw.rect(視窗,
                     color,
                     Rect(210, 340, 3, 20 ))
    pygame.draw.rect(視窗,
                     color,
                     Rect(217, 340, 3, 20 ))
    pygame.draw.rect(視窗,
                     color,
                     Rect(223, 340, 3, 20 ))
    pygame.draw.rect(視窗,
                     color,
                     Rect(204, 360, 22, 5 ))

def button_next_song(視窗, color):
    pygame.draw.circle(視窗, color, 圓圈座標[3], 圓圈半徑, 圓環寬度)
    points_one =[(270,343),(270,357),(277,350)]
    points_two =[(277,343),(277,357),(284,350)]
    pygame.draw.polygon(視窗,color,points_one)
    pygame.draw.polygon(視窗,color,points_two)
    pygame.draw.rect(視窗,
                     color,
                     Rect(284, 343, 5, 15 ))

					 
def listener():
    global 撥放鍵狀態
    global 收藏鍵狀態
    x, y = pygame.mouse.get_pos()
    color = (255,255,25)
    color_red = (230, 0, 0)
    for index in range(len(圓圈座標)):
        p_x = (圓圈座標[index][0] - x)**2
        p_y = (圓圈座標[index][1] - y)**2
        p_r = (圓圈半徑)**2
        if (p_x + p_y <= p_r):
            if index == 0 and 撥放鍵狀態:
                button_stop(視窗, color)
            elif index == 0 and not 撥放鍵狀態:
                button_play(視窗, color)
            elif index == 1 and 收藏鍵狀態:
                button_perfer(視窗, color)
            elif index == 1 and not 收藏鍵狀態:
                button_perfer(視窗, color_red)
            elif index == 2:
                button_del(視窗, color)
            elif index == 3:
                button_next_song(視窗, color)
            elif index == 4:
                button_authon_image(視窗, color)
				

def mouse_down_listener(sound):
    global 撥放鍵狀態
    global 收藏鍵狀態
    global 音樂編號狀態
    x, y = pygame.mouse.get_pos()
    for index in range(len(圓圈座標)):
        p_x = (圓圈座標[index][0] - x)**2
        p_y = (圓圈座標[index][1] - y)**2
        p_r = (圓圈半徑)**2
        if (p_x + p_y <= p_r):
            if index == 0 and 撥放鍵狀態:
                #print('stop now......')
                sound.stop()
                撥放鍵狀態 = False
            elif index == 0 and not 撥放鍵狀態:
                #print('play now ... ... ... ...')
                sound.play(0)
                撥放鍵狀態 = True
            elif index == 1 and 收藏鍵狀態:
                print('perfer song....<<', 音樂[音樂編號狀態][1], '>>')
                收藏鍵狀態 = False
            elif index == 1 and not 收藏鍵狀態:
                print('not perfer song... <<', 音樂[音樂編號狀態][1], '>>')
                收藏鍵狀態 = True
            elif index == 2:
                sound.stop()
                print('delete song....<<', 音樂[音樂編號狀態][1], '>>')
                if 音樂編號狀態 > 0:
                    音樂.pop(音樂編號狀態)
                    圖片的陣列.pop(音樂編號狀態)
                    音樂的陣列.pop(音樂編號狀態)
                    if 音樂編號狀態 >= len(音樂) - 1:
                        音樂編號狀態 -= 1
                else:
                    print('This is the last song.')
            elif index == 3:
                sound.stop()
                if 音樂編號狀態 < len(音樂) - 1:
                    音樂編號狀態 += 1
                else:
                    音樂編號狀態 = 0
                #print('next song....')
                
def draw_button(sound):
    color = (255,255,255)
    color_red = (230, 0, 0)
    #play or stop
    if 撥放鍵狀態:
        sound.play(0)
        button_stop(視窗, color)
    elif not 撥放鍵狀態:
        button_play(視窗, color)
    #perfer song
    if 收藏鍵狀態:
        button_perfer(視窗, color)
    elif not 收藏鍵狀態:
        button_perfer(視窗, color_red)
    #delete
    button_del(視窗, color)
    #next song
    button_next_song(視窗, color)
	

def draw_volume_info():
    #the background of volume
    pygame.draw.rect(視窗,
                     (255, 255, 255),
                     Rect((音量值初始位置[-1][0],
                           音量值初始位置[-1][1]),
                          (音量值[-10][0] - 音量值初始位置[-1][0],
                           20)))
    #the size of volume
    for v in range(音量+1):
        if v > 0:
            pygame.draw.rect(視窗,
                             音量值顏色[v],
                             Rect((音量值初始位置[-v][0],
                                   音量值初始位置[-v][1]),
                                  (音量值[-v][0] - 音量值初始位置[-v][0],
                                   20)))

def draw_song_title():
    title = 標題字型.render(音樂[音樂編號狀態][1], True, (255,165,0))
    songer = 歌曲字型.render(音樂[音樂編號狀態][2], True, (255, 255, 255))
    視窗.blit(title, (320, 60))
    視窗.blit(songer, (320, 110))

def draw_state_bar_info():
    pygame.draw.line(視窗, (165,42,42),(0, 視窗高度), (視窗寬度, 視窗高度))
    #music info
    music_info = 'All音樂: ' + str(len(音樂)) +'     Current: ' + str(音樂編號狀態 + 1)
    text = font.render(music_info, True, (255,255,255))
    視窗.blit(text, (0, 視窗高度+5))
    #author into
    author_info = font.render('hongtenzone@foxmail.com', True, (255,255,255))
    視窗.blit(author_info, (視窗寬度 - 160, 視窗高度+5))
    #volume info
    volume_text = font.render('Volume: ' + str(音量), True, (255, 255, 255))
    視窗.blit(volume_text, (視窗寬度 - 310, 視窗高度+5))
    
while True:
    
    視窗.blit(bg, (0, 0))
    pic = 圖片的陣列[音樂編號狀態]
    bg_sound = 音樂的陣列[音樂編號狀態]
    bg_sound.set_volume(0.1 * 音量)
    draw_button(bg_sound)
    listener()
    for event in pygame.event.get():
        if event.type == QUIT:
            bg_sound.stop()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                pass
            elif event.key == K_DOWN:
                pass
            elif event.key == K_LEFT:
                if 音量 > 0:
                    音量 -= 1
            elif event.key == K_RIGHT:
                if 音量 <= 9:
                    音量 += 1
        elif event.type == MOUSEMOTION:
            pass
                    
        elif event.type == MOUSEBUTTONDOWN:
            pressed_array = pygame.mouse.get_pressed()
            for index in range(len(pressed_array)):
                if pressed_array[index]:
                    if index == 0: #When the LEFT button down
                        mouse_down_listener(bg_sound)

    #picture rect
    draw_picture_rect()
    #volume information
    draw_volume_info()
    #state bar information
    draw_state_bar_info()
    #song title
    draw_song_title()
    
    視窗.blit(pic, (62.5, 62.5))
    pygame.display.update()
