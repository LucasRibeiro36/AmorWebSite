from flask import Flask
from controller.messageController import MessageController
from model.messageModel import Message
from model.baseModel import Base, engine
from model.userModel import User
from controller.loginController import LoginController
from controller.adminController import AdminController
from controller.userController import UserPagesController


app = Flask(__name__)
app.config['SECRET_KEY'] = '009e4e3a32a594adbce738436d6e8c89c6595db360aa9027'

Base.metadata.create_all(engine)  # Inicialize a instância do SQLAlchemy

# BP
messageBP = MessageController().getBP()
loginBP = LoginController().getBP()
adminBP = AdminController().getBP()
userBP = UserPagesController().getBP()

app.register_blueprint(messageBP, name='message')
app.register_blueprint(loginBP, name='login')
app.register_blueprint(adminBP, name='admin')
app.register_blueprint(userBP, name='user')


if __name__ == '__main__':
    app.run(debug=True)
