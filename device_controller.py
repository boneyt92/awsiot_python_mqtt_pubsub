#AWS IOT MQTT Subscribe and Publish Code
#Autor : technixweb@gmail.com

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys,os
import logging
import time

status = True

def customCallback(client, userdata, message):
	print "Received Data: " + message.payload
	if (message.payload == "STOP"):
		global status
		status = False
	elif (message.payload == "START"):
		global status
		status = True


print "--------------Initializing the MQTT Listener------------"

host = ""  
rootCAPath = "certs/RootCA.crt"
certificatePath = ""
privateKeyPath = ""

# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
myAWSIoTMQTTClient = AWSIoTMQTTClient("TCloud")
myAWSIoTMQTTClient.configureEndpoint(host, 8883)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()
myAWSIoTMQTTClient.subscribe("tc/things/sub/data", 1, customCallback)
loopCount = 0

while True:
	global status
	if(status):
		myAWSIoTMQTTClient.publish("tc/things/pub/data", "New Message " + str(loopCount), 1)
		loopCount += 1
		print "Value = " + str(loopCount-1)+ " Status = " + str(status)
		time.sleep(4)







