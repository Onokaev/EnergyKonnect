import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buf):
    print("Log: "+buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected")
    else:
        print("Bad connection")

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected Client. Result code" +str(rc))

#should process received messages
def on_message(client, userdata, msg):
    print(msg.topic+ "" +str(msg.payload))



client = mqtt.Client()
client.on_connect = on_connect
client.on_log = on_log
client.on_disconnect = on_disconnect
client.on_message = on_message


client.connect("mqtt.eclipse.org", 1883, 60)
#we need the loops for the callbacks to be processed
client.loop_start()
client.subscribe("house/sensor1")
client.publish("house/sensor1", "my first message")
time.sleep(2)
client.loop_stop()
client.disconnect()
#mqtt.eclipse.org