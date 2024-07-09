from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Store(BaseModel, Base):
    __tablename__ = 'stores'
    name = Column(String(255), nullable=True)
    location = Column(String(255), nullable=True)
    products = relationship("Product", back_populates="store")
