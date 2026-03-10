from sqlalchemy import Column, Integer, String
from database import Base

class Grocery(Base):
    __tablename__ = "groceries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    tamil = Column(String)
    price = Column(Integer)