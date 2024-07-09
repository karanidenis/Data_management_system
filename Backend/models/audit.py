from sqlalchemy import Column, String, Integer, Date, Time, ForeignKey
from models.base_model import BaseModel, Base

class Audit(BaseModel, Base):
    __tablename__ = 'audits'
    product_id = Column(Integer, ForeignKey('products.product_id'), nullable=True)
    store_id = Column(Integer, ForeignKey('stores.store_id'), nullable=True)
    auditor_name = Column(String(255), nullable=True)
    audit_date = Column(Date, nullable=True)
    audit_time = Column(Time, nullable=True)
