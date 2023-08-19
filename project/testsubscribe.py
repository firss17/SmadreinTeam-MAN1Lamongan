import paho.mqtt.client as paho
from paho import mqtt
import json
from random import randint
import time
# define static variable
# broker = "mqtt-dashboard.com"
broker = "industrial.api.ubidots.com"
port = 1883
timeout = 60

username = 'BBFF-GUCBVft9z4iaICE0uKzbl6kyhDFmiB'
# username = ''
password = ''
# topic default "/v2.0/devices/label-devices"
publish = "/v2.0/devices/sipoco"
subscribe = "/v2.0/devices/sipoco"
# topic devices + label yang akan di suscribe
current1 = "/v2.0/devices/sipoco/current-1_a"
energy1 = "/v2.0/devices/sipoco/energy-1_wh"
frequency1 = "/v2.0/devices/sipoco/frequency-1_hz"
power1 = "/v2.0/devices/sipoco/power-1_w"
voltage1 = "/v2.0/devices/sipoco/voltage-1"
powerfactor1 = "/v2.0/devices/sipoco/powerfactor-1_"

def infocurrent1(data_current1):
    print(data_current1)

def infoenergy1(data_energy1):
    print(data_energy1)

def infofrequency1(data_frequency1):
    print(data_frequency1)

def infopower1(data_power1):
    print(data_power1)

def infovoltage1(data_voltage1):
    print(data_voltage1)

def infopowerfactor1(data_powerfactor1):
    print(data_powerfactor1)
    
def on_connect(client, userdata, flag, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(subscribe,qos=1)

def on_publish(client, userdata, result):
    print("data published \n")

def on_message(client, userdata, msg):
    # print("Topic :"+msg.topic+"\nMessage:"+str(msg.payload.decode('utf-8')))
    if(msg.topic == current1):
        data = json.loads(msg.payload.decode('utf-8'))
        infocurrent1(data['current-1_a'])
    elif(msg.topic == energy1):
        data = json.loads(msg.payload.decode('utf-8'))
        infoenergy1(data['energy-1_wh'])
    elif(msg.topic == frequency1):
        data = json.loads(msg.payload.decode('utf-8'))
        infofrequency1(data['frequency-1_hz'])

    elif(msg.topic == power1):
        data = json.loads(msg.payload.decode('utf-8'))
        infopower1(data['power-1_w'])

    elif(msg.topic == voltage1):
        data = json.loads(msg.payload.decode('utf-8'))
        infovoltage1(data['voltage-1'])

    elif(msg.topic == powerfactor1):
        data = json.loads(msg.payload.decode('utf-8'))
        infopowerfactor1(data['powerfacytor-1_'])

    else:
        print("error")

client = paho.Client("sipoco", userdata=None) #client ID tidakboleh sama
client.username_pw_set(username=username, password=password)
client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message
client.connect(broker, port, timeout)
client.loop_forever()