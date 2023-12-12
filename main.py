import pygame as pg
import numpy as np
from numba import njit



class Sprite:
    def __init__(self, screen: pg.Surface, spritepic, x0, y0):
        global posx, posy, rot, maph
        self.screen = screen
        self.x, self.y=x0, y0
        self.diffspritean = 0
        self.spritepic = pg.transform.scale(spritepic, (300, 300))
        self.spritesize = np.asarray(self.spritepic.get_size())
        self.newsprtie = self.spritepic
        self.hor, self.vert = 1000, 1000



    def frame(self):
        self.spritean = np.arctan((self.y - posy) / (self.x - posx))
        if abs(posx + np.cos(self.spritean) - self.x) > abs(posx - self.x):
            self.spritean = (self.spritean - np.pi) % (2 * np.pi)
        self.diffspritean = (rot - self.spritean) % (2 * np.pi)
        if self.diffspritean > 11 * np.pi / 6 or self.diffspritean < np.pi / 6:
            dist = np.sqrt((posx - self.x) ** 2 + (posy - self.y) ** 2)
            cos2 = np.cos(self.diffspritean)
            cos, sin = 0.01 * (posx - self.x) / dist, 0.01 * (posy - self.y) / dist
            x, y = self.x, self.y
            scaling = min(1 / dist, 2) / cos2
            self.vert = 300 + 300 * scaling - scaling * self.spritesize[1]
            self.hor = 400 - 800 * np.sin(self.diffspritean) - scaling * self.spritesize[0] / 2
            self.newsprtie = pg.transform.scale(self.spritepic, scaling * self.spritesize)
            for i in range(int(dist / 0.01)):
                x, y = x + cos, y + sin
                if maph[int(x)][int(y)]:
                    self.hor, self.vert = 1000, 1000
            self.screen.blit(self.newsprtie, (self.hor, self.vert))

class Enemy:
    def __init__(self, screen: pg.Surface, spritesheet, x0, y0):
        global posx, posy, rot, maph, ticks
        self.screen = screen
        self.x, self.y=x0, y0
        self.diffspritean = 0
        self.spritesheet = spritesheet
        self.spritesize = np.asarray(self.spritesheet[0].get_size())
        self.newsprtie = self.spritesheet[0]
        self.hor, self.vert =1000, 1000

        self.alive = True

        self.cycle = 0


    def frame(self):
        self.cycle = int(ticks)%4
        self.spritean = np.arctan((self.y - posy) / (self.x - posx))
        if abs(posx + np.cos(self.spritean) - self.x) > abs(posx - self.x):
            self.spritean = (self.spritean - np.pi) % (2 * np.pi)
        self.diffspritean = (rot - self.spritean) % (2 * np.pi)
        if self.diffspritean > 11 * np.pi / 6 or self.diffspritean < np.pi / 6:
            dist = np.sqrt((posx - self.x) ** 2 + (posy - self.y) ** 2)
            cos2 = np.cos(self.diffspritean)
            cos, sin = 0.01 * (posx - self.x) / dist, 0.01 * (posy - self.y) / dist
            x, y = self.x, self.y
            scaling = min(1 / dist, 2) / cos2
            self.vert = 300 + 300 * scaling - scaling * self.spritesize[1]
            self.hor = 400 - 800 * np.sin(self.diffspritean) - scaling * self.spritesize[0] / 2
            if self.alive:
                self.spritesize = np.asarray(self.spritesheet[self.cycle].get_size())

                self.newsprtie = pg.transform.scale(self.spritesheet[self.cycle], scaling * self.spritesize)
            else:
                self.spritesize = np.asarray(self.spritesheet[4].get_size())

                self.newsprtie = pg.transform.scale(self.spritesheet[4], scaling * self.spritesize)

            for i in range(int(dist / 0.01)):
                x, y = x + cos, y + sin
                if maph[int(x)][int(y)]:
                    self.hor, self.vert = 1000, 1000
            self.screen.blit(self.newsprtie, (self.hor, self.vert))
    def hittest(self):
        self.diffspritean = (rot - self.spritean) % (2 * np.pi)
        if self.diffspritean > 47 * np.pi / 24 or self.diffspritean < np.pi / 24:
            self.alive = False



class Enemy:
    def __init__(self, screen: pg.Surface, spritesheet, x0, y0):
        global posx, posy, rot, maph, ticks
        self.screen = screen
        self.x, self.y = x0, y0
        self.rayx, self.rayy = posx, posy
        self.diffspritean = 0
        self.spritesheet = spritesheet
        self.spritesize = np.asarray(self.spritesheet[0].get_size())
        self.newsprtie = self.spritesheet[0]
        self.hor, self.vert =1000, 1000

        self.alive = True
        self.see = False

        self.cycle = 0


    def frame(self):
        self.cycle = int(ticks)%4
        self.rayx, self.rayy = posx, posy
        self.spritean = np.arctan((self.y - posy) / (self.x - posx))
        if abs(posx + np.cos(self.spritean) - self.x) > abs(posx - self.x):
            self.spritean = (self.spritean - np.pi) % (2 * np.pi)
        self.diffspritean = (rot - self.spritean) % (2 * np.pi)
        if self.diffspritean > 11 * np.pi / 6 or self.diffspritean < np.pi / 6:
            dist = np.sqrt((posx - self.x) ** 2 + (posy - self.y) ** 2)
            cos2 = np.cos(self.diffspritean)
            cos, sin = 0.01 * (posx - self.x) / dist, 0.01 * (posy - self.y) / dist
            x, y = self.x, self.y
            scaling = min(1 / dist, 2) / cos2
            self.vert = 300 + 300 * scaling - scaling * self.spritesize[1]
            self.hor = 400 - 800 * np.sin(self.diffspritean) - scaling * self.spritesize[0] / 2
            if self.alive:
                self.spritesize = np.asarray(self.spritesheet[self.cycle].get_size())

                self.newsprtie = pg.transform.scale(self.spritesheet[self.cycle], scaling * self.spritesize)
            else:
                self.spritesize = np.asarray(self.spritesheet[4].get_size())

                self.newsprtie = pg.transform.scale(self.spritesheet[4], scaling * self.spritesize)
            self.see=True
            for i in range(int(dist / 0.01)):
                x, y = x + cos, y + sin
                if maph[int(x)][int(y)]:
                    self.hor, self.vert = 1000, 1000
                    self.see = False

            self.screen.blit(self.newsprtie, (self.hor, self.vert))
        dist = np.sqrt((posx - self.x) ** 2 + (posy - self.y) ** 2)
        if self.see and self.alive and dist>0.5 and maph[int(self.x)][int(self.y)]==0:
            cos, sin = 0.01 * (posx - self.x) / dist, 0.01 * (posy - self.y) / dist
            self.x += cos
            self.y += sin
            print(maph[int(self.x)][int(self.y)])
        if maph[int(self.x)][int(self.y)] !=0:
            self.x -= 3*cos
            self.y -= 3*sin

    def hittest(self):
        self.diffspritean = (rot - self.spritean) % (2 * np.pi)
        if self.diffspritean > 47 * np.pi / 24 or self.diffspritean < np.pi / 24:
            self.alive = False





class HITLER:
    def __init__(self, screen: pg.Surface, spritesheetH, x0, y0):
        global posx, posy, rot, maph, ticks
        self.screen = screen
        self.x, self.y=x0, y0
        self.diffspritean = 0
        self.spritesheet = spritesheetH
        self.spritesize = np.asarray(self.spritesheet[0].get_size())
        self.newsprtie = self.spritesheet[0]
        self.hor, self.vert = 1000, 1000

        self.alive = True

        self.cycle = 0


    def frame(self):
        self.cycle = int(ticks)%7
        self.spritean = np.arctan((self.y - posy) / (self.x - posx))
        if abs(posx + np.cos(self.spritean) - self.x) > abs(posx - self.x):
            self.spritean = (self.spritean - np.pi) % (2 * np.pi)
        self.diffspritean = (rot - self.spritean) % (2 * np.pi)
        if self.diffspritean > 11 * np.pi / 6 or self.diffspritean < np.pi / 6:
            dist = np.sqrt((posx - self.x) ** 2 + (posy - self.y) ** 2)
            cos2 = np.cos(self.diffspritean)
            cos, sin = 0.01 * (posx - self.x) / dist, 0.01 * (posy - self.y) / dist
            x, y = self.x, self.y
            scaling = min(1 / dist, 2) / cos2
            self.vert = 300 + 300 * scaling - scaling * self.spritesize[1]
            self.hor = 400 - 800 * np.sin(self.diffspritean) - scaling * self.spritesize[0] / 2
            if self.alive:
                self.spritesize = np.asarray(self.spritesheet[self.cycle].get_size())

                self.newsprtie = pg.transform.scale(self.spritesheet[self.cycle], scaling * self.spritesize)
            else:
                self.spritesize = np.asarray(self.spritesheet[7].get_size())

                self.newsprtie = pg.transform.scale(self.spritesheet[7], scaling * self.spritesize)

            for i in range(int(dist / 0.01)):
                x, y = x + cos, y + sin
                if maph[int(x)][int(y)]:
                    self.hor, self.vert = 1000, 1000
            self.screen.blit(self.newsprtie, (self.hor, self.vert))
    def hittest(self):
        self.diffspritean = (rot - self.spritean) % (2 * np.pi)
        if self.diffspritean > 47 * np.pi / 24 or self.diffspritean < np.pi / 24:
            self.alive = False



class GOBLIN:
    def __init__(self, screen: pg.Surface, spritesheetG, x0, y0):
        global posx, posy, rot, maph, ticks
        self.screen = screen
        self.x, self.y=x0, y0
        self.diffspritean = 0
        self.spritesheet = spritesheetG
        self.spritesize = np.asarray(self.spritesheet[0].get_size())
        self.newsprtie = self.spritesheet[0]
        self.hor, self.vert = 1000, 1000

        self.alive = True

        self.cycle = 0


    def frame(self):
        self.cycle = int(ticks)%4
        self.spritean = np.arctan((self.y - posy) / (self.x - posx))
        if abs(posx + np.cos(self.spritean) - self.x) > abs(posx - self.x):
            self.spritean = (self.spritean - np.pi) % (2 * np.pi)
        self.diffspritean = (rot - self.spritean) % (2 * np.pi)
        if self.diffspritean > 11 * np.pi / 6 or self.diffspritean < np.pi / 6:
            dist = np.sqrt((posx - self.x) ** 2 + (posy - self.y) ** 2)
            cos2 = np.cos(self.diffspritean)
            cos, sin = 0.01 * (posx - self.x) / dist, 0.01 * (posy - self.y) / dist
            x, y = self.x, self.y
            scaling = min(1 / dist, 2) / cos2
            self.vert = 300 + 300 * scaling - scaling * self.spritesize[1]
            self.hor = 400 - 800 * np.sin(self.diffspritean) - scaling * self.spritesize[0] / 2
            if self.alive:
                self.spritesize = np.asarray(self.spritesheet[self.cycle].get_size())

                self.newsprtie = pg.transform.scale(self.spritesheet[self.cycle], scaling * self.spritesize)
            else:
                self.spritesize = np.asarray(self.spritesheet[4].get_size())

                self.newsprtie = pg.transform.scale(self.spritesheet[4], scaling * self.spritesize)

            for i in range(int(dist / 0.01)):
                x, y = x + cos, y + sin
                if maph[int(x)][int(y)]:
                    self.hor, self.vert = 1000, 1000
            self.screen.blit(self.newsprtie, (self.hor, self.vert))
    def hittest(self):
        self.diffspritean = (rot - self.spritean) % (2 * np.pi)
        if self.diffspritean > 47 * np.pi / 24 or self.diffspritean < np.pi / 24:
            self.alive = False



class Weapon:
    def __init__(self, screen: pg.Surface, weaponsheet, x0, y0):
        global posx, posy, rot, maph, ticks
        self.screen = screen
        self.diffspritean = 0
        self.weaponsheet = weaponsheet
        self.newsprtie = self.weaponsheet[0]
        self.hor, self.vert = x0, y0
        self.shooting = False

        self.time = 0
        self.cycle = 0

    def frame(self):
        self.newsprtie = self.weaponsheet[0]

        if self.shooting and self.time < 10:
            self.newsprtie = self.weaponsheet[1]
            self.time+=1
        if self.shooting and self.time > 10:
            self.time = 0
            self.shooting=False
            self.newsprtie = self.weaponsheet[0]
        self.screen.blit(self.newsprtie, (self.hor, self.vert))

    def shoot(self):
        self.shooting = True
        self.time = 0





def movement(posx, posy, rot, maph, et):
    pressed_keys = pg.key.get_pressed()
    x, y, diag = posx, posy, rot
    p_mouse = pg.mouse.get_rel()
    rot = rot + np.clip((p_mouse[0]) / 200, -0.2, .2)

    if pressed_keys[pg.K_UP] or pressed_keys[ord('w')]:
        x, y, diag = x + et * np.cos(rot), y + et * np.sin(rot), 1

    elif pressed_keys[pg.K_DOWN] or pressed_keys[ord('s')]:
        x, y, diag = x - et * np.cos(rot), y - et * np.sin(rot), 1

    if pressed_keys[pg.K_LEFT] or pressed_keys[ord('a')]:
        #et = et / (diag + 1)
        x, y = x + et * np.sin(rot), y - et * np.cos(rot)

    elif pressed_keys[pg.K_RIGHT] or pressed_keys[ord('d')]:
        #et = et / (diag + 1)
        x, y = x - et * np.sin(rot), y + et * np.cos(rot)

    if not (maph[int(x - 0.2)][int(y)] or maph[int(x + 0.2)][int(y)] or
            maph[int(x)][int(y - 0.2)] or maph[int(x)][int(y + 0.2)]):
        posx, posy = x, y

    elif not (maph[int(posx - 0.2)][int(y)] or maph[int(posx + 0.2)][int(y)] or
              maph[int(posx)][int(y - 0.2)] or maph[int(posx)][int(y + 0.2)]):
        posy = y

    elif not (maph[int(x - 0.2)][int(posy)] or maph[int(x + 0.2)][int(posy)] or
              maph[int(x)][int(posy - 0.2)] or maph[int(x)][int(posy + 0.2)]):
        posx = x

    return posx, posy, rot


def gen_map(size):
    maph = np.array([[1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1]])
    '''
    maph = np.random.choice([0, 0, 0, 0, 1, 1], (size, size))
    maph[0, :], maph[size - 1, :], maph[:, 0], maph[:, size - 1] = (1, 1, 1, 1)'''
    print(type(maph))
    posx, posy, rot = 1.5, 1.5, np.pi /2

    x, y = int(posx), int(posy)
    maph[x][y] = 0
    count = 0
    while True:
        testx, testy = (x, y)
        if np.random.uniform() > 0.5:
            testx = testx + np.random.choice([-1, 1])
        else:
            testy = testy + np.random.choice([-1, 1])
        if testx > 0 and testx < size - 1 and testy > 0 and testy < size - 1:
            if maph[testx][testy] == 0 or count > 5:
                count = 0
                x, y = (testx, testy)
                maph[x][y] = 0
                if x == size - 2:
                    exitx, exity = (x, y)
                    break
            else:
                count = count + 1
    return posx, posy, rot, maph, exitx, exity


@njit()
def new_frame(posx, posy, rot, frame, sky, floor, hres, halfvres, mod, maph, size, wall, exitx, exity):
    for i in range(hres):
        rot_i = rot + np.deg2rad(i / mod - 30)
        sin, cos, cos2 = np.sin(rot_i), np.cos(rot_i), np.cos(np.deg2rad(i / mod - 30))
        frame[i][:] = sky[int(np.rad2deg(rot_i) % 359)][:]

        x, y = posx, posy
        while maph[int(x) % (size - 1)][int(y) % (size - 1)] == 0:
            x, y = x + 0.01 * cos, y + 0.01 * sin

        n = abs((x - posx) / cos)
        h = int(halfvres / (n * cos2 + 0.001))

        xx = int(x * 3 % 1 * 99)
        if x % 1 < 0.02 or x % 1 > 0.98:
            xx = int(y * 3 % 1 * 99)
        yy = np.linspace(0, 3, h * 2) * 99 % 99







        for k in range(h * 2):
            if halfvres - h + k >= 0 and halfvres - h + k < 2 * halfvres:
                frame[i][halfvres - h + k] = wall[xx][int(yy[k])]


        for j in range(halfvres - h):
            n = (halfvres / (halfvres - j)) / cos2
            x, y = posx + cos * n, posy + sin * n
            xx, yy = int(x * 2 % 1 * 99), int(y * 2 % 1 * 99)


            frame[i][halfvres * 2 - j - 1] = floor[xx][yy]
            if int(x) == exitx and int(y) == exity and (x % 1 - 0.5) ** 2 + (y % 1 - 0.5) ** 2 < 0.2:
                ee = j / (10 * halfvres)
                frame[i][j:2 * halfvres - j] = (ee * np.ones(3) + frame[i][j:2 * halfvres - j]) / (1 + ee)

    return frame

pg.init()
screen = pg.display.set_mode((800, 600))
running = True
clock = pg.time.Clock()
ticks = 0

pg.mouse.set_visible(False)

hres = 200  # horizontal resolution
halfvres = 150  # vertical resolution/2

mod = hres / 60  # scaling factor (60° fov)

size = 8
posx, posy, rot, maph, exitx, exity = gen_map(size)

frame = np.random.uniform(0, 1, (hres, halfvres * 2, 3))
sky = pg.image.load('WALL30.bmp')
sky = pg.surfarray.array3d(pg.transform.scale(sky, (360, halfvres * 2))) / 255
floor = pg.surfarray.array3d(pg.transform.scale(pg.image.load('WALL87.bmp'), (300,300))) / 255
wall = pg.surfarray.array3d(pg.transform.scale(pg.image.load('WALL32.bmp'), (300,300))) / 255
pillarpic = pg.transform.scale(pg.image.load('pillar.png'), (300,300))
enemypic = pg.image.load('27846.png')
enemysheet = [pg.transform.scale(pg.image.load('testenemy/1.png'),(200, 300)), pg.transform.scale(pg.image.load('testenemy/2.png'),(200, 300)), pg.transform.scale(pg.image.load('testenemy/3.png'),(200, 300)), pg.transform.scale(pg.image.load('testenemy/4.png'),(200, 300)) , pg.transform.scale(pg.image.load('testenemy/5.png'),(150, 200))]
enemysheetH = [pg.transform.scale(pg.image.load('HITLER/1.png'),(200, 300)), pg.transform.scale(pg.image.load('HITLER/2.png'),(200, 300)), pg.transform.scale(pg.image.load('HITLER/3.png'),(200, 300)), pg.transform.scale(pg.image.load('HITLER/4.png'),(200, 300)), pg.transform.scale(pg.image.load('HITLER/5.png'),(200, 300)), pg.transform.scale(pg.image.load('HITLER/6.png'),(200, 300)), pg.transform.scale(pg.image.load('HITLER/7.png'),(200, 300)), pg.transform.scale(pg.image.load('HITLER/8.png'),(200, 300))]
enemysheetG = [pg.transform.scale(pg.image.load('enemys/1.png'),(200, 300)), pg.transform.scale(pg.image.load('enemys/2.png'),(200, 300)), pg.transform.scale(pg.image.load('enemys/3.png'),(200, 300)), pg.transform.scale(pg.image.load('enemys/4.png'),(200, 300)), pg.transform.scale(pg.image.load('enemys/5.png'),(200, 300))]

weaponsheet = [pg.transform.scale(pg.image.load('1.png'),(150, 150)), pg.transform.scale(pg.image.load('2.png'),(150, 150))]
weapontest = Weapon(screen,weaponsheet, 350, 450)

e1 = Enemy(screen, enemysheet, 2, 2)
e2 = HITLER(screen, enemysheetH, 5,5)
e3 = GOBLIN(screen, enemysheetG, 4, 2)

pg.event.set_grab(1)
pillar = Sprite(screen, pillarpic, 3,3)
while running:
    ticks = pg.time.get_ticks() / 200
    if int(posx) == exitx and int(posy) == exity:
        print("you got out of the maze!")
        running = False
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            weapontest.shoot()
            e1.hittest()
            e2.hittest()
            e3.hittest()



    frame = new_frame(posx, posy, rot, frame, sky, floor, hres, halfvres, mod, maph, size,
                      wall, exitx, exity)

    surf = pg.surfarray.make_surface(frame * 255)
    surf = pg.transform.scale(surf, (800, 600))
    fps = int(clock.get_fps())
    pg.display.set_caption("Pycasting maze - FPS: " + str(fps))

    screen.blit(surf, (0, 0))

    '''toiletan = np.arctan((toilety - posy)/(toiletx - posx))
        if abs(posx+np.cos(toiletan) -toiletx) > abs(posx - toiletx):
            toiletan = (toiletan - np.pi)%(2*np.pi)
        difftoiletan = (rot - toiletan)%(2*np.pi)
        if difftoiletan > 11*np.pi/6 or difftoiletan < np.pi/6:
            dist = np.sqrt((posx-toiletx)**2 + (posy- toilety)**2)
            cos2 = np.cos(difftoiletan)
            cos, sin = 0.01*(posx - toiletx)/dist, 0.01*(posy - toilety)/dist
            x, y = toiletx, toilety
            scaling = min(1/dist, 2) / cos2
            vert = 300 + 300*scaling - scaling*toiletsize[1]/2
            hor = 400 - 800*np.sin(difftoiletan)- scaling*toiletsize[0]/2
            toiletnew = pg.transform.scale(toilet, scaling*toiletsize)
            for i in range(int(dist/0.01)):
                x, y = x+cos, y+sin
                if maph[int(x)][int(y)]:
                    toiletnew = pg.transform.scale(toilet, (0,0))
            screen.blit(toiletnew, (hor, vert))'''

    pillar.frame()
    e1.frame()
    e2.frame()
    e3.frame()
    weapontest.frame()
    pg.display.update()

    posx, posy, rot = movement(posx, posy, rot, maph, 0.04)
    clock.tick(60)

pg.quit()