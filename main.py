import pygame as p
import os as o
import settings as sett
import sprits as spr
import random as r
import pygame.freetype as pf
import map as m
import camera as ca
import base_fynksii as bf
p.init()
okno = p.display.set_mode((sett.SHIRINA, sett.BISOTA))
chasi = p.time.Clock()
a = 0
igra_menu = 0
player = spr.Player(sett.NAME, 5, bf.coordinates(sett.NAME))
mapp = m.Map()
camera = ca.Camera(player)
npc = spr.NPC(mapp.spisok_kartinok[119],(576,576))

while a == 0:
    events = p.event.get()
    for one_event in events:
        if one_event.type == p.QUIT:
            a = 1
        if one_event.type == p.KEYDOWN:
            if one_event.key == p.K_SPACE:
                bf.dobavlenie_obnovlenie(player.name, player.xitbox.x, player.xitbox.y)
                

    okno.fill((0,50,0))
    mapp.prorisovka_vsex_tail(okno,camera)
    camera.slezka_za_igrokom(mapp.shirina_map,mapp.bisota_map)
    player.dvizenie(mapp.spisok_tail, npc)
    npc.prorisovka(okno,camera)
    player.prorisovka(okno,camera)
    npc.dvizenie()

    p.display.update()
    chasi.tick(120)
