#!/usr/bin/env python3
import time
import json
from dotenv import load_dotenv
import os

import paho.mqtt.client as mqtt
from pa1010d import PA1010D

load_dotenv()
# MQTT setup
MQTT_BROKER = os.getenv("MQTT_BROKER", "192.168.0.180")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))

print("Broker details: ", MQTT_BROKER, MQTT_PORT)


mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)  # Updated to use the latest protocol version

mqtt_client.connect(MQTT_BROKER, MQTT_PORT , 60)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

mqtt_client.on_connect = on_connect

def publish_to_mqtt(data):
    mqtt_client.publish("gps/data", json.dumps(data))


gps = PA1010D()
 

while True:
    result = gps.update()
    j = {
        "timestamp": str(gps.data['timestamp']),
        "latitude": gps.data['latitude'],
        "longitude": gps.data['longitude'],
        "altitude": gps.data['altitude'],
        "num_sats": gps.data['num_sats'],
        "gps_qual": gps.data['gps_qual'],
        "speed_over_ground": gps.data['speed_over_ground'],
        "mode_fix_type": gps.data['mode_fix_type'],
        "pdop": gps.data['pdop'],
        "vdop": gps.data['vdop'],
        "hdop": gps.data['hdop']
    }
    if result:
        print(j)
        publish_to_mqtt(j)

    time.sleep(1.0)
