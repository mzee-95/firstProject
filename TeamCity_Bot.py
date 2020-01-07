import telebot
import os
import sys

bot_token = '928532602:AAEoedP50RLpJ_jQV3xi3PLVi8ibpFCGupE'

bot = telebot.TeleBot(token=bot_token)

chat_id = -1001265292288

if 'Started' in sys.argv:
    message = 'Build Started'

if 'Finished' in sys.argv:
    message = 'Build Successful'

bot.send_message(chat_id=chat_id, text=message)
