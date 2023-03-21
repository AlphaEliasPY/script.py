# -*- coding: utf-8 -*-
import telegram
from telegram.ext import Updater, MessageHandler, Filters

import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Token del bot
TOKEN = "889289459:AAGLSiTZiJKg4A9idIkiy5hVDETpUdPLDwo"

# Creamos el objeto updater y el dispatcher
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Definimos la función que enviará la respuesta
def responder(update, context):
    # Creamos la respuesta
    respuesta = "Este es un mensaje fijo de prueba"
    # Enviamos la respuesta
    context.bot.send_message(chat_id=update.message.chat_id, text=respuesta)

# Creamos el handler y lo agregamos al dispatcher
handler = MessageHandler(Filters.text & (~Filters.command), responder)
dispatcher.add_handler(handler)

# Iniciamos el bot
updater.start_polling()
updater.idle()
