from flask import Flask
from src.db.connect import db
from src.config_env.config import Config
from src.user.user_routes import user_bp

# import models so tables can be automatically created
from src.company.company_model import Company
from src.user.user_model import User

# TODO: copiar estructura de este archivo
# https://www.youtube.com/watch?v=b_qmjG7n-Ao
# TODO: seguir con USER SERVICE api delete update create read. Agregar db.session q creo q es el metodo correcto, pero investigar y dejar todo asentado
# TODO: armar una relacion many to many

# TODO: AUTH

# TODO: ver tema cache en docker q no me gusta q no se renueva automaticamente, ni q tampoco se actualiza acorde. El docker- compose up/down funciona p/las env vars
# TODO: ver xq la info no se retiene, calculo q tiene q ver con volumes
# TODO: ver xq BE falla con docker (probé muchas cosas, se me ocurre q puede ser el host q falla. Dejar para el final ya q perdí mucho tiempo)
# TODO: ver como hacer para q los types del user se reflejen, no me gusta
# TODO: ver q deje todos en el docker compose

class BaseUrlRouting:
    USERS='users'


app = Flask(__name__)
#  see https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/config/#flask_sqlalchemy.config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_DATABASE_URI'] =f'mysql+pymysql://{Config.MYSQL_DB_USER}:{Config.MYSQL_DB_PASSWORD}@{Config.MYSQL_DB_HOST}:{Config.MYSQL_DB_PORT}/{Config.MYSQL_DB_NAME}'

db.init_app(app)
# https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#create-the-tables
with app.app_context():
    db.create_all()

# Register routes
app.register_blueprint(user_bp, url_prefix=f'/{BaseUrlRouting.USERS}')


if __name__ == '__main__':
    app.run(debug=True)
