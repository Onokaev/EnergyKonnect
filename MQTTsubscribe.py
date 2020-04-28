import paho.mqtt.client as mqtt
import time
from time import gmtime, strftime
import sqlite3
from datetime import datetime
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "base.settings")
django.setup()
from core.models import Consumption_Data

the_topic = "kplc/consumption_update"

dbFile = 'db.sqlite3'
    
#these functions are for MQTT status 

#should process received messages
#message format is kplc/consumption_update/meter_number/consumption_update/units_remaining
def on_message(client, userdata, msg):
    if msg.topic == the_topic:
        print(msg.topic+ " " +str(msg.payload))
        m1 = str(msg.payload)
        
        #divide the string using split method
        first_1 = m1.split('/')

        meter_number = first_1[0]
        latest_consumed = first_1[1]
        units_left = first_1[2]
        
        #add date
        print("Saving")

        hallo = Consumption_Data(meter_no = meter_number, current_units_balance = units_left, cumulative_usage = latest_consumed)
        hallo.save()


def on_log(client, userdata, level, buf):
    print("Log: "+buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected")
        client.subscribe(the_topic)
       # client.publish(the_topic, '653434')
        client.subscribe(the_topic)
    else:
        print("Bad connection")


def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected Client. Result code" +str(rc))



broker = "mqtt.eclipse.org"
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883, 60)
client.loop_forever()