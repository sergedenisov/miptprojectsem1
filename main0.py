import pygame
import sys
import math

#global const
SCREEN_HEIGHT = 480
SCREEN_WIDTH = SCREEN_HEIGHT*2
MAP_SIZE = 8
TILE_SIZE = int((SCREEN_WIDTH / 2) / MAP_SIZE)
FOV = math.pi / 3
HALF_FOV = FOV / 2
CASTED_RAYS = 120
STEP_ANGLE = FOV / CASTED_RAYS
MAX_DEPTH = int(MAP_SIZE * TILE_SIZE)
SCALE = (SCREEN_WIDTH / 2) / CASTED_RAYS

#global var
player_x = int(SCREEN_HEIGHT / 4)
player_y = int(SCREEN_HEIGHT / 4)
player_an = math.pi
player_speed = 3

dog_surf = pygame.image.load('WALL32.bmp')
dog_surf = pygame.transform.scale(dog_surf, (512, 512))

#MAP
MAP = (
    '11111111'
    '10001001'
    '10000001'
    '10010001'
    '10001001'
    '10000001'
    '10000101'
    '11111111'
)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Reycasting')

clock = pygame.time.Clock()

def draw_map():
    #map
    for row in range(MAP_SIZE):
        for col in range(MAP_SIZE):
            square = row * MAP_SIZE + col

            pygame.draw.rect(
                screen,
                (200, 200, 200) if MAP[square] == '1' else (100, 100, 100),
                (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE-2, TILE_SIZE-2)
            )
    pygame.draw.rect(screen, (180, 180, 180), (SCREEN_WIDTH/2, 0 , SCREEN_WIDTH, SCREEN_HEIGHT/2))
    pygame.draw.rect(screen, (100, 100, 100), (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 , SCREEN_WIDTH, SCREEN_HEIGHT))

    #payer
    pygame.draw.circle(screen, (255, 0, 0), (player_x, player_y), 8)
    pygame.draw.line(screen, (0, 255, 0), (player_x, player_y), (player_x - math.sin(player_an)*20, player_y + math.cos(player_an)*20), 3)
    #player fov
    pygame.draw.line(screen, (0, 255, 0), (player_x, player_y), (player_x - math.sin(player_an-HALF_FOV)*20, player_y + math.cos(player_an-HALF_FOV)*20), 3)
    pygame.draw.line(screen, (0, 255, 0), (player_x, player_y), (player_x - math.sin(player_an+HALF_FOV)*20, player_y + math.cos(player_an+HALF_FOV)*20), 3)

def cast_rays():
    start_an = player_an - HALF_FOV
    for ray in range(CASTED_RAYS):
        for depth in range(MAX_DEPTH):
            target_x = player_x - math.sin(start_an)*depth
            target_y = player_y + math.cos(start_an)*depth

            col = int(target_x / TILE_SIZE)
            row = int(target_y / TILE_SIZE)

            pic_x = player_x + depth*math.sin(player_an - math.pi) - (TILE_SIZE * col)

            square = row * MAP_SIZE + col
            if MAP[square] == '1':


                pygame.draw.line(screen, (0, 255, 0), (player_x, player_y), (target_x, target_y))

                #wall
                depth *= math.cos(player_an - start_an)
                wall_height = 21000/ (depth+0.000001)
                if wall_height > SCREEN_HEIGHT: wall_height = SCREEN_HEIGHT
                color = 255/ (1 + depth * depth * 0.0001)

                tile = pygame.transform.scale(dog_surf, (512, wall_height))

                section = tile.subsurface(target_x % TILE_SIZE, 0, SCALE, wall_height)

                screen.blit(section, (SCREEN_HEIGHT + ray * SCALE, (SCREEN_HEIGHT / 2) - wall_height / 2))

                #pygame.draw.rect(screen, (color, color, color), (SCREEN_HEIGHT + ray * SCALE, (SCREEN_HEIGHT / 2) - wall_height / 2, SCALE, wall_height))
                print(target_x, target_y, depth)

                break
        start_an += STEP_ANGLE

forward = True

while True:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    col = int(player_x / TILE_SIZE)
    row = int(player_y / TILE_SIZE)

    square = row * MAP_SIZE + col
    if MAP[square] == '1':
        if forward:
            player_x -= -math.sin(player_an) * player_speed
            player_y -= math.cos(player_an) * player_speed
        else:
            player_x += -math.sin(player_an) * player_speed
            player_y += math.cos(player_an) * player_speed

    draw_map()
    cast_rays()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_an -= 0.1
    if keys[pygame.K_RIGHT]: player_an += 0.1
    if keys[pygame.K_UP]:
        forward = True
        player_x += -math.sin(player_an) * player_speed
        player_y += math.cos(player_an) * player_speed
    if keys[pygame.K_DOWN]:
        forward = False
        player_x -= -math.sin(player_an) * player_speed
        player_y -= math.cos(player_an) * player_speed


    clock.tick(60)
    fps = str(int(clock.get_fps()))
    font = pygame.font.SysFont('Comic Sans', 30)
    fps_surface = font.render(fps, False, (255, 255, 255))
    screen.blit(fps_surface, (0,0))

    pygame.display.flip()
