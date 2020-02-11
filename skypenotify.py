from skpy import *
import os
import base64
import sys
#SkypegroupIDs

PreProd_CH = "19:60a2b5c7b97e425ebc108606add74c97@thread.skype"
PreProd_UK = "19:bbfb0996efbb4fcab10137fee50bf285@thread.skype"
PreProd_BE = "19:78936e3003e3428b8e3d46eb07fa3b94@thread.skype"
PreProd_AT = "19:f32cfcd7a985455a9b2f13ef43813cae@thread.skype"
PreProd_CL = "19:87efd6d1566c4ed18f709bb532640b4c@thread.skype"
PreProd_IE = "19:71d38aad9f924f2b82afd58446bc4b73@thread.skype"
PreProd_NL = "19:66269e0aac9f4419b39faca164f01cfd@thread.skype"
Prod_IE = "19:983e4898dda64024b5c694a1069d4fca@thread.skype"
Prod_AT = "19:01c91bf7224c4a53a3c5674fd820fda4@thread.skype"
Prod_NL = "19:4e026db402cc47c9ae7631b7a1e17ace@thread.skype"
Prod_CH = "19:08655faed3904d45b29448dcf56e1e87@thread.skype"
Prod_CL = "19:a23e7e1c8fef47898ecb49c17a326048@thread.skype"
Prod_UK = "19:399ad3a47a624f21a7a8a0042dfa0085@thread.skype"
Prod_BE = "19:219428f5af7d4bb69dd656b0c34abe69@thread.skype"
TEST_POC = "19:de0f09a0026240e69df3a4d6a9f18d96@thread.skype"

#get input from jenkinsfile
inputlist = sys.argv
#notifymessage = ""
#notifymessage = ' '.join(inputlist[1:])
#notifymessage = notifymessage.replace("[body:","")
#notifymessage = notifymessage.replace(inputlist[-2],"")

def selectstage(stage):

  if ( stage == 'checkout'):
    skypemessage = "Checking out GIT"
  elif (stage == 'STARTED'):
    skypemessage = "Updating JIRA ISSUE"
  elif (stage == 'MavenBuild'):
    skypemessage = "Building JAR file"
  elif (stage == 'DockerImageBuild'):
    skypemessage = "Building docker image and running it"
  else :
    skypemessage = " Job failed"
  return skypemessage
    
stage = inputlist[1]
#print (stage)
msg=selectstage(stage)

#encoding password
password = base64.b64decode("U3RhY2NhdG9AMTIzNDU=").decode("utf-8")
#skype id
sk = Skype("bhuvanesh0311@gmail.com", password)
#Skype username and password
country = sys.argv[-1]
env = sys.argv[-2]
if ( country  == "TEST" and env == "TEST" ):
        ch = sk.chats[TEST_POC]
        ch.sendMsg(msg)


