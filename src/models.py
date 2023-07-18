from sqlalchemy import Column, Integer, DateTime, String
import datetime

from src.db import Base


class Temperature(Base):
    __tablename__ = 'temperatures'

    uid = Column(Integer, primary_key=True)
    city = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    datetime = Column(DateTime, default=datetime.datetime.now())

    def __str__(self) -> str:
        return 'Temperature {city}, {value}'.format(
            city=self.city,
            value=self.value,
        )
