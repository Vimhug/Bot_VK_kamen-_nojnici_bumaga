import vk_api
from random import choice , randrange
from vk_api.longpoll import VkLongPoll,VkEventType

TOKEN = ''

vk_session = vk_api.VkApi(token=TOKEN )
longpoll = VkLongPoll(vk_session)
vk= vk_session.get_api()

vars = ['камень','ножницы','бумага']

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text: 
        if event.from_user and str(event.text).lower() in vars :
            bot = choice(vars)
            user = str(event.text).lower()
            vk.messages.send(user_id= event.user_id, message= bot, random_id= randrange(1,1000000))
            out = None

            if bot == 'ножницы' :
                if user == 'ножницы':
                    out= 'ничья'
                elif user == 'камень':
                    out = 'ты выиграл'
                else:
                    out = 'ты проиграл'
            
            if bot == 'камень' :
                if user == 'камень':
                    out= 'ничья'
                elif user == 'бумага':
                    out = 'ты выиграл'
                else:
                    out = 'ты проиграл'
            
            if bot == 'бумага' :
                if user == 'бумага':
                    out= 'ничья'
                elif user == 'камень':
                    out = 'ты выиграл'
                else:
                    out = 'ты проиграл'
            
            vk.messages.send(user_id= event.user_id, message= out, random_id= randrange(1,1000000))
        else:
            vk.messages.send(user_id= event.user_id, message='Ошибка. Выберите камень, ножницы или бумагу !' , random_id= randrange(1,1000000))
            
            

            
