from flask import Blueprint, request,jsonify
from src.models.user.user_model import User
from src.models.company.company_model import Company
from src.models.user.user_service import UserService
from src.models.company.company_service import CompanyService
from src.db.connect import db
from flask_jwt_extended import create_access_token

user_bp = Blueprint('user', __name__)

@user_bp.get('/')
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    userFound = UserService.findUserByUsername(username)
    # TODO: see if findbyusername can fail by default and if we can throw errors in a better fashion
    if not userFound or not userFound.comparePasswords(password):
        return jsonify({"error": "Invalid username or password"}), 401



    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

