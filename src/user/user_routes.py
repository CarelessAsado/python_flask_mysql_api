from flask import Blueprint, request,jsonify
from src.user.user_model import User
from src.company.company_model import Company
from src.user.user_service import UserService
from src.company.company_service import CompanyService
from src.db.connect import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def getAllUsers():
    # Obtener los parámetros de consulta de la URL
    query_params = request.args
    users = UserService.get_all_users()
        # Create a list of user dictionaries to return as JSON
    users_list = [
        user.to_dict() for user in users
    ]
    
    return jsonify(users_list)

@user_bp.route('/<int:userId>', methods=['DELETE','GET'])
# TODO: check if userId string needs to be hardcoded
def deleteSingleUser(userId):
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

@user_bp.route('/add_user', methods=['GET'])
def add_user():
    username = 'rod'
    """ request.args.get('username') """
    email = 'rod2@g.com'


    if not username or not email:
        return jsonify({"error": "Missing required fields"}), 400
    print('before')
    new_company=Company(name='Rod company')
    CompanyService.createCompany(new_company)
    # TODO: check how can these args be typed, I checked mypy, and also playing with BaseModel, but no easy solution yet
    new_user = User(username=username, email=email,company_id=new_company.id)
    print('after')

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({
            "message": "User added successfully!",
            "user": new_user.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

