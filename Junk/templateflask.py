from flask import Flask, request,jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

password = "sXgqDoMQeL9uVvv4"
uri = f"mongodb+srv://anggasetiaw:{password}@cluster0.dxsulqe.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['sic-mentor-angga'] # ganti sesuai dengan nama database kalian
my_collections = db['mentor'] # ganti sesuai dengan nama collections kalian

app = Flask(_name_)


@app.route('/sensor1', methods=['POST'])
def sensor1():
    try:
        data_coll = {'temperature':request.form.get('temperature', type=int),'kelembaban':request.form.get('kelembaban',type=int)}
        results = my_collections.insert_one(data_coll)
        return jsonify({"code":201,"message":f"{results}"})
    except Exception as e:
        return jsonify({"code":500,"message":e})
    
@app.route('/sensor1/kelembaban/avg', methods=['GET'])
def kelembabanavg():
    try:
        index = 0
        temp = 0
        for data in my_collections.find():
            temp = temp + data['kelembaban']
            index = index + 1
        if data == 0:
            return jsonify({"code":201,"message":"Rata rata temperature : 0"})
        else:
            hasil = temp / index

            return jsonify({"code":201,"message":f"Rata rata temperature : {hasil}"})
    except Exception as e:
        return jsonify({"code":500,"message":f"{e}"})

@app.route('/sensor1/temperature/avg', methods=['GET'])
def temperatureavg():
    try:
        index = 0
        temp = 0
        for data in my_collections.find():
            temp = temp + data['temperature']
            index = index + 1
        if data == 0:
            return jsonify({"code":201,"message":"Rata rata temperature : 0"})
        else:
            hasil = temp / index
            return jsonify({"code":201,"message":f"Rata rata temperature :{hasil}"})
    except Exception as e:
        return jsonify({"code":500,"message":e})

app.run(host='127.0.0.1', port=3000, debug=True)