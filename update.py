import paho.mqtt.client as mqtt
import os.path
import time
from datetime import datetime 
import json
 
MQTT_SERVER = "m16.cloudmqtt.com"
MQTT_PATH = "test_channel"
UPDATE_PATH= "./update.txt"
DEVICE_ID = "device1"


def update_file(msg):
    json_data = json.loads(msg)
    print(json_data)
    if json_data["deviceid"] != DEVICE_ID:
        return
    
    data = json_data["data"]
    if os.path.exists(UPDATE_PATH):
        print("exists")
        ts = time.time()
        st = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        os.rename(UPDATE_PATH,st+".txt")

    fh = open(UPDATE_PATH, "w") 
 
    fh.write(data) 
    fh.close()
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_PATH)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    update_file(str(msg.payload))
    # more callbacks, etc
 

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("laawfawh","Slmx1inecFKx")
 
client.connect(MQTT_SERVER, 16628, 60)
 
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
