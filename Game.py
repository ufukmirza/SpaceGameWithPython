import random

import pygame

# init
pygame.init()

# game starting ship coordinats
player_x = 400
player_y = 500
player_x_change = 0
game_over=False
last_over=False

# game starting enemy coordinats
enemy_x = random.randint(0, 750)
enemy_y = random.randint(50, 80)
goal = False

# screen and frame settings
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game")

# ship player
player_image = pygame.image.load('space-invaders.png')

# alien enemy
enemy_image = pygame.image.load('alien.png')
enemy_dead=False

# background
background = pygame.image.load('space-galaxy-background.jpg')

# for bullet
bullet_image = pygame.image.load('bullet.png')
is_fire = False
bullet_x = 0
bullet_y = 0
bullet_rights=5


def show_player(player_x, player_y):
    screen.blit(player_image, (player_x, player_y))


def show_enemy():
    screen.blit(enemy_image, (enemy_x, enemy_y))


def bullet_fire(bullet_x, bullet_y):
        screen.blit(bullet_image, (bullet_x, bullet_y))



# game running
running = True
while running == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # player movement

            if event.key == pygame.K_LEFT:
                player_x_change = -0.1
            if event.key == pygame.K_RIGHT:
                player_x_change = +0.1
            if event.key == pygame.K_SPACE:
                if is_fire == False:
                    is_fire = True
                    bullet_x = player_x
                    bullet_y = player_y - 5
                    bullet_rights-=1
                   #print(str(bullet_x) + "  " + str(bullet_y))

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    if player_x >= 0 and player_x <= 750:
        player_x += player_x_change
    else:
        if player_x < 0:
            player_x = 0
        if player_x > 750:
            player_x = 750

    # enemy movement
    if enemy_x >= 0 and enemy_x <= 750:
        if (goal == False):
            random_number = random.randint(0, 750)
            # print(random_number)
            goal = True
        if goal == True and enemy_x > float(random_number):
            #   print(enemy_x)
            move_x = -0.1
            enemy_x += move_x
        if goal == True and enemy_x < float(random_number):
            #   print(enemy_x)
            move_x = 0.1
            enemy_x += move_x
        if goal == True and enemy_x > (float(random_number) - 1) and enemy_x < (float(random_number) + 1):
            # print(goal)
            goal = False
    else:
        if enemy_x < 0:
            enemy_x = 0
        if enemy_x > 750:
            enemy_x = 750

    # fire and bullet
    # if is_fire == True:
    # bullet_y -= 0.3
    # bullet_fire(bullet_x, bullet_y)
    # if bullet_y < 0:
    # is_fire = False

    if  enemy_x-15<bullet_x and  bullet_x < enemy_x+ 15:
         if enemy_y-5<bullet_y and  bullet_y < enemy_y+ 5:
             enemy_dead=True
             print("gggg")


    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    if is_fire == True:
        bullet_y -= 2
        bullet_fire(bullet_x,bullet_y)
        if bullet_y<0 :
             is_fire=False
             if bullet_rights< 0:
                game_over=True
    if enemy_dead==False:
       show_enemy()
    myfont = pygame.font.SysFont(None, 20)
    myOver=  pygame.font.SysFont(None, 100)
    mytext = myfont.render('bullet number:'+str(bullet_rights), 1, (255, 100, 100))
    gameover_text=myOver.render('Game Over', 1, (255, 255, 255))
    screen.blit(mytext,(10,10))
    show_player(player_x, player_y)
    if game_over==False and enemy_dead==False:
      pygame.display.update()
    if game_over==True and enemy_dead==False:
            if last_over==False:
                screen.blit(gameover_text,(250,270))
                last_over=True
                pygame.display.update()
    if enemy_dead==True:
        if last_over == False:
            wintext=myOver.render('YOU WIN', 1, (255, 255, 255))
            screen.blit(wintext, (250, 270))
            last_over = True
            pygame.display.update()