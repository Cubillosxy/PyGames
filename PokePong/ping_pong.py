import sys
import pygame

pygame.init()

size = width, height = 1000, 600
speed = [1, 1]
black = 255, 255, 255

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Ping Pong - kong ?')

poke_ball = pygame.image.load('media/pokeok.gif')
poke_ball_rect = poke_ball.get_rect()

# move to center
# TODO dynamic
poke_ball_rect.move_ip(width/2, height/2)

#
pokedex = pygame.image.load('media/pokedex_30_98.png')
pokedex2 = pygame.image.load('media/pokedex_30_98.png')
pokedex_rect_player1 = pokedex.get_rect()
pokedex_rect_player2 = pokedex2.get_rect()


pokedex_width, pokedex_height = poke_ball.get_size()


# put pokedex
pokedex_rect_player1.move_ip(0, (height/2 - pokedex_height))
pokedex_rect_player2.move_ip(width - pokedex_width/2 - 5, height/2 - pokedex_height)

run = True
while run:
    pygame.time.delay(4)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # move pokedex
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        pokedex_rect_player2 = pokedex_rect_player2.move(0, -1)

    if keys[pygame.K_DOWN]:
        pokedex_rect_player2 = pokedex_rect_player2.move(0, 1)

    if keys[pygame.K_a]:
        pokedex_rect_player1 = pokedex_rect_player1.move(0, -1)

    if keys[pygame.K_z]:
        pokedex_rect_player1 = pokedex_rect_player1.move(0, 1)

    poke_ball_rect = poke_ball_rect.move(speed)

    # check if the player lose
    if poke_ball_rect.left < 0 or poke_ball_rect.right > width:
        # todo
        pass
        #speed[0] = -speed[0]

    # check if pokedex touch the pokeball
    if pokedex_rect_player1.colliderect(poke_ball_rect) or pokedex_rect_player2.colliderect(poke_ball_rect):
        speed[0] = -speed[0]

    # up down window
    if poke_ball_rect.top < 0 or poke_ball_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(poke_ball, poke_ball_rect)
    screen.blit(pokedex, pokedex_rect_player1)
    screen.blit(pokedex2, pokedex_rect_player2)
    pygame.display.flip()

pygame.quit()