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

username = 'BBFF-JwhfZjHhOhkAoH4jq2bcVAl2IEF76r'
# username = ''
password = ''
# topic default "/v2.0/devices/label-devices"
publish = "/v2.0/devices/mentoring"
subscribe = "/v2.0/devices/mentoring/#"
# topic devices + label yang akan di suscribe
lampu = "/v2.0/devices/mentoring/lampu"
kulkas = "/v2.0/devices/mentoring/kulkas"

def getDataSensor1():
    #codingan sensor
    hasil_sensor = randint(0,100)
    return hasil_sensor

def getDataSensor2():
    #codingan sensor
    hasil_sensor = randint(0,100)
    return hasil_sensor

def menyalakanrelay(data_lampu):
    if(data_lampu == 1):
        print("menyalakan lampu")
    else:
        print("mematikan lampu")

def menyalakan_kulkas(data_kulkas):
    if(data_kulkas == 1):
        print("menyalakan kulkas")
    else:
        print("mematikan kulkas")

def on_connect(client, userdata, flag, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(subscribe,qos=1)

def on_publish(client, userdata, result):
    print("data published \n")

def on_message(client, userdata, msg):
    # print("Topic :"+msg.topic+"\nMessage:"+str(msg.payload.decode('utf-8')))
    if(msg.topic == lampu):
        data = json.loads(msg.payload.decode('utf-8'))
        menyalakanrelay(data['value'])
    elif(msg.topic == kulkas):
        data = json.loads(msg.payload.decode('utf-8'))
        menyalakan_kulkas(data['value'])


def run():
    while True:
        sensor1 = getDataSensor1()
        sensor2 = getDataSensor2()
        json_temp = {'ultrasonik':sensor1,'temperature':sensor2}
        payload = json.dumps(json_temp, indent=4)
        client.publish(publish,payload,qos=1)
        time.sleep(20)
        

client = paho.Client("Mentoring", userdata=None) #client ID tidakboleh sama
client.username_pw_set(username=username, password=password)
client.on_connect = on_connect
client.on_publish = on_publish
client.on_message = on_message
client.connect(broker, port, timeout)
# client.loop_forever()
#menjalankan periodic pengiriman Data
run()


