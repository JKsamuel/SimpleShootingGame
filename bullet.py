from config import *


bulletImgWidth = 7
bulletImgHeigt = 20
bulletImg = pygame.image.load('img/bullet.jpg')
bulletImg = pygame.transform.scale(bulletImg, (bulletImgWidth, bulletImgHeigt))
bulletSpeed = 6


class Bullet:
    def __init__(self, image, position):
        self.image = image
        self.x = position[0]
        self.y = position[1]
        self.width = image.get_width()
        self.height = image.get_height()
        self.isExist = True

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.y - bulletSpeed == 0:
            self.isExist = False
        else:
            self.y -= bulletSpeed

    def rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))
