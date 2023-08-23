import time
import json
import RPi.GPIO as GPIO
import paho.mqtt.client as paho
from paho import mqtt

broker = "industrial.api.ubidots.com"
port = 1883
timeout = 60

username = 'BBFF-GUCBVft9z4iaICE0uKzbl6kyhDFmiB'
password = ''
topic = "/v2.0/devices/sipoco/#"
# mesin_topic = "/v2.0/devices/raspi/mesin"
relaykipas_topic = "/v2.0/devices/sipoco/relaykipas"
relaylampu_topic = "/v2.0/devices/sipoco/relaylampu"

channelkipas = 23
channellampu = 24

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(channelkipas, GPIO.OUT)
GPIO.setup(channellampu, GPIO.OUT)



def on_connect(client, userdata, flag, rc):
    print("Connected with result code "+str(rc))
    
    client.subscribe(topic,qos=1)

def on_publish(client, userdata, result):
    print("data published \n")

def on_message(client, userdata, msg):
    print("Topic :"+msg.topic+"\nMessage:"+str(msg.payload.decode('utf-8')))
    if(msg.topic == relaykipas_topic):
        messageMqtt = json.loads(msg.payload.decode('utf-8'))
        if(messageMqtt['value'] == 1):
            #action to GPIO
            print("relay_kipas")
            relay_on(channelkipas)
        else:
            print("relay_kipas_mati")
            relay_off(channelkipas)

    if(msg.topic == relaylampu_topic):
        messageMqtt = json.loads(msg.payload.decode('utf-8'))
        if(messageMqtt['value'] == 1):
            #action to GPIO
            print("relay_lampu")
            relay_on(channellampu)
        else:
            print("relay_lampu_Mati")
            relay_off(channellampu)

def relay_off(pin):
    GPIO.output(pin, GPIO.HIGH)  # Turn motor on


def relay_on(pin):
    GPIO.output(pin, GPIO.LOW)  # Turn motor off


if __name__ == "__main__":
   
    client = paho.Client("sipoco", userdata=None) #client ID name
    client.username_pw_set(username=username, password=password)
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.on_message = on_message
    client.connect(broker, port, timeout)
    client.loop_forever()