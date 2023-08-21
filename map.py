import helping as h
import pygame as p
import settings as sett
class Map ():
    def __init__ (self):
        self.map_csv = open('map.csv')
        self.spisok_csv = []
        self.zapolnenie_spiska_csv()
        self.spisok_kartinok = []
        self.kartinka = p.image.load("tile.png")
        self.zapolnenie_kartinok_tailov()
        self.nomber = 0
        self.spisok_tail = []
        self.zapolnenie_tailov()
        self.shirina_map = len(self.spisok_csv[1]) * sett.SIZE
        self.bisota_map = len(self.spisok_csv) * sett.SIZE
    
    def zapolnenie_spiska_csv (self):
        for one_stroka in self.map_csv:
            self.spisok_csv.append(h.razdelitel(one_stroka,','))
    
    def prorisovka_vsex_tail(self, okno, camera):
        for tail in self.spisok_tail:
            tail.prorisovka(okno, camera)
    
    def zapolnenie_tailov (self):
        x = -sett.SIZE
        y = 0
        for spisok_s_chislami in self.spisok_csv:
            for chislo in spisok_s_chislami:
                kartinka = self.spisok_kartinok[int(chislo)]
                x += sett.SIZE
                tail = Tail(int(chislo),(x,y),kartinka)
                self.spisok_tail.append(tail)
            x = -sett.SIZE
            y += sett.SIZE
        
    def zapolnenie_kartinok_tailov (self):
        for one_kartinka in range (17):
            one_kartinka_obrez = self.kartinka.subsurface(one_kartinka * 16, 0, 16, 16)
            one_kartinka_obrez_izmen = p.transform.scale(one_kartinka_obrez,(sett.SIZE,sett.SIZE))
            self.spisok_kartinok.append(one_kartinka_obrez_izmen)
        for one_kartinka in range (17):
            one_kartinka_obrez = self.kartinka.subsurface(one_kartinka * 16, 16, 16, 16)
            one_kartinka_obrez_izmen = p.transform.scale(one_kartinka_obrez,(sett.SIZE,sett.SIZE))
            self.spisok_kartinok.append(one_kartinka_obrez_izmen)
        for one_kartinka in range (17):
            one_kartinka_obrez = self.kartinka.subsurface(one_kartinka * 16, 32, 16, 16)
            one_kartinka_obrez_izmen = p.transform.scale(one_kartinka_obrez,(sett.SIZE,sett.SIZE))
            self.spisok_kartinok.append(one_kartinka_obrez_izmen)
        for one_kartinka in range (17):
            one_kartinka_obrez = self.kartinka.subsurface(one_kartinka * 16, 48, 16, 16)
            one_kartinka_obrez_izmen = p.transform.scale(one_kartinka_obrez,(sett.SIZE,sett.SIZE))
            self.spisok_kartinok.append(one_kartinka_obrez_izmen)
        for one_kartinka in range (17):
            one_kartinka_obrez = self.kartinka.subsurface(one_kartinka * 16, 64, 16, 16)
            one_kartinka_obrez_izmen = p.transform.scale(one_kartinka_obrez,(sett.SIZE,sett.SIZE))
            self.spisok_kartinok.append(one_kartinka_obrez_izmen)
        for one_kartinka in range (17):
            one_kartinka_obrez = self.kartinka.subsurface(one_kartinka * 16, 80, 16, 16)
            one_kartinka_obrez_izmen = p.transform.scale(one_kartinka_obrez,(sett.SIZE,sett.SIZE))
            self.spisok_kartinok.append(one_kartinka_obrez_izmen)
        for one_kartinka in range (17):
            one_kartinka_obrez = self.kartinka.subsurface(one_kartinka * 16, 96, 16, 16)
            one_kartinka_obrez_izmen = p.transform.scale(one_kartinka_obrez,(sett.SIZE,sett.SIZE))
            self.spisok_kartinok.append(one_kartinka_obrez_izmen)
        for one_kartinka in range (17):
            one_kartinka_obrez = self.kartinka.subsurface(one_kartinka * 16, 112, 16, 16)
            one_kartinka_obrez_izmen = p.transform.scale(one_kartinka_obrez,(sett.SIZE,sett.SIZE))
            self.spisok_kartinok.append(one_kartinka_obrez_izmen)

class Tail ():
    def __init__(self, id, x_y, kartinka):
        self.id = id
        self.x_y = x_y
        self.kartinka = kartinka
        self.xitbox = p.rect.Rect(x_y, (sett.SIZE,sett.SIZE))

    def prorisovka (self, okno, camera):
        camera_xitbox = camera.zamena_camera(self)
        okno.blit(self.kartinka, camera_xitbox)
    
        

        