from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String
from src.db.connect import db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    # username: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(String(150), unique=True)  # Added length for VARCHAR
    # email: Mapped[str]
    email: Mapped[str] = mapped_column(String(255))  # Added length for VARCHAR

    def __repr__(self):
      return f"<User(id={self.id}, username={self.username}, email={self.email})>"