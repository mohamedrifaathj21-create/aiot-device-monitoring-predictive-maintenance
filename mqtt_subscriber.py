import paho.mqtt.client as mqtt


BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "aiot/MCH-007/telemetry"


def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected to MQTT broker!")
    print("Subscribing to:", TOPIC)

    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    print("\nMessage received!")
    print("Topic:", msg.topic)
    print("Message:", msg.payload.decode())


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="MCH-007-subscriber"
)

client.on_connect = on_connect
client.on_message = on_message

print("Connecting to MQTT broker...")

client.connect(BROKER, PORT, 60)

client.loop_forever()