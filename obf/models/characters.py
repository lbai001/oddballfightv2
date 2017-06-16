from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    level = Column(Integer)
    hp = Column(Integer)
    mp = Column(Integer)
    exp = Column(Integer)
    score = Column(Integer)

    def hi(self):
        print (self.name)


Index('character_index', Character.name, unique=True, mysql_length=255)
