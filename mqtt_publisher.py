import json
import time

import paho.mqtt.client as mqtt

from device_simulator import generate_telemetry


BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "aiot/MCH-007/telemetry"


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="MCH-007-publisher"
)


print("Connecting to MQTT broker...")

client.connect(BROKER, PORT, 60)

print("Connected to MQTT broker!")


try:

    while True:

        # Generate telemetry from the actual simulator
        telemetry = generate_telemetry()

        # Convert Python dictionary to JSON
        message = json.dumps(telemetry)

        # Publish to MQTT
        result = client.publish(TOPIC, message)

        # Make sure the message was accepted
        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print("\nTelemetry published successfully!")
        else:
            print("\nFailed to publish telemetry.")

        print("Topic:", TOPIC)
        print("Message:", message)

        # Wait 5 seconds
        time.sleep(5)


except KeyboardInterrupt:

    print("\nStopping MQTT publisher...")


finally:

    client.disconnect()

    print("Disconnected from MQTT broker.")