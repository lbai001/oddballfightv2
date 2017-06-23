from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey
)

from .meta import Base
from sqlalchemy.orm import relationship
import json


class Skill(Base):
    """
    :param name=string
    :param dmg = string
    """
    __tablename__ = 'skill'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    dmg = Column(Integer)
    mpc = Column(Integer)
    # foreign key to character
    player_id = Column(ForeignKey('character.id'), nullable=False)
    player = relationship('Character', backref='character_skill')

    def __json__(self, arg):
        return {
            'name': self.name,
            'dmg': self.dmg,
            'mpc': self.mpc,
            'player_id': self.player_id
        }


Index('skill_index', Skill.name, unique=True, mysql_length=255)
