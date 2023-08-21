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
    
    def dvizenie (self, all_tiles):
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
        if self.stolknovenie(all_tiles) == True:
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
        
    def stolknovenie (self, all_tiles):
        self.dop_xitbox = p.rect.Rect(self.xitbox.centerx - 7 + self.skorostx * 5, self.xitbox.centery - 7 + self.skorosty * 5, sett.SIZE//4, sett.SIZE//4)
        for one_tile in all_tiles:
            if self.dop_xitbox.colliderect(one_tile.xitbox) == True and one_tile.id in sett.WALL_IDS:
                return True
        return False