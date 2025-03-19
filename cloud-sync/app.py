from azure.eventhub import EventHubProducerClient, EventData
from dotenv import load_dotenv
import os

import paho.mqtt.client as mqtt

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = os.getenv("MQTT_TOPIC")
EVENT_HUB_CONNECTION_STR = os.getenv("EVENT_HUB_CONNECTION_STR")
EVENT_HUB_NAME = os.getenv("EVENT_HUB_NAME")


print(EVENT_HUB_CONNECTION_STR, EVENT_HUB_NAME)


# Callback when a message is received from the MQTT broker
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()}")
    send_to_event_hub(message.payload.decode())

# Function to send message to Azure Event Hub
def send_to_event_hub(message):
    producer = EventHubProducerClient.from_connection_string(conn_str=EVENT_HUB_CONNECTION_STR, eventhub_name=EVENT_HUB_NAME)
    event_data_batch = producer.create_batch()
    event_data_batch.add(EventData(message))
    producer.send_batch(event_data_batch)
    producer.close()

# Set up MQTT client
mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message

mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.subscribe(MQTT_TOPIC)

# Start the MQTT client
mqtt_client.loop_forever()