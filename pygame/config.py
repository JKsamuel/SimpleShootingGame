import pygame

pygame.init()
screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('img/ufo.jpg')
pygame.display.set_icon(icon)


bgImg = pygame.image.load('img/background.jpg')
bgImg = pygame.transform.scale(bgImg, (screenWidth, screenHeight))
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# explosionImg
explosionImg = pygame.image.load('img/player.jpg')
explosionImg = pygame.transform.scale(explosionImg, (50, 50))

#Music
bulletSound = pygame.mixer.Sound('music/bullet.wav')
pygame.mixer.music.load('music/bg.mp3')