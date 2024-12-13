import datetime

from datetime import datetime
from sqlalchemy.orm import declared_attr, declarative_base
from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy import  DateTime

from bot.database.engine import engine


def current_time():
    return datetime.now()

class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, index=True)
    date_registered = Column(DateTime, default=current_time)

Base = declarative_base(cls=PreBase)


class User(Base):
    telegram_id = Column(BigInteger, unique=True)
    username = Column(String, default='@None')
    fullname = Column(String)
    lang_tg = Column(String, nullable=True)
