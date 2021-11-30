from config import *
from Player import *
from enemy import *
from bullet import *
import random

players = []
players.append(Player(playerImg, (playerX, playerY)))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(30 * 0.01)

# Game Loop
running = True
while running:
    pygame.time.delay(10)
    # setting RGB
    # screen.fill((0, 255, 0))
    screen.blit(bgImg, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.draw.rect(screen, WHITE, (screenWidth - players[0].hp - 5, 5, players[0].hp, 10))
    players[0].displayPoint()

    keys = pygame.key.get_pressed()

    for player in players:
        player.draw()
        if player.isExist == False:
             players.remove(players[1])
        players[0].move(keys)

    if random.randint(1, 10) == 1:
        rand_x = random.randint(0, screenWidth - enemyWidth)
        enemies.append(Enemy(enemyImg, (rand_x, 0)))

    for enemy in enemies:
        enemy.move()
        enemy.draw()

        if enemy.isExist == False:
            enemy.duration += 1

            if enemy.duration % 10 == 0:
                enemies.remove(enemy)

        if enemy.rect().colliderect(players[0].rect()):
            if players[0].hp <= 0:
                players[0].hp = 0
            else:
                players[0].hp -= 5

        players[0].isExploded(enemy)



    pygame.display.update()

pygame.quit()