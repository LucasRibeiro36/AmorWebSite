from flask import render_template, request, redirect, url_for, flash
from service.messageService import MessageService
from datetime import datetime
from flask import Blueprint
from service.userService import UserService
import time
from utils.loginDecorator import login_required
from flask import session

class UserPagesController:
    def __init__(self) -> None:
        self.userService = UserService()
        self.messageService = MessageService()
        self.userPagesBP = Blueprint('user', __name__)
        self.userPagesBP.add_url_rule('/user/', view_func=self.index)
        self.userPagesBP.add_url_rule('/user/create/', view_func=self.create, methods=['GET', 'POST'])
        self.userPagesBP.add_url_rule('/user/getAllUsers/', view_func=self.getAllUsers)
    
    @login_required
    def index(self):
        messages = MessageService().getMessageByTo('user')
        return render_template('user/index.html', messages=messages, current_user=self.getUser())
    
    @login_required
    def create(self):
        if request.method == 'POST':
            autor = request.form['autor']
            to = request.form['to']
            title = request.form['title']
            content = request.form['content']
            extra = request.form['extra']
            category = request.form['category']
            print (autor, to, title, content, extra)

            if not title:
                flash('O título é obrigatório!')
            elif not content:
                flash('O conteúdo é obrigatório!')
            elif not autor:
                flash('O autor é obrigatório!')
            elif not to:
                flash('O destinatário é obrigatório!')
            else:
                self.messageService.createMessage(autor, to, title, content, extra, category)
                flash('Mensagem criada com sucesso!')
                return redirect(url_for('user.index'))
        current_user = {'name': 'user'}
        users = self.userService.getAllUsers()
        for user in users:
            if user.isAdmin:
                users.remove(user)
        return render_template('user/create.html', current_user=self.getUser(), users=users)
    
    def getBP(self):
        return self.userPagesBP
    
    @login_required
    def getAllUsers(self):
        users = self.userService.getAllUsers()
        return users
    
    def getUser(self):
        return session.get('user')