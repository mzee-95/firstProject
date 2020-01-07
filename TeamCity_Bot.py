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


chat_id = -1001265292288

bot.send_message(chat_id=chat_id, text='TC Build started')



