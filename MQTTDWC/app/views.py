"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django import forms
from django.utils import timezone
from app.forms import NewMessageForm
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from app.models import Message
from django.views.generic import ListView
import paho.mqtt.client as mqtt

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def topic_list(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    object_list = Message.objects.all()
    all_topics = []
    for o in object_list:
        all_topics.append(o.topic)
    all_topics = set(all_topics)

    return render(
        request,
        'app/message_list.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'alltopics': all_topics,
            'objectlist': object_list,
        }
    )


def publish(request):
    """Renders the about page."""
    if request.method == "POST":        
        client.publish(request.POST['topic'],request.POST['message_string'])
        return HttpResponseRedirect('/topics')
    
    else:
        form = NewMessageForm() 
        return render(request, "app/publish.html", {'form': form})

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

def on_publish(client,userdata,result):
    print("data published \n")
    pass

def on_disconnect(client, userdata, rc):
   print("Disconnected with result code "+str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect_async("test.mosquitto.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_start()