from flask_sqlalchemy import SQLAlchemy
from src.db.base import Base
import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy(model_class=Base)

# Had to add this because mypy was complaining
#  see https://stackoverflow.com/questions/75774283/flask-sql-alchemy-and-mypy-error-with-db-model-incompatible-types-in-assignmen
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model as BaseModel
else:
    BaseModel = db.Model