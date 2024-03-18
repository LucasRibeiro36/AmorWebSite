from flask import render_template, request, redirect, url_for, flash
from datetime import datetime
from flask import Blueprint
from service.loginService import LoginService
import time
from flask import session

class LoginController:
    def __init__(self) -> None:
        self.loginBP = Blueprint('login', __name__)
        self.loginBP.add_url_rule('/login/', view_func=self.login, methods=['GET', 'POST'])
        self.loginBP.add_url_rule('/logout/', view_func=self.logout, methods=['GET'])
        self.loginService = LoginService()
    
    def login(self):
        # if GET
        if request.method == 'GET':
            return render_template('login.html')
        
        # if POST
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username:
            flash('O usuário é obrigatório!')
            return render_template('login.html')  # Retorna o template novamente
        elif not password:
            flash('A senha é obrigatória!')
            return render_template('login.html')  # Retorna o template novamente
        else:
            if self.loginService.login(username, password) is not False:
                if self.loginService.login(username, password)['isAdmin']:
                    session['user'] = self.loginService.login(username, password)
                    return redirect(url_for('admin.index'))
                else:
                    session['user'] = self.loginService.login(username, password)
                    return redirect(url_for('user.index'))
            else:
                flash('Usuário ou senha inválidos!')
                return render_template('login.html')  # Retorna o template novamente
            
    def logout(self):
        session.pop('user', None)
        return redirect(url_for('login.login'))
        
    def getBP(self):
        return self.loginBP
