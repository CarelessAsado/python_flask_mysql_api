from flask import Blueprint, request,jsonify
from src.models.user.user_model import User
from src.models.company.company_model import Company
from src.models.user.user_service import UserService
from src.models.company.company_service import CompanyService
from src.db.connect import db

user_bp = Blueprint('user', __name__)

@user_bp.get('/')
def getAllUsers():
    # Obtener los parámetros de consulta de la URL
    query_params = request.args
    users = UserService.get_all_users()
        # Create a list of user dictionaries to return as JSON
    users_list = [
        user.to_dict() for user in users
    ]
    
    return jsonify(users_list)

@user_bp.get('/<int:userId>')
# TODO: check if userId string needs to be hardcoded
def getSingleUser(userId):
    userFound= UserService.getSingleUserOrFail(userId)
    
    return jsonify(userFound.to_dict())
    # Obtener los parámetros de consulta de la URL
    query_params = request.args
    users = UserService.get_all_users()
        # Create a list of user dictionaries to return as JSON
    users_list = [
       user.to_dict() for user in users
    ]
    
    return jsonify(users_list)

@user_bp.post('/')
def add_user():

    data = request.json

    username = data.get('username')
    email = data.get('email')
    companyName = data.get('companyName')


    # if not username or not email:
    #     return jsonify({"error": "Missing required fields"}), 400
    # TODO: abstract to create user
    # TODO: delete user
    # TODO: remove fac key/relation if present on Company table
    # Todo: validation with validators in sqlalchemy or library https://dev.to/aylolo/controlling-data-with-flask-sqlalchemy-validations-vs-constraints-219o
    new_company=Company(name=companyName)

    # TODO: check how can these args be typed, I checked mypy, and also playing with BaseModel, but no easy solution yet
    new_user = User(username=username, email=email,company_id=new_company.id)
    print('after')

    currentSession= db.session
    
    CompanyService.createCompany(new_company,currentSession)
    UserService.createUser(new_user,currentSession)

    currentSession.commit()
    return jsonify({
        "message": "User added successfully!",
        "user": new_user.to_dict()
    }), 201
