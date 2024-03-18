from flask import render_template, request, redirect, url_for, flash
from datetime import datetime
from flask import Blueprint
import time
from service.messageService import MessageService
from flask import request
from flask import session
from utils.loginDecorator import login_required_admin

class AdminController:
    def __init__(self) -> None:
        self.messageService = MessageService()
        self.adminBP = Blueprint('admin', __name__)
        self.adminBP.add_url_rule('/admin/', view_func=self.index, methods=['GET'])
        self.adminBP.add_url_rule('/admin/isSubmited/', view_func=self.isSubmited, methods=['GET'])
        self.adminBP.add_url_rule('/admin/delete/', view_func=self.delete, methods=['GET'])

    @login_required_admin   
    def index(self):
        current_user = session.get('user')
        return render_template('admin/index.html', current_user=current_user, messages=self.messageService.getAllMessages())
    @login_required_admin
    def isSubmited(self):
        id = request.args.get('id')
        self.messageService.isSubmited(id)
        return redirect(url_for('admin.index'))
    @login_required_admin
    def delete(self):
        id = request.args.get('id')
        self.messageService.delete(id)
        return redirect(url_for('admin.index'))

    def getBP(self):
        return self.adminBP
    