# pylint: disable=invalid-name, line-too-long
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey,
    JSON,
    Boolean
)

from .meta import Base


class Game(Base):
    __tablename__ = 'game'
    id = Column(Integer, primary_key=True)
    player = Column(JSON)
    opponent = Column(JSON)
    end_fight = Column(Boolean)


Index('game_index', Game.id)
