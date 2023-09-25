import pygame as p
import os as o
import settings as sett
import random as r
import pygame.freetype as pf
class Player ():
    def __init__(self, name, skorost, x_y):
        self.name = name
        self.skorost = skorost
        self.skorostx = 0
        self.skorosty = 0
        self.x_y = x_y
        self.kartinka = p.image.load("player.png")
        self.down = []
        self.left = []
        self.right = []
        self.up = []
        self.all = self.up
        self.nomber = 0
        self.save_xy = 'x_y.csv'
        for one_kartinka in range (4):
            one_kartinka_obrez = self.kartinka.subsurface(one_kartinka * 32, 0, 32, 32)
            one_kartinka_obrez_izmen = p.transform.scale(one_kartinka_obrez,(sett.SIZE,sett.SIZE))
            self.down.append(one_kartinka_obrez_izmen)
        for one_kartinka in range (4):
            one_kartinka_obrez = self.kartinka.subsurface(one_kartinka * 32, 32, 32, 32)
            one_kartinka_obrez_izmen = p.transform.scale(one_kartinka_obrez,(sett.SIZE,sett.SIZE))
            self.left.append(one_kartinka_obrez_izmen)
        for one_kartinka in range (4):
            one_kartinka_obrez = self.kartinka.subsurface(one_kartinka * 32, 64, 32, 32)
            one_kartinka_obrez_izmen = p.transform.scale(one_kartinka_obrez,(sett.SIZE,sett.SIZE))
            self.right.append(one_kartinka_obrez_izmen)
        for one_kartinka in range (4):
            one_kartinka_obrez = self.kartinka.subsurface(one_kartinka * 32, 96, 32, 32)
            one_kartinka_obrez_izmen = p.transform.scale(one_kartinka_obrez,(sett.SIZE,sett.SIZE))
            self.up.append(one_kartinka_obrez_izmen)
            
        self.xitbox = p.Rect(x_y, (sett.SIZE,sett.SIZE))
        self.dop_xitbox = p.rect.Rect(self.xitbox.x + self.skorostx * 5, self.xitbox.y + self.skorosty * 5, sett.SIZE, sett.SIZE)

    def prorisovka (self,okno,camera):
        camera_xitbox = camera.zamena_camera(self)
        okno.blit(self.all[self.nomber], camera_xitbox)
        # p.draw.rect(okno,(250,0,0),self.dop_xitbox)
    
    def dvizenie (self, all_tiles, npc):
        self.skorosty = 0
        self.skorostx = 0
        keys = p.key.get_pressed()
        if keys[p.K_w]:
            self.skorosty = -self.skorost
            self.skorostx = 0
            self.all = self.up
        if keys[p.K_s]:
            self.skorosty = self.skorost
            self.skorostx = 0
            self.all = self.down
        if keys[p.K_a]:
            self.skorosty = 0
            self.skorostx = -self.skorost
            self.all = self.left
        if keys[p.K_d]:
            self.skorosty = 0
            self.skorostx = self.skorost
            self.all = self.right
        if self.stolknovenie(all_tiles, npc) == True:
                if self.skorostx > 0:
                    self.skorostx = 0
                if self.skorostx < 0:
                    self.skorostx = 0
                if self.skorosty > 0:
                    self.skorosty = 0
                if self.skorosty < 0:
                    self.skorosty = 0
        self.xitbox.x += self.skorostx
        self.xitbox.y += self.skorosty
        if self.skorosty !=0 or self.skorostx != 0:
            self.nomber += 1
        else:
            self.nomber = 0
        if self.nomber == 4:
            self.nomber = 0
        
    def stolknovenie (self, all_tiles, npc):
        self.dop_xitbox = p.rect.Rect(self.xitbox.centerx - 7 + self.skorostx * 5, self.xitbox.centery - 7 + self.skorosty * 5, sett.SIZE//4, sett.SIZE//4)
        for one_tile in all_tiles:
            if self.dop_xitbox.colliderect(one_tile.xitbox) == True and one_tile.id in sett.WALL_IDS:
                return True
            if npc.xitbox.colliderect(self.dop_xitbox) == True:
                npc.igrok_radom = True
                return True
            else:
                a = abs(npc.xitbox.centerx - self.xitbox.centerx)
                b = abs(npc.xitbox.centery - self.xitbox.centery)
                c = (a**2 + b**2)**0.5
                if c >= 100:
                    npc.igrok_radom = False
        return False

class NPC:
    def __init__(self, kartinka, x_y):
        self.skorostx = 2
        self.kartinka = kartinka
        self.xitbox = p.Rect(x_y, (sett.SIZE,sett.SIZE))
        self.x_y = x_y
        self.igrok_radom = False

    def prorisovka (self,okno,camera):
        camera_xitbox = camera.zamena_camera(self)
        okno.blit(self.kartinka, camera_xitbox)
    
    def dvizenie (self):
        if self.igrok_radom == False:
            self.xitbox.x += self.skorostx
            if self.x_y[0] < self.xitbox.x - 20:
                self.skorostx = -self.skorostx
            if self.x_y[0] > self.xitbox.x + 20:
                self.skorostx = -self.skorostx
class SMS:
    def __init__(self,x_y,text):
        self.xitbox = p.Rect(x_y, )
