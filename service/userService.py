from model.baseModel import Session
from model.userModel import User


class UserService:
    def __init__(self):
        self.session = Session()

    def createUser(self, username, password, email):
        new_user = User(username=username, password=password, email=email)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def getAllUsers(self):
        users = self.session.query(User).all()
        return users

    def getUserByID(self, id):
        user = self.session.query(User).filter_by(id=id).first()
        return user
    
    def getUserByEmail(self, email):
        user = self.session.query(User).filter_by(email=email).first()
        return user
    
    def getUserByUsername(self, username):
        user = self.session.query(User).filter_by(username=username).first()
        return user
    