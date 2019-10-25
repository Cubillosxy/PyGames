import sys
import pygame

pygame.init()

size = width, height = 1000, 600
start_speed = 8
speed = [start_speed, start_speed]
white = 255, 255, 255
black = 0, 0, 0
green = (0, 255, 0)
blue = (0, 0, 128)
red_poke = 222, 109, 103

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
pokeball_player2_coordinate = [width - pokedex.get_width() - poke_ball.get_width(), height/2 - poke_ball.get_height()/2]
poke_ball_rect.move_ip(*pokeball_start_coordinate)


# put pokedex
pokedex_rect_player1.move_ip(0, (height/2 - pokedex_height/2))
pokedex_rect_player2.move_ip(width - pokedex_width, height/2 - pokedex_height/2)

# the game is running?
is_playing = False

# it time to player 1?
turn_player_1 = True

# text
font = pygame.font.Font('freesansbold.ttf', 30)
text_container_p1 = font.render('0', True, red_poke, white)
text_container_p2 = font.render('0', True, red_poke, white)

text_score_1 = text_container_p1.get_rect()
text_score_2 = text_container_p2.get_rect()
score_player1 = 0
score_player2 = 0

span_text = 120
text_score_1.center = (width/2 - span_text, 15)
text_score_2.center = (width/2 + span_text, 15)

counter_shots = 0
delay_value = 15
impulse_pokedex = start_speed
run = True
while run:
    pygame.time.delay(delay_value)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    def move_pokedex(target, impulse, move_pokeball):
        target = target.move(0, impulse)
        if not is_playing and move_pokeball:
            return poke_ball_rect.move(0, impulse), target
        return poke_ball_rect, target

    def set_pokeball(turn_player, score_p1, score_p2):
        new_pokeball = poke_ball.get_rect()
        # win p1 , put the ball in player 2 side
        if turn_player:
            score_p1 += 1
            _height = (pokedex_rect_player2.top + pokedex_rect_player2.bottom) / 2
            _weight = pokeball_player2_coordinate[0]
        else:
            _height = (pokedex_rect_player1.top + pokedex_rect_player1.bottom) / 2
            _weight = pokeball_start_coordinate[0]
            score_p2 += 1
        text_p1 = font.render(str(score_p1), True, red_poke, white)
        text_p2 = font.render(str(score_p2), True, red_poke, white)
        text_rect_p1 = text_p1.get_rect()
        text_rect_p2 = text_p2.get_rect()
        text_rect_p1.center = (width / 2 - span_text, 15)
        text_rect_p2.center = (width / 2 + span_text, 15)
        new_pokeball.move_ip(_weight, _height - poke_ball.get_height()/2)
        return new_pokeball, not turn_player, score_p1, score_p2, text_p1, text_p2

    # move pokedex
    keys = pygame.key.get_pressed()
    move_ball_up = False
    move_ball_down = False

    if keys[pygame.K_UP] and pokedex_rect_player2.top > 0:
        poke_ball_rect, pokedex_rect_player2 = move_pokedex(
            pokedex_rect_player2,
            impulse=-impulse_pokedex,
            move_pokeball=not turn_player_1
        )

    if keys[pygame.K_DOWN] and pokedex_rect_player2.bottom < height:
        poke_ball_rect, pokedex_rect_player2 = move_pokedex(
            pokedex_rect_player2,
            impulse=impulse_pokedex,
            move_pokeball=not turn_player_1
        )

    if keys[pygame.K_a] and pokedex_rect_player1.top > 0:
        poke_ball_rect, pokedex_rect_player1 = move_pokedex(
            pokedex_rect_player1,
            impulse=-impulse_pokedex,
            move_pokeball=turn_player_1
        )
    if keys[pygame.K_z] and pokedex_rect_player1.bottom < height:
        poke_ball_rect, pokedex_rect_player1 = move_pokedex(
            pokedex_rect_player1,
            impulse=impulse_pokedex,
            move_pokeball=turn_player_1
        )

    if keys[pygame.K_p]:
        print('counter: ', counter_shots)
        print('turn:', turn_player_1, ' is playing: ', is_playing)

    if not is_playing:
        if keys[pygame.K_SPACE]:
            if keys[pygame.K_a] or keys[pygame.K_UP]:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif keys[pygame.K_z] or keys[pygame.K_DOWN]:
                speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
            is_playing = True
    else:
        poke_ball_rect = poke_ball_rect.move(speed)

    # check if the player lose
    if poke_ball_rect.left < 0 or poke_ball_rect.right > width:
        is_playing = False
        poke_ball_rect, turn_player_1, score_player1, score_player2, text_container_p1, text_container_p2 = set_pokeball(
            turn_player_1,
            score_p1=score_player1,
            score_p2=score_player2,
        )
        speed[0] = -speed[0]

        # set speed to half
        if abs(speed[0]) > 1:
            speed = [i/2 for i in speed]
            if speed[0] < start_speed:
                speed[0] = start_speed
                speed[1] = start_speed

    # check if pokedex touch the pokeball
    if pokedex_rect_player1.colliderect(poke_ball_rect) or pokedex_rect_player2.colliderect(poke_ball_rect):
        speed[0] = -speed[0]
        counter_shots += 1
        if counter_shots % 2 == 0:
            speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1

    # up down window
    if poke_ball_rect.top < 0 or poke_ball_rect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(white)
    screen.blit(poke_ball, poke_ball_rect)
    screen.blit(pokedex, pokedex_rect_player1)
    screen.blit(pokedex, pokedex_rect_player2)
    screen.blit(text_container_p1, text_score_1)
    screen.blit(text_container_p2, text_score_2)
    pygame.display.flip()

pygame.quit()
