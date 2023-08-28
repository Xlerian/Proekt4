import sqlalchemy as sq
import sqlalchemy.orm as sqo
Class_base = sqo.declarative_base()
class tablisa (Class_base):
    __tablename__ = 'Player'
    id = sq.Column(sq.Integer)
    name = sq.Column(sq.String(255))
    x = sq.Column(sq.Integer)
    y = sq.Column(sq.Integer)