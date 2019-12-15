from sqlalchemy import *
from database import Base


class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    done = Column(Boolean)