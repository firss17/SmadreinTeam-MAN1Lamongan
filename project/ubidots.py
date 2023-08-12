import paho.mqtt.client as paho
from paho import mqtt
import json
# define static variable
# broker = "mqtt-dashboard.com"
broker = "industrial.api.ubidots.com"
port = 1883
timeout = 60

username = 'BBFF-YxKin1FIVR21bg9qnIa0IVfbeQOTzC'
# username = ''
password = ''
# topic = "test_topic/1"
#topic = "test_topic/<api-labeldevice>"
topic = "/v2.0/devices/si-poco"
# mesin_topic = "/v2.0/devices/raspi/mesin"

def on_connect(client, userdata, flag, rc):
    print("Connected with result code "+str(rc))
    client.publish(topic, '{"tegangan":11}', qos=1) 
    # client.subscribe(mesin_topic,qos=1)

def on_publish(client, userdata, result):
    print("data published \n")

def on_message(client, userdata, msg):
    # print("Topic :"+msg.topic+"\nMessage:"+str(msg.payload.decode('utf-8')))
    if(msg.topic == mesin_topic):
        messageMqtt = json.loads(msg.payload.decode('utf-8'))
        if(messageMqtt['value'] == 1):
            #action to GPIO
            print("Motor Nyala")
        else:
            print("Motor Mati")


client = paho.Client("client1", userdata=None) #client ID name
client.username_pw_set(username=username, password=password)
client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message
client.connect(broker, port, timeout)
client.loop_forever()