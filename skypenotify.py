from skpy import *
import sys
import base64
notifymessage = sys.argv[1]
#Encoding password
password = base64.b64decode("TG9uZG9ucGFyaXNAMQ==").decode("utf-8")
#skype id
sk = Skype("bhuvanesh0311@gmail.com", password)
#Skype username and password
ch = sk.chats["19:de0f09a0026240e69df3a4d6a9f18d96@thread.skype"]
ch.sendMsg(notifymessage)
