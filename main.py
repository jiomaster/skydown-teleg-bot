import config

import databasemanager
import usermanager
import telegram


def start(bot, update):
	c_id = update.message.chat_id
	global msg, image, buttons
	msg = ''
	image = None
	buttons = None
