from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String,ForeignKey
from src.db.connect import db,BaseModel
import bcrypt

class User(BaseModel):
    
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(150), unique=True) 
    email: Mapped[str] = mapped_column(String(255)) 
    password: Mapped[str] = mapped_column(String(80), nullable=False)
    # TODO: company table name is hardcoded
    company_id: Mapped[int] = mapped_column(ForeignKey(f"company.id"))

    def __repr__(self):
      print(self)
      return f"<User(id={self.id}, username={self.username}, email={self.email})>"
    
      # Serialize the object to a dictionary
      # TODO: ver https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json q capaz hay otra alternativa
    def to_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
     # Hash the password
    def encodePassword(self, raw_password: str) -> None:
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(raw_password, salt)

    # Check if the password matches the stored hash
    def comparePasswords(self, raw_password: str) -> bool:
        return bcrypt.checkpw(raw_password, self.password)