from config import *
from bullet import *

# Player
playerImgWidth = 50
playerImgHeigt = 50
playerImg = pygame.image.load('img/player.jpg')
playerImg = pygame.transform.scale(playerImg, (playerImgWidth, playerImgHeigt))

playerX = int((screenWidth - playerImgWidth) / 2)
playerY = 480
speed = 5

class Player:
    def __init__(self, image, position):
        self.image = image
        self.x = position[0]
        self.y = position[1]
        self.width = image.get_width()
        self.height = image.get_height()
        self.isExist = True
        self.hp = 200
        self.bullets = []
        self.isFired = False
        self.point = 0

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

        if self.hp == 0:
            screen.blit(explosionImg, (self.x, self.y))
            self.isExist = False

        for bullet in self.bullets:
            bullet.draw()
            bullet.move()

            if bullet.isExist == False:
                self.bullets.remove(bullet)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            if self.x >= speed:
                self.x -= speed
            else:
                self.x = 0
        if keys[pygame.K_RIGHT]:
            if self.x + speed <= screenWidth - self.width:
                self.x += speed
            else:
                self.x = screenWidth - self.width
        if keys[pygame.K_UP]:
            if self.y >= speed:
                self.y -= speed
            else:
                self.y = 0
        if keys[pygame.K_DOWN]:
            if self.y + speed <= screenHeight - self.height:
                self.y += speed
            else:
                self.y = screenHeight - self.height
        if keys[pygame.K_SPACE]:
            if self.isFired == False:
                self.bullets.append(Bullet(bulletImg, (self.x + self.width/2 - bulletImgWidth/2, self.y)))
                self.isFired = True
                bulletSound.play()
        else:
            self.isFired = False


    def rect(self):
        return self.image.get_rect(topleft = (self.x, self.y))

    def isExploded(self, enemy):
        for bullet in self.bullets:
            if bullet.rect().colliderect(enemy):
                enemy.image = explosionImg
                enemy.isExist = False
                bullet.isExist = False
                self.point += 1


    def displayPoint(self):
        font = pygame.font.SysFont(None, 30)
        text = font.render("Point : " + str(self.point), True, WHITE)
        screen.blit(text, (5, 5))


