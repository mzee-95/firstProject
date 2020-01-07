import telebot
import threading
import time
import os
import socket
import asyncio
import sys
import logging

bot_token = '928532602:AAEoedP50RLpJ_jQV3xi3PLVi8ibpFCGupE'

bot = telebot.TeleBot(token=bot_token)

#We squash bugs chat_id: -1001225534207
#Test group chat_id: -375105540
chat_id = -1001225534207
chat_id = -375105540

bot.send_message(chat_id=chat_id, text='TC Bot active 👌🏽')


#Hercules: 10.3.1.154
#Marno: 10.100.4.38
