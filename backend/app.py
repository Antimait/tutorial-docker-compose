from paho.mqtt.client import Client
from flask import Flask
from flask_cors import CORS

import json
import random

data_dict = {}

with open("conf.json", "r") as c:
    conf = json.loads(c.read())


def on_connect(client, userdata, flags, rc):
    client.subscribe(conf["topic"])


def on_message(client, userdata, message):
    topic = message.topic.split("/")[-1]
    data_dict[topic] = message.payload.decode()
    print(data_dict)


c = Client(f"Client-{random.randint(100, 999)}")
c.on_connect = on_connect
c.on_message = on_message
c.connect(conf["broker"])
c.loop_start()

app = Flask(__name__)
CORS(app)


@app.route("/topics_data", methods=["GET"])
def get_data():
    return {"topics_data": data_dict}, 200
