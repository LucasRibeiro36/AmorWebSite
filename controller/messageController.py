from flask import render_template, request, redirect, url_for, flash
from service.messageService import MessageService
from datetime import datetime
from flask import Blueprint
import time

class MessageController:
    def __init__(self) -> None:
        self.messageService = MessageService()
        self.messageBP = Blueprint('message', __name__)
        self.messageBP.add_url_rule('/create/', view_func=self.create, methods=['GET', 'POST'])
        self.messageBP.add_url_rule('/about/', view_func=self.about, methods=['GET'])
        self.messageBP.add_url_rule('/', view_func=self.index)

    def create(self):
        if request.method == 'POST':
            autor = request.form['autor']
            to = request.form['to']
            title = request.form['title']
            content = request.form['content']

            if not title:
                flash('O título é obrigatório!')
            elif not content:
                flash('O conteúdo é obrigatório!')
            elif not autor:
                flash('O autor é obrigatório!')
            elif not to:
                flash('O destinatário é obrigatório!')
            else:
                self.messageService.createMessage(autor, to, title, content)
                flash('Mensagem criada com sucesso!')
                return redirect(url_for('message.index'))

        return render_template('create.html')

    def about(self):
        return render_template('about.html')

    def index(self):
        messages = self.messageService.getAllMessages()
        return render_template('index.html', messages=messages)
    
    def getBP(self):
        return self.messageBP

