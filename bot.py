from pyrogram import Client
from pyrogram.types import Message
from moodle import delete
import random
from config import *

bot = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
#instanceamos el bot
#responder al comando start
@bot.message_handler(comand=['start','ayuda','help'])
def cmd_start(message):
	               #Da la bienbenida al bot
	   bot.reply_to(message,'HOLA BIENBENIDO AL BOT')
	   
	   
#responde a palabras no usadas
@bot.message_handler(content_types=['text'])
def bot_mensajes_texto(menssage):
	   #Gestionar los mensajes de texto recibidos
	   if message.textstartswith('/')
	  
	   	   bot.send_message(message.chat.id,'COMANDO NO DISPONIBLE')
	   else:	   
	   bot.send_message(message.chat.id,'EN QUE PUEDO AYUDARTE')
	   
if __name__ == '__main__':
      print('BOT INICIADO')
      bot.infinity_polling( )
      print('Fin')