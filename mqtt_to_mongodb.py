import json
import os

import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from pymongo import MongoClient


load_dotenv()

MONGO_URI = os.getenv("MONGODB_URI")

if not MONGO_URI:
    print("ERROR: MONGODB_URI not found in .env")
    exit()


BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "aiot/MCH-007/telemetry"


print("Connecting to MongoDB Atlas...")

mongo_client = MongoClient(MONGO_URI)

db = mongo_client["aiot_database"]
collection = db["telemetry"]

mongo_client.admin.command("ping")

print("MongoDB Atlas connected successfully! ✅")


def on_connect(client, userdata, flags, reason_code, properties):

    print("Connected to MQTT broker! ✅")

    client.subscribe(TOPIC)

    print("Subscribed to:", TOPIC)


def on_message(client, userdata, msg):

    try:

        telemetry = json.loads(msg.payload.decode())

        result = collection.insert_one(telemetry)

        print("\nTelemetry received and saved to MongoDB! ✅")

        print("Topic:", msg.topic)
        print("Device:", telemetry["device_id"])
        print("Status:", telemetry["status"])
        print("MongoDB ID:", result.inserted_id)

    except Exception as e:

        print("Error processing message:", e)


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="MCH-007-mongodb-subscriber"
)

client.on_connect = on_connect
client.on_message = on_message


print("Connecting to MQTT broker...")

client.connect(BROKER, PORT, 60)


try:

    client.loop_forever()

except KeyboardInterrupt:

    print("\nStopping MQTT → MongoDB service...")

finally:

    client.disconnect()
    mongo_client.close()

    print("Disconnected.")