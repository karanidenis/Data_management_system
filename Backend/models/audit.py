from sqlalchemy import Column, String, Date, Time, ForeignKey
from models.base_model import BaseModel, Base

class Audit(BaseModel, Base):
    __tablename__ = 'audits'
    product_id = Column(String(60), ForeignKey('products.id'), nullable=True)
    store_id = Column(String(60), ForeignKey('stores.id'), nullable=True)
    auditor_name = Column(String(255), nullable=True)
    audit_date = Column(Date, nullable=True)
    audit_time = Column(Time, nullable=True)

    def __init__(self, *args, **kwargs):
        """Initializes Audit"""
        super().__init__(*args, **kwargs)
