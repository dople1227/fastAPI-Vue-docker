from sqlalchemy import Column, Integer, Float, VARCHAR, BOOLEAN
from enum import Enum
from .session import Base


class User(Base):
    __tablename__ = "user"
    id = Column(VARCHAR(100), primary_key=True, index=True)
    name = Column(VARCHAR(40), nullable=False)
    email = Column(VARCHAR(40), unique=True, index=True, nullable=False)
    phoneNumber = Column(VARCHAR(20), unique=True, nullable=False)
    is_active = Column(BOOLEAN, default=True)
    is_superuser = Column(BOOLEAN, default=False)

    # def __init__(self, critter, count, damages):
    #     self.critter = critter
    #     self.count = count
    #     self.damages = damages

    # def __repr__(self):
    #     return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)


class ModelName(str, Enum):
    """독스트링 스타일

    첫줄에 요약된 설명을 작성하고 추가설명은 한줄 띄운 후 기입
    """

    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
