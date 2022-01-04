import math

import pygame
from pygame.color import THECOLORS

# initialize pygame
pygame.init()

# create a pygame screen
screen = pygame.display.set_mode([600, 600])

# 将蓝色铺满整个窗口
# screen.fill(THECOLORS['blue'])


# 绘制不同形状的方法
# 绘制矩形的语句格式如下：
#
# 矩形    rect(screen, 颜色,范围（left,top,width,height）,线宽（0表示填充）)
# 圆形    circle(screen, 颜色,位置（left,top）,半径,线宽（0表示填充）)
# 弧形    pygame.draw.arc(screen,颜色,范围（left,top,width,height）,起始角度,结束角度,线宽)
# 椭圆    ellipse(screen, 颜色,范围（left,top,width,height）,线宽（0表示填充）)
# 曲线    aalines(screen, 颜色,False（首尾不相连）, plotPoints（点的列表）, 线宽)

#  添加白色与红色区域
# pygame.draw.rect(screen, THECOLORS['white'],[0,150,600,100],0)
# pygame.draw.rect(screen, THECOLORS['white'],[150,0,100,400],0)
# pygame.draw.rect(screen, THECOLORS['red'],[0,170,600,60],0)
# pygame.draw.rect(screen, THECOLORS['red'],[170,0,60,400],0)
# screen.fill(THECOLORS['red'])
# pygame.draw.rect(screen, THECOLORS['blue'], [0, 100, 600, 200], 0)
# pygame.draw.circle(screen, THECOLORS['white'], [300, 200], 90, 0)

# 画太极
screen.fill(THECOLORS['white'])
pygame.draw.circle(screen, THECOLORS['black'], [300, 300], 300, 0)
pygame.draw.rect(screen, THECOLORS['white'], [0, 300, 600, 300], 0)
pygame.draw.circle(screen, THECOLORS['black'], [150, 300], 150, 0)
pygame.draw.circle(screen, THECOLORS['white'], [450, 300], 150, 0)
pygame.draw.circle(screen, THECOLORS['white'], [125, 300], 50, 0)
pygame.draw.circle(screen, THECOLORS['black'], [475, 300], 50, 0)
pygame.draw.arc(screen, THECOLORS['black'], [0, 0, 600, 600], math.pi, 2 * math.pi, 1)





# 翻转
pygame.display.flip()

# LOOP: mRunning
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
            pygame.quit()
