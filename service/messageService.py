from model.messageModel import Message
from service.userService import UserService
from model.baseModel import Session


class MessageService:
    def __init__(self) -> None:
        self.session = Session()
    
    def createMessage(self, autor, to, title, content, extra, category):
        new_message = Message(autor=autor, to=to, title=title, content=content, extra=extra, category=category)
        self.session.add(new_message)
        self.session.commit()
        return new_message
    
    def getAllMessages(self):
        messages = self.session.query(Message).all()
        formatted_messages = []
        category = ""
        for message in messages:
            if message.category == '1':
                category = "Somente no App/Site"
            elif message.category == '2':
                category = "No App/Site + entrega"
            elif message.category == '3':
                category = "No App/Site + entrega + bombom"

            to_user = UserService().getUserByID(message.to)
            to_username = to_user.username if to_user else "Não encontrado"
            

            print(message.to)

            formatted_message = {
                'id': message.id,
                'autor': message.autor,
                'to': to_username,
                'extra': message.extra,
                'title': message.title,
                'content': message.content,
                'category': category,
                'date': message.date.strftime('%d/%m/%Y %H:%M:%S'),
                'isSubmited': 'Sim' if message.isSubmited else 'Não'
            }
            formatted_messages.append(formatted_message)
        
        return formatted_messages
    
    def getMessageByTo(self, to):
        messages = self.session.query(Message).filter_by(to=to).all()
        formatted_messages = []

        for message in messages:
            formatted_message = {
                'id': message.id,
                'autor': message.autor,
                'to': message.to,
                'title': message.title,
                'content': message.content,
                'date': message.date.strftime('%d/%m/%Y %H:%M:%S'),
                'isSubmited': 'Sim' if message.isSubmited else 'Não'
            }
            formatted_messages.append(formatted_message)
        
        return formatted_messages
    
    def delete(self, id):
        message = self.session.query(Message).filter_by(id=id).first()
        self.session.delete(message)
        self.session.commit()
        return message

    def isSubmited(self, id):
        message = self.session.query(Message).filter_by(id=id).first()
        message.isSubmited = True
        self.session.commit()
        return message