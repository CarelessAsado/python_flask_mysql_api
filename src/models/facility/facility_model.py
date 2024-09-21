from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String,ForeignKey
from src.db.connect import db
from src.models.user.user_model import User

class Facility(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), unique=True) 
    company_id: Mapped[int] = mapped_column(ForeignKey(f"company.id"))

    def __repr__(self):
      return f"<Facility (id={self.id}, name={self.name})>"
    
      # Serialize the object to a dictionary
    def to_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
