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
# userId string needs to be hardcoded, otherwise it fails
def getSingleUser(userId):
    userFound= UserService.getSingleUserOrFail(userId)
    return jsonify(userFound.to_dict())

@user_bp.delete('/<int:userId>')
def deleteSingleUser(userId):
    userDeleted = UserService.deleteUser(userId,db)
    db.session.commit()
    return jsonify(userDeleted.to_dict())

@user_bp.post('/')
def createUser():

    data = request.json

    username = data.get('username')
    email = data.get('email')
    companyName = data.get('companyName')


    # if not username or not email:
    #     return jsonify({"error": "Missing required fields"}), 400

    new_company=Company(name=companyName)
    currentSession= db.session
    CompanyService.createCompany(new_company,currentSession)
    # so that company_id converts from null to an actual id
    currentSession.flush()

    # TODO: check how can these args be typed, I checked mypy, and also playing with BaseModel, but no easy solution yet
    new_user = User(username=username, email=email,company_id=new_company.id)
    UserService.createUser(new_user,currentSession)

    currentSession.commit()

    return jsonify({
        "message": "User added successfully!",
        'user': new_user.to_dict()
    }), 201
