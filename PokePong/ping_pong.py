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

pokedex = pygame.image.load('media/pokedex_30_98.png')
pokedex_rect_player1 = pokedex.get_rect()
pokedex_rect_player2 = pokedex.get_rect()

pokedex_width, pokedex_height = pokedex.get_size()

# move to center
pokeball_start_coordinate = [0 + pokedex.get_width(), height/2 - poke_ball.get_height()/2]
pokeball_player2_coordinate = [width - pokedex.get_width(), height/2 - poke_ball.get_height()/2]
poke_ball_rect.move_ip(*pokeball_start_coordinate)


# put pokedex
pokedex_rect_player1.move_ip(0, (height/2 - pokedex_height/2))
pokedex_rect_player2.move_ip(width - pokedex_width, height/2 - pokedex_height/2)

# the game is running?
is_playing = False

# it time to player 1?
turn_player_1 = True

run = True
while run:
    pygame.time.delay(4)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    def move_pokedex(target, impulse, move_pokeball):
        target = target.move(0, impulse)
        if not is_playing and move_pokeball:
            return poke_ball_rect.move(0, impulse), target
        return poke_ball_rect, target

    # move pokedex
    keys = pygame.key.get_pressed()
    move_ball_up = False
    move_ball_down = False

    if keys[pygame.K_UP] and pokedex_rect_player2.top > 0:
        poke_ball_rect, pokedex_rect_player2 = move_pokedex(
            pokedex_rect_player2,
            impulse=-1,
            move_pokeball=not turn_player_1
        )

    if keys[pygame.K_DOWN] and pokedex_rect_player2.bottom < height:
        poke_ball_rect, pokedex_rect_player2 = move_pokedex(
            pokedex_rect_player2,
            impulse=1,
            move_pokeball=not turn_player_1
        )

    if keys[pygame.K_a] and pokedex_rect_player1.top > 0:
        poke_ball_rect, pokedex_rect_player1 = move_pokedex(
            pokedex_rect_player1,
            impulse=-1,
            move_pokeball=turn_player_1
        )
    if keys[pygame.K_z] and pokedex_rect_player1.bottom < height:
        poke_ball_rect, pokedex_rect_player1 = move_pokedex(
            pokedex_rect_player1,
            impulse=1,
            move_pokeball=turn_player_1
        )

    if not is_playing:
        if keys[pygame.K_SPACE]:
            is_playing = True
    else:
        poke_ball_rect = poke_ball_rect.move(speed)

    # check if the player lose
    if poke_ball_rect.left < 0 or poke_ball_rect.right > width:
        is_playing = False
        turn_player_1 = not turn_player_1

        # TODO place pokeball en othder

    # check if pokedex touch the pokeball
    if pokedex_rect_player1.colliderect(poke_ball_rect) or pokedex_rect_player2.colliderect(poke_ball_rect):
        speed[0] = -speed[0]

    # up down window
    if poke_ball_rect.top < 0 or poke_ball_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(poke_ball, poke_ball_rect)
    screen.blit(pokedex, pokedex_rect_player1)
    screen.blit(pokedex, pokedex_rect_player2)
    pygame.display.flip()

pygame.quit()
