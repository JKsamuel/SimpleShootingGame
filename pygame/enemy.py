from config import *

# Enemy
enemyImg = pygame.image.load('img/enemy.jpg')
enemyWidth = 50
enemyImgHeight = 50
enemyImg = pygame.transform.scale(enemyImg, (enemyWidth, enemyImgHeight))
enemyX = (screenWidth - enemyWidth) / 2
enemyY = 0
enemySpeed = 5

enemies = []

class Enemy:
    def __init__(self, image, position):
        self.image = image
        self.x = position[0]
        self.y = position[1]
        self.width = image.get_width()
        self.height = image.get_height()
        self.isExist = True
        self.duration = 0

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.y + enemySpeed > screenHeight:
            self.isExist = False
        else:
            self.y += enemySpeed

    def rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))


# for i in range(5):
    # rand_x = random.randint(0, screenWidth - enemyWidth)
    # enemies.append(Enemy(enemyImg, (rand_x, 0)))
