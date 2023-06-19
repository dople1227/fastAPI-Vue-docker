from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, VARCHAR
from enum import Enum

Base = declarative_base()


class Zoo(Base):
    __tablename__ = "zoo"
    critter = Column("critter", VARCHAR(100), primary_key=True)
    count = Column("count", Integer)
    damages = Column("damages", Float)

    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages

    def __repr__(self):
        return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)


class ModelName(str, Enum):
    """독스트링 스타일

    첫줄에 요약된 설명을 작성하고 추가설명은 한줄 띄운 후 기입
    """

    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
