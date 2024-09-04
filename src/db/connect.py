from flask_sqlalchemy import SQLAlchemy
from src.db.base import Base
import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy(model_class=Base)