from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String,ForeignKey
from src.db.connect import db,BaseModel
import bcrypt
from flask_jwt_extended import JWTManager
# from src.models.user.user_service import UserService




jwt = JWTManager()
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
    def to_dict(self, include_password: bool = False):
      json={c.name: getattr(self, c.name) for c in self.__table__.columns}

   # TODO: check if I can do sth on db level to avoid returning pwd
      if not include_password:
        json.pop("password", None)  # Exclude the password by default
      
      return json
    
     # Hash the password
    def encodePassword(self, raw_password: str) -> None:
        salt = bcrypt.gensalt()
        hashed_password_bytes = bcrypt.hashpw(raw_password.encode('utf-8'), salt)
        self.password = hashed_password_bytes.decode('utf-8')  # Store as a string

    # Check if the password matches the stored hash
    def comparePasswords(self, raw_password: str) -> bool:
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))