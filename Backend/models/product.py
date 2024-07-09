from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Product(BaseModel, Base):
    __tablename__ = 'products'
    category = Column(String(100), nullable=True)
    segment = Column(String(100), nullable=True)
    manufacturer = Column(String(100), nullable=True)
    brand = Column(String(100), nullable=True)
    description = Column(String(1024) , nullable=True)
    package_type = Column(String(50), nullable=True)
    package_size = Column(String(50), nullable=True)
    barcode = Column(String(255), nullable=True, unique=True)
    store_id = Column(String(60), ForeignKey('stores.id'), nullable=False)
    store = relationship("Store", back_populates="products")
    
    def __init__(self, *args, **kwargs):
        """initializes produts"""
        super().__init__(*args, **kwargs)