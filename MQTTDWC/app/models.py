"""
Definition of models.
"""

from django.db import models
import paho.mqtt.client as mqtt
from datetime import datetime
# Create your models here.

class Message(models.Model):
    topic = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=50)
    message_string = models.CharField(max_length=100)



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("World")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    new_message = Message()
    new_message.topic = msg.topic
    new_message.message_string = msg.payload
    new_message.timestamp = datetime.now()
    new_message.save()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect_async("test.mosquitto.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()