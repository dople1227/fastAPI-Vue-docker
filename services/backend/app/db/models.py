from sqlalchemy import Column, Integer, Float, VARCHAR, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(VARCHAR(100), primary_key=True, index=True)
    name = Column(VARCHAR(40), nullable=False)
    email = Column(VARCHAR(40), unique=True, index=True, nullable=False)
    phoneNumber = Column(VARCHAR(20), unique=True, nullable=False)
    is_active = Column(BOOLEAN, default=True)
    is_superuser = Column(BOOLEAN, default=False)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(80), index=True)
    description = Column(VARCHAR(200), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
