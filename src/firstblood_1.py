# filename is: firstblood_1.py
# import zone
import pygame
from pygame.color import THECOLORS

# initialize pygame
pygame.init()

# create a pygame screen
screen = pygame.display.set_mode([800, 600])

# fill with color WHITE
screen.fill(THECOLORS['white'])
# load and show the image of lanbo
jpgFileName = 'lanbo800_600.jpg'
imgRect = pygame.image.load(jpgFileName)
screen.blit(imgRect, [0, 0])
# load and show the sound of firstblood
wavFileName = 'FirstBlood.wav'
pygame.mixer.music.load(wavFileName)
pygame.mixer.music.play()
# flip
pygame.display.flip()

# LOOP: mRunning
mRunning = True
while mRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mRunning = False
            pygame.quit()
