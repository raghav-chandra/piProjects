import sys
import time
import random
import datetime
import time
import telepot
import subprocess
from telepot.loop import MessageLoop

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command
    if command == '/click':
	timestamp = time.time()
	fileName = '/home/pi/Workspace/TelegramBot/' + `timestamp` + '.jpeg'
        sp = subprocess.Popen(['fswebcam', fileName], stdout = subprocess.PIPE)
	sp.wait()
        f = open(fileName, 'rb')
	print f
	bot.sendPhoto(chat_id, f)
    else:
        bot.sendMessage(chat_id,command)

bot = telepot.Bot('<TelegramAPIKey>')
MessageLoop(bot, handle).run_as_thread()

print 'I am listening...'

while 1:
     time.sleep(10)
