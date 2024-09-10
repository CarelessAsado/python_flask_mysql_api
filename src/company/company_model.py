from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import Integer, String
from src.db.connect import db
from typing import List
from src.user.user_model import User

class Company(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), unique=True) 
    users: Mapped[List[User]] = relationship(User.__name__)

    def __repr__(self):
      return f"<Company (id={self.id}, name={self.name})>"
    
      # Serialize the object to a dictionary
    def to_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
