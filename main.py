import random

import pygame as pg
import numpy as np
from numba import njit
from random import randint as rnd



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
        cos, sin = 0.01 * (posx - self.x) / dist, 0.01 * (posy - self.y) / dist
        if self.see and self.alive and dist>0.5 and maph[int(self.x)][int(self.y)]==0:
            cos, sin = 0.01 * (posx - self.x) / dist, 0.01 * (posy - self.y) / dist
            self.x += cos
            self.y += sin

        if maph[int(self.x)][int(self.y)] !=0:
            self.x -= 3*cos
            self.y -= 3*sin

    def hittest(self):
        self.diffspritean = (rot - self.spritean) % (2 * np.pi)
        if self.diffspritean > 47 * np.pi / 24 or self.diffspritean < np.pi / 24:
            self.alive = False
    def distance(self):
        return np.sqrt((posx - self.x) ** 2 + (posy - self.y) ** 2)
    def isalive(self):
        return self.alive




class HITLER:
    def __init__(self, screen: pg.Surface, spritesheetH, x0, y0):
        global posx, posy, rot, maph, ticks
        self.screen = screen
        self.x, self.y=x0, y0
        self.health = 5
        self.diffspritean = 0
        self.spritesheet = spritesheetH
        self.spritesize = np.asarray(self.spritesheet[0].get_size())
        self.newsprtie = self.spritesheet[0]
        self.hor, self.vert = 1000, 1000

        self.angle = 0


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
        if self.alive:
            self.move_circle()

    def move_circle(self):

        center_x, center_y = 7, 6

        radius = 0.5

        self.angle += np.radians(1)
        self.angle %= 2 * np.pi

        self.x = center_x + radius * np.cos(self.angle)
        self.y = center_y + radius * np.sin(self.angle)


    def hittest(self):
        self.diffspritean = (rot - self.spritean) % (2 * np.pi)
        if self.diffspritean > 47 * np.pi / 24 or self.diffspritean < np.pi / 24:
            self.health -= 1
        if self.health == 0:
            self.alive = False



class GOBLIN:
    def __init__(self, screen: pg.Surface, spritesheetG, x0, y0):
        global posx, posy, rot, maph, ticks
        self.screen = screen
        self.x, self.y=x0, y0
        self.health = 2
        self.diffspritean = 0
        self.spritesheet = spritesheetG
        self.spritesize = np.asarray(self.spritesheet[0].get_size())
        self.newsprtie = self.spritesheet[0]
        self.hor, self.vert = 1000, 1000

        self.alive = True
        self.see = True
        self.standing = True
        self.shooting = False

        self.time = 0

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
                if self.standing:
                    self.spritesize = np.asarray(self.spritesheet[0].get_size())
                    self.newsprtie = pg.transform.scale(self.spritesheet[0], scaling * self.spritesize)
                    self.time+=1
                    if self.time >= 120:
                        self.shooting = True
                        self.time = 0
                    if self.time <20 and self.shooting:
                        self.spritesize = np.asarray(self.spritesheet[5].get_size())
                        self.newsprtie = pg.transform.scale(self.spritesheet[5], scaling * self.spritesize)
                    if self.time >=20 and self.shooting:
                        self.shooting = False
                        self.time = 0


                else:
                    self.spritesize = np.asarray(self.spritesheet[self.cycle].get_size())
                    self.newsprtie = pg.transform.scale(self.spritesheet[self.cycle], scaling * self.spritesize)
            else:
                self.spritesize = np.asarray(self.spritesheet[4].get_size())
                self.newsprtie = pg.transform.scale(self.spritesheet[4], scaling * self.spritesize)

            self.see = True

            for i in range(int(dist / 0.01)):
                x, y = x + cos, y + sin
                if maph[int(x)][int(y)]:
                    self.hor, self.vert = 1000, 1000
                    self.see = False
            self.screen.blit(self.newsprtie, (self.hor, self.vert))

        dist = np.sqrt((posx - self.x)**2 + (posy - self.y)**2)
        cos, sin = 0.01 * (posx - self.x) / dist, 0.01 * (posy - self.y) / dist
        if self.see and self.alive and dist > 1.5 and maph[int(self.x)][int(self.y)] == 0:
            self.x += cos
            self.y += sin
            self.standing = False

        if dist <= 1.5:
            self.standing = True
        if maph[int(self.x)][int(self.y)] != 0:
            self.x -= 3 * cos
            self.y -= 3 * sin
    def isshooting(self):
        return self.shooting
    def isalive(self):
        return self.alive
    def distance(self):
        return np.sqrt((posx - self.x) ** 2 + (posy - self.y) ** 2)


            





    def hittest(self):
        self.diffspritean = (rot - self.spritean) % (2 * np.pi)
        if self.diffspritean > 47 * np.pi / 24 or self.diffspritean < np.pi / 24:
            self.health -=1
        if self.health == 0:
            self.alive = False



class Weapon:
    def __init__(self, screen: pg.Surface, weaponsheet_dict, x0, y0):
        self.screen = screen
        self.weaponsheet_dict = weaponsheet_dict
        self.current_weapon = '2'
        self.newsprites = self.weaponsheet_dict[self.current_weapon]
        self.newsprtie = self.newsprites[0]
        self.hor, self.vert = x0, y0
        self.shooting = False

        self.time = 0
        self.cycle = 0

    def change_weapon(self, weapon_id):
        print(f"Переключение на оружие {weapon_id}")
        self.current_weapon = weapon_id
        self.newsprites = self.weaponsheet_dict[weapon_id]

    def frame(self):
        if self.shooting and self.time < 10:
            self.newsprtie = self.newsprites[1]
            self.time += 1
        elif self.shooting and self.time >= 10:
            self.time = 0
            self.shooting = False
            self.newsprtie = self.newsprites[0]

        self.newsprtie = self.newsprites[0 if not self.shooting else 1]
        self.screen.blit(self.newsprtie, (self.hor, self.vert))

    def shoot(self):
        self.shooting = True
        self.time = 0

class Medicine(Sprite):
    def reposition(self):
        self.x = rnd (1, 19)
        self.y = rnd (1, 19)
class Barrel(Medicine):
    pass



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


def gen_map2(size):
    maph = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ])
    '''
    maph = np.random.choice([0, 0, 0, 0, 1, 1], (size, size))
    maph[0, :], maph[size - 1, :], maph[:, 0], maph[:, size - 1] = (1, 1, 1, 1)'''

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

def gen_map(size):
    maph = np.array([[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 2, 2, 0, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2],
            [2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 2, 0, 2, 0, 0, 0, 2, 2, 3, 2, 2, 2, 2, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 3, 2, 2, 0, 0, 3, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 0, 2, 2, 4, 2, 4, 2, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 3, 0, 0, 0, 0, 0, 4, 0, 0, 2, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 3, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 0, 2],
            [2, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
            ])
    '''
    maph = np.random.choice([0, 0, 0, 0, 1, 1], (size, size))
    maph[0, :], maph[size - 1, :], maph[:, 0], maph[:, size - 1] = (1, 1, 1, 1)'''

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
def new_frame(posx, posy, rot, frame, sky, floor, hres, halfvres, mod, maph, size, walls, exitx, exity):
    for i in range(hres):
        walltype = 1
        rot_i = rot + np.deg2rad(i / mod - 30)
        sin, cos, cos2 = np.sin(rot_i), np.cos(rot_i), np.cos(np.deg2rad(i / mod - 30))
        frame[i][:] = sky[int(np.rad2deg(rot_i) % 359)][:]

        x, y = posx, posy
        while maph[int(x) % (size - 1)][int(y) % (size - 1)] == 0:
            x, y = x + 0.01 * cos, y + 0.01 * sin
        walltype = maph[int(x) % (size - 1)][int(y) % (size - 1)]



        n = abs((x - posx) / cos)
        h = int(halfvres / (n * cos2 + 0.001))

        xx = int(x * 3 % 1 * 99)
        if x % 1 < 0.02 or x % 1 > 0.98:
            xx = int(y * 3 % 1 * 99)
        yy = np.linspace(0, 3, h * 2) * 99 % 99







        for k in range(h * 2):
            if halfvres - h + k >= 0 and halfvres - h + k < 2 * halfvres:
                frame[i][halfvres - h + k] = walls[walltype-1][xx][int(yy[k])]


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

size = 20
posx, posy, rot, maph, exitx, exity = gen_map(size)
health = 100
pg.font.init()
font = pg.font.SysFont('Comic Sans MS', 30)
hptext = font.render('HP: %d' % health, False, (0, 0, 0))

frame = np.random.uniform(0, 1, (hres, halfvres * 2, 3))
sky = pg.image.load('WALL30.bmp')
sky = pg.surfarray.array3d(pg.transform.scale(sky, (360, halfvres * 2))) / 255
floor = pg.surfarray.array3d(pg.transform.scale(pg.image.load('WALL87.bmp'), (300,300))) / 255
wall = pg.surfarray.array3d(pg.transform.scale(pg.image.load('WALL32.bmp'), (300,300))) / 255
wall1 = pg.surfarray.array3d(pg.transform.scale(pg.image.load('wall1.png'), (300,300))) / 255
grass = pg.surfarray.array3d(pg.transform.scale(pg.image.load('grass.png'), (300,300))) / 255
hwall = pg.surfarray.array3d(pg.transform.scale(pg.image.load('HWALL.jpg'), (300,300))) / 255
wsw = pg.surfarray.array3d(pg.transform.scale(pg.image.load('WSW.png'), (300,300))) / 255
walls = [wall, wall1, hwall, wsw]
pillarpic = pg.transform.scale(pg.image.load('pillar.png'), (300,300))
barrelpic = pg.transform.scale(pg.image.load('barrel.png'), (300,300))
medicinepic = pg.transform.scale(pg.image.load('medicine.png'), (300,300))
enemypic = pg.image.load('27846.png')
enemysheet = [pg.transform.scale(pg.image.load('testenemy/1.png'),(200, 300)), pg.transform.scale(pg.image.load('testenemy/2.png'),(200, 300)), pg.transform.scale(pg.image.load('testenemy/3.png'),(200, 300)), pg.transform.scale(pg.image.load('testenemy/4.png'),(200, 300)) , pg.transform.scale(pg.image.load('testenemy/5.png'),(150, 200))]
enemysheetH = [pg.transform.scale(pg.image.load('HITLER/1.png'),(400, 600)), pg.transform.scale(pg.image.load('HITLER/2.png'),(400, 600)), pg.transform.scale(pg.image.load('HITLER/3.png'),(400, 600)), pg.transform.scale(pg.image.load('HITLER/4.png'),(400, 600)), pg.transform.scale(pg.image.load('HITLER/5.png'),(400, 600)), pg.transform.scale(pg.image.load('HITLER/6.png'),(400, 600)), pg.transform.scale(pg.image.load('HITLER/7.png'),(400, 600)), pg.transform.scale(pg.image.load('HITLER/8.png'),(400, 600))]
enemysheetG = [pg.transform.scale(pg.image.load('enemys/1.png'),(200, 300)), pg.transform.scale(pg.image.load('enemys/2.png'),(200, 300)), pg.transform.scale(pg.image.load('enemys/3.png'),(200, 300)), pg.transform.scale(pg.image.load('enemys/4.png'),(200, 300)), pg.transform.scale(pg.image.load('enemys/5.png'),(200, 300)), pg.transform.scale(pg.image.load('enemys/7.png'),(200, 300))]

"""weaponsheet = [pg.transform.scale(pg.image.load('1.png'),(150, 150)), pg.transform.scale(pg.image.load('2.png'),(150, 150))]
weapontest = Weapon(screen,weaponsheet, 350, 450)"""

weaponsheet1 = [pg.transform.scale(pg.image.load('1A.png'), (150, 150)),pg.transform.scale(pg.image.load('2A.png'), (150, 150))]

weaponsheet2 = [pg.transform.scale(pg.image.load('1B.png'), (150, 150)),pg.transform.scale(pg.image.load('2B.png'), (150, 150))]

weapons_dict = {
    '1': weaponsheet1,
    '2': weaponsheet2
}

weapon = Weapon(screen, weapons_dict, 350, 450)

e1 = Enemy(screen, enemysheet, 2, 2)
e2 = HITLER(screen, enemysheetH, 20,20)
e3 = GOBLIN(screen, enemysheetG, 4, 2)

enemylist1 = [Enemy(screen, enemysheet, 2, 9), Enemy(screen, enemysheet, 1, 9), Enemy(screen, enemysheet, 2, 4), Enemy(screen, enemysheet, 18, 18), Enemy(screen, enemysheet, 6, 18), Enemy(screen, enemysheet, 6, 7), Enemy(screen, enemysheet, 18, 13), Enemy(screen, enemysheet, 18, 7), GOBLIN(screen, enemysheetG, 13, 9), GOBLIN(screen, enemysheetG, 14, 2), GOBLIN(screen, enemysheetG, 11, 9), GOBLIN(screen, enemysheetG, 11, 18)]

pg.event.set_grab(1)
pillar = Sprite(screen, pillarpic, 3,3)
barrel1 = Barrel(screen, barrelpic, rnd(1, 19), rnd(1, 19))
barrel2 = Barrel(screen, barrelpic, rnd(1, 19), rnd(1, 19))
barrel3 = Barrel(screen, barrelpic, rnd(1, 19), rnd(1, 19))
medicine1 = Medicine(screen, medicinepic, rnd(1, 19), rnd(1, 19))
medicine2 = Medicine(screen, medicinepic, rnd(1, 19), rnd(1, 19))
medicine3 = Medicine(screen, medicinepic, rnd(1, 19), rnd(1, 19))
barreles=[barrel1, barrel2, barrel3]
medicines=[medicine1, medicine2, medicine3]

globaltime = 0
runningmenu = True
menu1 = font.render('RayCasting игра "Одолей фашизм!"', False, (0, 0, 0))
menu2 = font.render('Нажмите на пробел для того, чтобы начать игру.', False, (0, 0, 0))
menu3 = font.render('Авторы игры: Денисов Сергей Б02-309,', False, (0, 0, 0))
menu4 = font.render('Наумов Максим Б02-301,', False, (0, 0, 0))
menu5 = font.render('Стефанов Никита Б02-302', False, (0, 0, 0))
menu6 = font.render('Нажмите на esc чтобы выйти из игры.', False, (0, 0, 0))


pg.mixer.music.load('Was_wollen_wir_trinken.mp3')
pg.mixer.music.play()

while runningmenu:
    screen.fill((255, 0,0))
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            runningmenu = False
            running = True
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            runningmenu = False
            running = False


    screen.blit(menu1, (160, 50))
    screen.blit(menu2, (50, 150))
    screen.blit(menu3, (10, 350))
    screen.blit(menu4, (220, 400))
    screen.blit(menu5, (220, 450))
    screen.blit(menu6, (50, 520))


    pg.display.update()
while running:
    ticks = pg.time.get_ticks() / 200
    globaltime+=1
    globaltime%=60

    if int(posx) == exitx and int(posy) == exity:
        print("you got out of the maze!")
        running = False
    if health <=0:
        deathscreen = True
        menu1 = font.render('RayCasting игра "Одолей фашизм!"', False, (0, 0, 0))
        menu2 = font.render('ВАС УБИЛИ!', False, (0, 0, 0))
        menu3 = font.render('Нажмите пробел чтобы возродиться.', False, (0, 0, 0))
        menu4 = font.render('Нажмите esc чтобы выйти.', False, (0, 0, 0))

        while deathscreen:
            screen.fill((255, 0, 0))
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    deathscreen = False
                    running = True
                    health=100
                if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    running = False
                    deathscreen = False

            screen.blit(menu1, (160, 50))
            screen.blit(menu2, (300, 150))
            screen.blit(menu3, (50, 450))
            screen.blit(menu4, (50, 500))

            pg.display.update()
    for k in medicines:
        if (posx - k.x) ** 2 + (posy - k.y) ** 2 <= 1:
            health += rnd(5, 30)
            k.reposition()
    for m in barreles:
        if (posx - m.x) ** 2 + (posy - m.y) ** 2 <= 1:
            health -= rnd(10, 50)
            m.reposition()

    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                weapon.change_weapon('1')
            elif event.key == pg.K_2:
                weapon.change_weapon('2')

        if event.type == pg.MOUSEBUTTONDOWN:
            weapon.shoot()
            for i in enemylist1:
                i.hittest()
            e1.hittest()
            e3.hittest()



    frame = new_frame(posx, posy, rot, frame, sky, floor, hres, halfvres, mod, maph, size,
                      walls, exitx, exity)

    surf = pg.surfarray.make_surface(frame * 255)
    surf = pg.transform.scale(surf, (800, 600))
    fps = int(clock.get_fps())
    pg.display.set_caption("Pycasting maze - FPS: " + str(fps))

    screen.blit(surf, (0, 0))

    for i in enemylist1:
        i.frame()
        if type(i) == Enemy:
            if i.isalive() and i.distance() <= 1 and globaltime % 20 == 0:
                health -= 1
        if type(i) == GOBLIN:
            if i.isshooting() and i.isalive() and i.distance() <=1.5:
                # if random.Random(10) == 1:
                health -= 0.5




    pillar.frame()
    barrel1.frame()
    barrel2.frame()
    barrel3.frame()
    medicine1.frame()
    medicine2.frame()
    medicine3.frame()
    e1.frame()
    e3.frame()
    weapon.frame()

    if e1.isalive() and e1.distance() <= 1 and globaltime%20 == 0:
        health -= 1
    if e3.isshooting() and e3.isalive() and e3.distance()<=1.5:
        #if random.Random(10) == 1:
       health -=0.5

    hptext = font.render('HP: %d' % health, False, (0, 0, 0))

    screen.blit(hptext, (20, 550))

    pg.display.update()

    posx, posy, rot = movement(posx, posy, rot, maph, 0.04)
    clock.tick(60)
#INTERMINSIN
menu1 = font.render('Вы закончили первый уровень', False, (0, 0, 0))
menu2 = font.render('Нажмите на пробель чтобы начать следуйщий', False, (0, 0, 0))

runningmenu = True
while runningmenu:
    screen.fill((255, 0,0))
    for event in pg.event.get():
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            runningmenu = False
            running = True
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            runningmenu = False
            running = False


    screen.blit(menu1, (160, 50))
    screen.blit(menu2, (50, 150))



    pg.display.update()


#SECOND LEVEL
enemylist2 = [Enemy(screen, enemysheet, 2, 2), Enemy(screen, enemysheet, 3, 4), Enemy(screen, enemysheet, 3, 5), Enemy(screen, enemysheet, 6, 7), GOBLIN(screen, enemysheetG, 13, 9), GOBLIN(screen, enemysheetG, 14, 2), GOBLIN(screen, enemysheetG, 11, 9)]

posx, posy, rot, maph, exitx, exity = gen_map2(size)
health = 100
running = True
while running:
    ticks = pg.time.get_ticks() / 200
    globaltime+=1
    globaltime%=60

    if int(posx) == exitx and int(posy) == exity:
        print("you got out of the maze!")
        running = False
    if health <=0:
        deathscreen = True
        menu1 = font.render('RayCasting игра "Одолей фашизм!"', False, (0, 0, 0))
        menu2 = font.render('ВАС УБИЛИ!', False, (0, 0, 0))
        menu3 = font.render('Нажмите пробел чтобы возродиться.', False, (0, 0, 0))
        menu4 = font.render('Нажмите esc чтобы выйти.', False, (0, 0, 0))

        while deathscreen:
            screen.fill((255, 0, 0))
            for event in pg.event.get():
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    deathscreen = False
                    running = True
                    health=100
                if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    running = False
                    deathscreen = False

            screen.blit(menu1, (160, 50))
            screen.blit(menu2, (300, 150))
            screen.blit(menu3, (50, 450))
            screen.blit(menu4, (50, 500))

            pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                weapon.change_weapon('1')
            elif event.key == pg.K_2:
                weapon.change_weapon('2')

        if event.type == pg.MOUSEBUTTONDOWN:
            weapon.shoot()
            for i in enemylist1:
                i.hittest()
            e1.hittest()
            e2.hittest()
            e3.hittest()



    frame = new_frame(posx, posy, rot, frame, sky, floor, hres, halfvres, mod, maph, size,
                      walls, exitx, exity)

    surf = pg.surfarray.make_surface(frame * 255)
    surf = pg.transform.scale(surf, (800, 600))
    fps = int(clock.get_fps())
    pg.display.set_caption("Pycasting maze - FPS: " + str(fps))

    screen.blit(surf, (0, 0))

    for i in enemylist1:
        i.frame()
        if type(i) == Enemy:
            if i.isalive() and i.distance() <= 1 and globaltime % 20 == 0:
                health -= 1
        if type(i) == GOBLIN:
            if i.isshooting() and i.isalive() and i.distance() <=1.5:
                # if random.Random(10) == 1:
                health -= 0.5




    pillar.frame()
    barrel1.frame()
    e1.frame()
    e2.frame()
    e3.frame()
    weapon.frame()

    if e1.isalive() and e1.distance() <= 1 and globaltime%20 == 0:
        health -= 1
    if e3.isshooting() and e3.isalive() and e3.distance()<=1.5:
        #if random.Random(10) == 1:
       health -=0.5

    hptext = font.render('HP: %d' % health, False, (0, 0, 0))

    screen.blit(hptext, (20, 550))

    pg.display.update()

    posx, posy, rot = movement(posx, posy, rot, maph, 0.04)
    clock.tick(60)


pg.quit()