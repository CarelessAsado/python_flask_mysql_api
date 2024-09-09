from src.user.user_model import User
from src.db.connect import db

# TODO: add return types

class UserService:
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
    def getSingleUserOrFail(userId):
        return  db.get_or_404(User, userId)

    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def delete_user_by_id(user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False