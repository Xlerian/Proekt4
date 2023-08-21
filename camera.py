import pygame as p
import settings as sett
class Camera():
    def __init__ (self, igrok):
        self.igrok = igrok
        self.skorost_smeshenia =[sett.SHIRINA/2,sett.BISOTA/2]
    
    def zamena_camera (self, object):
        rect = p.rect.Rect((object.xitbox.x + self.skorost_smeshenia[0],object.xitbox.y + self.skorost_smeshenia[1]),object.xitbox.size)
        return rect 

    def slezka_za_igrokom (self,shirina, bisota):
        self.skorost_smeshenia[0] = -self.igrok.xitbox.x + sett.SHIRINA/2
        self.skorost_smeshenia[1] = -self.igrok.xitbox.y + sett.BISOTA/2
        if self.igrok.xitbox.x <= sett.SHIRINA/2:
            self.skorost_smeshenia[0] = 0
        if self.igrok.xitbox.y <= sett.BISOTA/2:
            self.skorost_smeshenia[1] = 0
        if self.igrok.xitbox.x >= shirina - sett.SHIRINA/2:
            self.skorost_smeshenia[0] = -(shirina - sett.SHIRINA)
        if self.igrok.xitbox.y >= bisota - sett.BISOTA/2:
            self.skorost_smeshenia[1] = -(bisota - sett.BISOTA)
