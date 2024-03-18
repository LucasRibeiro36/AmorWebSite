from .userService import UserService

class LoginService:
    def __init__(self):
        self.userService = UserService()

    def login(self, username, password):
        user = self.userService.getUserByUsername(username)
        if user is None:
            return False
        if user.password == password:
            return {'username': user.username, 'isAdmin': user.isAdmin}
        else:
            return False