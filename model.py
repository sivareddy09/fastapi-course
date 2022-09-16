from sqlalchemy import Column, Integer, String
from database import Base


class Student(Base):
    __tablename__ = "details"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String, index=True)
    branch = Column(String, index=True)