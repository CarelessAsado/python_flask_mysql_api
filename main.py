from flask import Flask, request,jsonify
from src.db.connect import db
from src.models.user import User
from src.config_env.config import Config

CONNECT_STRING= f'mysql+pymysql://{Config.MYSQL_DB_USER}:{Config.MYSQL_DB_PASSWORD}@{Config.MYSQL_DB_HOST}:{Config.MYSQL_DB_PORT}/{Config.MYSQL_DB_NAME}'

# TODO: armar apuntes sobre env variables en docker compose
# TODO: seguir con api delete update create read
# TODO: armar una relacion many to many
# TODO: AUTH

# TODO: ver tema cache en docker q no me gusta q no se renueva automaticamente, ni q tampoco se actualiza acorde. El docker- compose up/down funciona p/las env vars
# TODO: ver xq la info no se retiene, calculo q tiene q ver con volumes
# TODO: ver xq BE falla con docker (probé muchas cosas, se me ocurre q puede ser el host q falla. Dejar para el final ya q perdí mucho tiempo)
# TODO: ver como hacer para q los types del user se reflejen, no me gusta
# TODO: ver q deje todos en el docker compose

def TEST(var):
    print('hola' + var)

TEST('do it')

app = Flask(__name__)
#  see https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/config/#flask_sqlalchemy.config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECT_STRING
db.init_app(app)



# https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#create-the-tables
with app.app_context():
    db.create_all()


@app.route('/', methods=['GET'])
def get_params():
    # Obtener los parámetros de consulta de la URL
    query_params = request.args
    users = User.query.all()
        # Create a list of user dictionaries to return as JSON
    users_list = [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email
        } for user in users
    ]
    
    # Devolver los parámetros de consulta en la respuesta
    return jsonify(users_list)

# GET endpoint to add a user
@app.route('/add_user', methods=['GET'])
def add_user():
    username = 'rod'
    """ request.args.get('username') """
    email = 'rod2@g.com'


    if not username or not email:
        return jsonify({"error": "Missing required fields"}), 400
    print('before')
    new_user = User(username=username, email=email)
    print('after')

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({
            "message": "User added successfully!",
            "user": {
                "id": new_user.id,
                "username": new_user.username,
                "email": new_user.email
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
