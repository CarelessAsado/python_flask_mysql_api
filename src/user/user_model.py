from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String,ForeignKey
from src.db.connect import db

class User( db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(150), unique=True) 
    email: Mapped[str] = mapped_column(String(255)) 
    # TODO: company table name is hardcoded
    company_id: Mapped[int] = mapped_column(ForeignKey(f"company.id"))

    def __repr__(self):
      print(self)
      return f"<User(id={self.id}, username={self.username}, email={self.email})>"
    
      # Serialize the object to a dictionary
      # TODO: ver https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json q capaz hay otra alternativa
    def to_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}