from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Style(Base):
    __tablename__ = "style"
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    screen_name = Column(String(256), unique=True)

    def __repr__(self):
        return self.name


class Gig(Base):
    __tablename__ = "gig"
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    gig_id = Column(String(256))
    vk_screen_name = Column(String(256))
    price = Column(String(256))
    groups = Column(String(1024))
    club = Column(String(256))
    date = Column(Date)
    style = Column(Integer, ForeignKey("style.id"))

    def __repr__(self):
        return self.name
