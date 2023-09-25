import sqlalchemy as sq
import sqlalchemy.orm as sqo
import base as b
Sessia_for_podkl = sqo.sessionmaker()
def proverka (name):
    sessia = Sessia_for_podkl(bind = b.base)
    query = sessia.query(b.tablisa)
    for zapis in query:
        if zapis.name == name:
            sessia.close()
            return True
    sessia.close()
    return False

def dobavlenie_obnovlenie(name,x,y):
    if proverka(name) == True:
        sessia = Sessia_for_podkl(bind = b.base)
        query = sessia.query(b.tablisa)
        for zapis in query:
            if zapis.name == name:
                zapis.x = x
                zapis.y = y
                break
        sessia.commit()
        sessia.close()
    else:
        sessia = Sessia_for_podkl(bind = b.base)
        player = b.tablisa(name = name, x = x, y = y)
        sessia.add(player)
        sessia.commit()
        sessia.close()

def coordinates (name):
    sessia = Sessia_for_podkl(bind = b.base)
    query = sessia.query(b.tablisa)
    for zapis in query:
        if zapis.name == name:
            sessia.close()
            return zapis.x, zapis.y
    sessia.close()
    return 100,100