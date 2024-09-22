from src.models.user.user_model import User
from src.db.connect import db

# TODO: add return types

class UserService:
    
    @staticmethod
    def createUser(user=User, currentSession=db.session):
            currentSession.add(user)

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
    
    @staticmethod
    def getSingleUserOrFail(userId):
        return  db.get_or_404(User, userId)

    @staticmethod
    def get_all_users():
        # todo: USE DB.EXECUTE METHOD
        return User.query.all()

    @staticmethod
    def deleteUser(userId=User.id,dataBase=db)-> User:
        user = dataBase.session.execute(dataBase.select(User).filter_by(id=userId)).scalar_one()
        dataBase.session.delete(user)
        return user
