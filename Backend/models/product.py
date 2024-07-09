from sqlalchemy import Column, String, Integer, ForeignKey
from models.base_model import BaseModel, Base

class Product(BaseModel, Base):
    __tablename__ = 'products'
    category = Column(String(100), nullable=True)
    segment = Column(String(100), nullable=True)
    manufacturer = Column(String(100), nullable=True)
    brand = Column(String(100), nullable=True)
    description = Column(String, nullable=True)
    package_type = Column(String(50), nullable=True)
    package_size = Column(String(50), nullable=True)
    barcode = Column(String(255), nullable=True, unique=True)
    store_id = Column(Integer, ForeignKey('stores.id'), nullable=False)
